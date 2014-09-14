import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc

def get_subsidy(height):
    if height < 17291:
        return 347 * 100000000
    halvings = height // 240000
    if halvings >= 64:
        return 0
    return (50 * 100000000) >> halvings

nets = dict(
    globalboosty=math.Object(
        P2P_PREFIX='a2b2e2f2'.decode('hex'),
        P2P_PORT=8226,
        ADDRESS_VERSION=77,
        RPC_PORT=8225,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'globalboostaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: get_subsidy(height+1),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('yescrypt_hash').getHash(data, 80)),
        BLOCK_PERIOD=600, # s
        SYMBOL='BSTY',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'GlobalBoost-Y') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/GlobalBoost-Y/') if platform.system() == 'Darwin' else os.path.expanduser('~/.globalboosty'), 'globalboost.conf'),
        BLOCK_EXPLORER_URL_PREFIX='',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//10000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
