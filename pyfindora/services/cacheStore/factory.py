from types import CacheFactory, CacheItem, CacheProvider

class Factory(CacheFactory):

    def read(entry_name: str, provider: CacheProvider):
        return provider.read(entry_name)

    def write(
        entry_name: str,
        data: CacheItem,
        provider: CacheProvider
    ):
        return provider.write(entry_name, data)

    def prune(provider: CacheProvider):
        if provider.prune:
            return provider.prune()
        else:
            return True

factory = Factory()