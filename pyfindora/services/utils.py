import binascii
from pathlib import Path

def int_array_to_hex_str(input: list):
    return binascii.hexlify(bytearray(input))

def writeFile(filename: str, cacheData: str):
    try:
        f = open(filename, 'w')
        f.write(cacheData)
    except IOError:
        raise IOError

    return True

def readFile(filename: str, cacheData: str):
    try:
        f = open(filename, 'r')
        data = f.read()
    except IOError:
        raise IOError

    return data

def createCacheDir(dirPath: str):
    return Path(dirPath).mkdir(parents=True, exist_ok=True)
