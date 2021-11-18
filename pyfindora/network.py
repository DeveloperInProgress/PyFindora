import requests
import logging
import json 

class Network:
    def __init__(self, protocol, host, queryPort, submitPort, ledgerPort):
        self.config = {
            "protocol": protocol,
            "host": host,
            "queryPort": queryPort,
            "submitPort": submitPort,
            "ledgetPort": ledgerPort
        }
    
    @property
    def submitRoute(self):
        return f"{self.config['protocol']}://{self.config['host']}:{self.config['submitPort']}"

    @property
    def queryRoute(self):
        return f"{self.config['protocol']}://{self.config['host']}:{self.config['queryPort']}"

    @property
    def ledgerRoute(self):
        return f"{self.config['protocol']}://{self.config['host']}:{self.config['ledgerPort']}"

    async def getTxnStatus(self, handle):
        logging.info(f"request: {self.submitRoute}/txnStatus/{handle}")
        status = await requests.get(f"{this.submitRoute}/txnStatus/{handle}")
        logging.info(f"response: {status.data}")
        return status.content
    
    async def submitTransaction(self, txn):
        logging.info(f"request: {self.submitRoute}/submit_transaction")
        handle = await requests.post(f"{self.submitRoute}/submit_transaction",data=json.dumps(txn))
        logging.info(f"response: {status.data}")
        return status.content 

    async def getTxn(self, txnSid):
        logging.info(f"request: {self.ledgerRoute}/txn_sid/{txnSid}")
        txn = await requests.get(f"{self.ledgerRoute}/txn_sid/{txnSod}")
        return txn.content
    
    async def getAsset(self, code):
        logging.info(f"request: {self.ledgerRoute}/asset_token/{code}")
        asset = await requests.get(f"{self.ledgerRoute}/asset_token/{code}")
        return asset.content

    async def getIssuanceNum(self, code):
        logging.info(f"request: {self.ledgerRoute}/asset_issuance_num/{code}")
        asset = await requests.get(f"{self.ledgerRoute}/asset_issuance_num/{code}")
        return asset.content

    async def getAssetProperties(self, code):
        logging.info(f"request: {self.ledgerRoute}/asset_token/{code}")
        asset = await requests.get(f"{self.ledgerRoute}/asset_token/{code}")
        return asset.content.properties

    async def getStateCommitment(self):
        logging.info(f"request: {self.ledgerRoute}/global_state")
        stateCommitment = await requests.get(f"{this.ledgerRoute}/global_state")
        logging.info(stateCommitment.content)
        return stateCommitment.content

    async def getUtxo(self, utxoSid):
        logging.info(f"request: {self.ledgerRoute}/utxo_sid/{utxoSid}")
        res = await requests.get(f"{self.ledgerRoute}/utxo_sid/{utxoSid}")
        return res.content

    async def getAIRResult(self, addr):
        logging.info(f"request: {self.ledgerRoute}/air_address/{addr}")
        res = await requests.get(f"{self.ledgerRoute}/air_address/{addr}")
        return res.content

    async def getRelatedSids(self, address):
        logging.info(f"request: {self.queryRoute}/get_related_txns/{address}")
        sids = await requests.get(f"{self.queryRoute}/get_related_txns/{address}")
        return sids.content

    async def getRelatedXfrs(self, code):
        logging.info(f"request: {self.queryRoute}/get_related_xfrs/{code}")
        sids = await requests.get(f"{self.queryRoute}/get_related_xfrs/{code}")
        return sids.content

    async def getOwnedSids(self, address):
        logging.info(f'request: {self.queryRoute}/get_owned_utxos/{address}')
        sids = await requests.get(f"{self.queryRoute}/get_owned_utxos/{address}")
        return sids.content

    async def getOwnerMemo(self, utxoSid):
        logging.info(f'request: {self.queryRoute}/get_owner_memo/{utxoSid}')
        memo = await requests.get(f'{self.queryRoute}/get_owner_memo/{utxoSid}')
        return memo.content

    async def getCreatedAssets(self, address):
        logging.info(f'request: {self.queryRoute}/get_created_asset/{address}')
        sids = await requests.get(f'{self.queryRoute}/get_created_assets/{address}')
        return sids.content

    async def getTracedAssets(self, address):
        logging.info(f'request: {self.queryRoute}/get_traced_assets/{address}')
        sids = await requests.get(f'{self.queryRoute}/get_traced_assets'/{address})
        return sids.content

    async def getCustomData(self, key):
        logging.info(f'request: {self.queryRoute}/get_custom_data/{key}')
        result = await requests.get(f'{self.queryRoute}/get_custom_data/{key}')
        return result.content

    async def storeCustomData(self, customData):
        logging.info(f'request: {self.queryRoute}/store_custom_data')
        result = await requests.post(f'{self.queryRoute}/store_custom_data')
        return result.content

    async def getIssuedRecords(self, address):
        logging.info(f'request: {self.queryRoute}/get_issued_records/{address}')
        records = await requests.get(f'{self.queryRoute}/get_issued_records/{address}')
        return records.content

    async def getCustomDataHash(self, key):
        logging.log(f'request: ${self.ledgerRoute}/kv_lookup/{key}')
        result = await requests.get(f'{self.ledgerRoute}/kv_lookup/{key}')
        return result.content
