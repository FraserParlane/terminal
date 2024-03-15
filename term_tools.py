from pathlib import Path
import json
import zlib
import sys
import os

def zlib_decompress() -> None:
    """Decompress a .zlib file to .json"""
    dir = Path(os.getcwd())
    src = dir / sys.argv[1]
    dst = dir / f'{src.stem}.json'
    with open(src, 'rb') as s, open(dst, 'wb') as d:
        print(zlib.decompress(s.read()))