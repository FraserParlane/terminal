from pathlib import Path
import json
import zlib
import sys
import os

def zlib_decompress() -> None:
    """Decompress a .zlib file to .json"""
    directory = Path(os.getcwd())
    source = directory / sys.argv[1]
    dest = directory / f'{source.stem}.json'
    with open(source, 'rb') as s, open(dest, 'w') as d:
        jsondict = json.loads(zlib.decompress(s.read()).decode("utf-8"))
        json.dump(jsondict, d, indent=4)
        
def zlib_compress() -> None:
    """Compress a .json to .zlib"""
    directory = Path(os.getcwd())
    directory = Path(os.getcwd())
    source = directory / sys.argv[1]
    dest = directory / f'{source.stem}.zlib'
    with open(source, 'r') as s, open(dest, 'wb') as d:
        bstring = json.dumps(json.load(s)).encode('utf-8')
        d.write(zlib.compress(bstring))
