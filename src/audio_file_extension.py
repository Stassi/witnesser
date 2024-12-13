def audio_file_extension(audio_codec: str) -> str:
    file_extension: str | None = {
        'aac': 'm4a',
        'ac3': 'ac3',
        'flac': 'flac',
        'mp3': 'mp3',
        'opus': 'opus'
    }.get(audio_codec)

    if not file_extension:
        raise ValueError(f'Unsupported audio codec: {audio_codec}')

    return file_extension
