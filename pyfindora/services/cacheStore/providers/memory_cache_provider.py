from types import CacheItem, CacheProvider

class MemoryCache:
    data = {}

def readCache(filename: str):
    cacheData = {}
    cacheData = MemoryCache.data[filename]
    return cacheData

def writeCache(filename: str, data: CacheItem):
    MemoryCache.data[filename] = data 
    return True 

class MemoryCacheProvider(CacheProvider):
    def read(entry_name: str):
        return readCache(entry_name)

    def write(entry_name: str, data: CacheItem):
        return writeCache(entry_name, data)
