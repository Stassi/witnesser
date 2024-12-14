import ffmpeg
import json
import os
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from _typeshed import SupportsWrite

def save_video_probe(video_file: str):
    probed_video = ffmpeg.probe(video_file)

    base_name: str = os.path.splitext(os.path.basename(video_file))[0]
    cache_dir: str = os.path.join('cache', base_name)

    os.makedirs(cache_dir, exist_ok=True)

    with open(
        encoding='utf-8',
        file=os.path.join(
            cache_dir,
            f'{base_name}.av.json'
        ),
        mode='w',
    ) as f:
        f: SupportsWrite[str]
        json.dump(
            probed_video,
            f,
            ensure_ascii=False,
            indent=4,
            sort_keys=True
        )
        f.write('\n')

    return probed_video
