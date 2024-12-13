import ffmpeg
from .audio_output_path import audio_output_path


def extract_audio(video_file: str, output_directory: str):
    audio_codec = next(
        (stream['codec_name'] for stream in ffmpeg.probe(video_file)['streams'] if stream['codec_type'] == 'audio'),
        None
    )

    if not audio_codec:
        raise ValueError(f"No audio stream found in file: {video_file}")

    output_file = audio_output_path(audio_codec, input_file=video_file, output_directory=output_directory)

    (
        ffmpeg
        .input(video_file)
        .output(
            output_file,
            acodec="copy",
            vn=None
        ).run()
    )

    return output_file
