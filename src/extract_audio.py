import ffmpeg
import json
import os
from .audio_output_path import audio_output_path
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from _typeshed import SupportsWrite

def extract_audio(video_file: str):
    probed_video = ffmpeg.probe(video_file)

    base_name = os.path.splitext(os.path.basename(video_file))[0]
    cache_dir = os.path.join("cache", base_name)
    os.makedirs(cache_dir, exist_ok=True)

    f: SupportsWrite[str]
    with open(
        os.path.join(
            cache_dir,
            f"{base_name}.video.json"
        ),
        'w',
        encoding='utf-8'
    ) as f:
        json.dump(
            probed_video,
            f,
            ensure_ascii=False,
            indent=4,
            sort_keys=True
        )
        f.write('\n')

    audio_codec = next(
        (stream['codec_name'] for stream in probed_video['streams'] if stream['codec_type'] == 'audio'),
        None
    )

    if not audio_codec:
        raise ValueError(f'No audio stream found in file: {video_file}')

    output_file = audio_output_path(audio_codec, input_file=video_file)

    (
        ffmpeg
        .input(video_file)
        .output(
            output_file,
            acodec='copy',
            vn=None
        ).run(overwrite_output=True)
    )

    return output_file
