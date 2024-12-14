import ffmpeg
from .audio_output_path import audio_output_path
from .save_video_probe import save_video_probe


def save_audio(video_file: str):
    probed_video = save_video_probe(video_file)

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
