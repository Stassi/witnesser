import os


def audio_output_path(audio_codec: str, input_file: str) -> str:
    file_extension = {
        'aac': 'm4a',
        'ac3': 'ac3',
        'mp3': 'mp3',
        'opus': 'opus',
    }.get(audio_codec)

    if not file_extension:
        raise ValueError(f'Unsupported audio codec: {audio_codec}')

    base_name = os.path.splitext(os.path.basename(input_file))[0]

    cache_dir = os.path.join('cache', base_name)

    os.makedirs(cache_dir, exist_ok=True)

    return os.path.join(cache_dir, f'{base_name}.{file_extension}')
