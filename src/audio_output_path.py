import os

from .audio_file_extension import audio_file_extension


def audio_output_path(
    audio_codec: str,
    hash_digest: str,
    video_file: str
) -> str:
    base_name: str = os.path.splitext(
        os.path.basename(video_file)
    )[0]
    cache_dir: str = os.path.join('cache', hash_digest)

    os.makedirs(cache_dir, exist_ok=True)

    return os.path.join(
        cache_dir,
        f'{base_name}.{audio_file_extension(audio_codec)}'
    )
