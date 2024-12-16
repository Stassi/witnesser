from .save_video_probe import FFMpegProbe


def audio_codec_name(probed_video: FFMpegProbe) -> str:
    codec_name: str | None = next(
        (
            stream['codec_name']
            for stream in probed_video['streams']
            if stream['codec_type'] == 'audio'
        ),
        None
    )

    if not codec_name:
        raise ValueError('No audio stream found in probed video')
    
    return codec_name
