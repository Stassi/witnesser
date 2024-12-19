import json
import os
from dataclasses import dataclass
from typing import TYPE_CHECKING

import ffmpeg

from .ffmpeg_probe import FFMpegProbe
from .hash_digest import hash_digest

if TYPE_CHECKING:
    from _typeshed import SupportsWrite


@dataclass
class SaveVideoProbe:
    hash_digest: str
    probed_video: FFMpegProbe


def save_video_probe(video_file: str) -> SaveVideoProbe:
    probed_video: FFMpegProbe = ffmpeg.probe(video_file)

    json_str: str = json.dumps(
        ensure_ascii=False,
        indent=4,
        obj=probed_video,
        sort_keys=True
    ) + '\n'

    digest: str = hash_digest(json_str)
    cache_dir: str = os.path.join('cache', digest)

    os.makedirs(cache_dir, exist_ok=True)

    with open(
        encoding='utf-8',
        file=os.path.join(
            cache_dir,
            f'{os.path.splitext(os.path.basename(video_file))[0]}.av.json'
        ),
        mode='w',
    ) as f:
        f: SupportsWrite[str]
        f.write(json_str)

    return SaveVideoProbe(
        hash_digest=digest,
        probed_video=probed_video,
    )
