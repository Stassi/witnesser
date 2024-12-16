from typing import (
    Any,
    Dict,
    List,
    TypedDict,
)

from .ffmpeg_stream import FFMpegStream


class FFMpegProbe(TypedDict):
    format: Dict[str, Any]
    streams: List[FFMpegStream]
