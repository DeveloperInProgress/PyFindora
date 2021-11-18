sdk_default_env = {
    'hostUrl': 'https://dev-evm.dev.findora.org',
    'queryPort': '8667',
    'ledgerPort': '8668',
    'submissionPort': '8669',
    'explorerApiPort': '26657',
}

class Sdk:
    environment = sdk_default_env

    def init(sdkEnv):
        Sdk.environment = sdkEnv

    def reset():
        Sdk.environment = sdk_default_env

    def set_utxo_data(
        wallet_address: str,
        utxo_cache #define CacheItem
    ): 
        cache_data_to_save = {}
        for item in utxo_cache:
            cache_data_to_save[f"sid_{item['sid']}"] = item
        
