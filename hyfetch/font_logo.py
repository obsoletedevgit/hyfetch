import json
from pathlib import Path

from hyfetch.constants import CACHE_PATH
from hyfetch.neofetch_util import get_distro_name


def levenshtein_distance(s1: str, s2: str) -> int:
    # Create a matrix to hold the distances
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def get_font_logo() -> str:
    cache = CACHE_PATH / 'font_logo_cache.txt'
    if cache.exists():
        return cache.read_text('utf-8')

    font_logos: dict[str, str] = json.loads((Path(__file__).parent / 'data/font_logos.json').read_text('utf-8'))

    # Get the distro
    distro = get_distro_name()

    # Find most likely distro by textual similarity
    distro = min(font_logos.keys(), key=lambda x: levenshtein_distance(x, distro))

    logo = font_logos[distro]
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(logo)

    return logo

