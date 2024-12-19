import ffmpeg

from .audio_codec_name import audio_codec_name
from .audio_output_path import audio_output_path
from .save_video_probe import SaveVideoProbe, save_video_probe


def save_audio(video_file: str) -> str:
    probe: SaveVideoProbe = save_video_probe(video_file)

    audio_file: str = audio_output_path(
        audio_codec=audio_codec_name(probe.probed_video),
        hash_digest=probe.hash_digest,
        video_file=video_file,
    )

    (
        ffmpeg
        .input(video_file)
        .output(
            audio_file,
            acodec='copy',
            vn=None
        ).run(overwrite_output=True)
    )

    return audio_file
