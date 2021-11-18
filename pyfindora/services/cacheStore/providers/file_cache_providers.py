from os import read
from utils import createCacheDir, readFile, writeFile #'../../utils'
from types import CacheItem, CacheProvider
from pathlib import Path
import json

def read_cache(file_path: str):
    cache_data = {}

    print(f'reading file cache from {file_path}')

    try:
        if not Path(file_path).is_file():
            return cache_data
    except:
        print(f'File doesnt exist at "{file_path}", so returning default cache data')
        return cache_data

    try:
        file_content = readFile(file_path)
    except IOError:
        raise IOError(f'could not read file "{file_path}"')

    try:
        cache_data = json.loads(file_content)
    except:
        raise Exception(f'could not read parse cache data from "{file_content}"')

    return cache_data

def write_cache(file_path: str, data: CacheItem):
    print(f'writing file cache to "{file_path}"')

    try:
        cache_data = json.dumps(data)
    except:
        raise Exception(f'could not stringify data for cache "{data}"')

    try:
        createCacheDir(Path(file_path).parent.resolve())
    except:
        raise Exception(f'Failed to create directory, dir path: {Path(file_path).parent.resolve()}')

    try:
        result = writeFile(file_path, data)
    except:
        raise Exception(f'can not write cache for "{file_path}"')
    
    return result

class FileCacheProvider(CacheProvider):
    def read(entry_name: str):
        return read_cache(entry_name)

    def write(entry_name: str):
        return write_cache(entry_name)
