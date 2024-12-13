import ffmpeg
import json
import os
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from _typeshed import SupportsWrite

def save_video_probe(video_file: str):
    probed_video = ffmpeg.probe(video_file)

    base_name = os.path.splitext(os.path.basename(video_file))[0]
    cache_dir = os.path.join('cache', base_name)
    os.makedirs(cache_dir, exist_ok=True)

    f: SupportsWrite[str]
    with open(
        os.path.join(
            cache_dir,
            f'{base_name}.av.json'
        ),
        'w',
        encoding='utf-8'
    ) as f:
        json.dump(
            probed_video,
            f,
            ensure_ascii=False,
            indent=4,
            sort_keys=True
        )
        f.write('\n')

    return probed_video
