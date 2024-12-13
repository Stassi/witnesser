import os


def audio_output_path(audio_codec: str, input_file: str, output_directory: str) -> str:
    file_extension = {
        'aac': 'm4a',
        'ac3': 'ac3',
        'mp3': 'mp3',
        'opus': 'opus',
    }.get(audio_codec)

    if not file_extension: raise ValueError(f"Unsupported audio codec: {audio_codec}")

    return os.path.join(
        output_directory,
        f"{os.path.splitext(os.path.basename(input_file))[0]}.{file_extension}"
    )
