import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc

def get_subsidy(height):
    halfreward = 10 * 100000000
    halvings = height // 788000
    if halvings >= 18:
        return 0
    return (halfreward >> halvings) + (halfreward >> ((height + 394000) // 788000))

nets = dict(
    bitmark=math.Object(
        P2P_PREFIX='f9beb4d9'.decode('hex'),
        P2P_PORT=9265,
        ADDRESS_VERSION=85,
        RPC_PORT=9266,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bitmarkaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: get_subsidy(height+1),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=120, # s
        SYMBOL='BTM',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitmark') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitmark/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitmark'), 'bitmark.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://cryptexplorer.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://cryptexplorer.com/address/',
        TX_EXPLORER_URL_PREFIX='http://cryptexplorer.com/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    bitmark_testnet=math.Object(
        P2P_PREFIX='0b110907'.decode('hex'),
        P2P_PORT=19265,
        ADDRESS_VERSION=130,
        RPC_PORT=19266,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bitmarkaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: get_subsidy(height+1),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=120, # s
        SYMBOL='tBTM',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitmark') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitmark/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitmark'), 'bitmark.conf'),
        BLOCK_EXPLORER_URL_PREFIX='',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
