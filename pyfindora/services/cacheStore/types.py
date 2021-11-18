class CacheItem:
    key = None

class CacheProvider:
    def read(entry_name: str):
        pass

    def write(entry_name: str):
        pass
    
    def prune():
        pass

class CacheFactory:
    def read(entry_name: str, provider: CacheProvider):
        pass

    def write(entry_name: str, provider: CacheProvider):
        pass 

    def prune(provider: CacheProvider):
        pass 
