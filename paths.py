from enum import Enum
from pathlib import Path


class Dir(Enum):
    root = Path(__file__).parent.resolve()
    static = root / 'static'

