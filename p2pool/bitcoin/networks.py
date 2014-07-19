import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc

nets = dict(
    viacoin=math.Object(
        P2P_PREFIX='0f68c6cb'.decode('hex'),
        P2P_PORT=5223,
        ADDRESS_VERSION=71,
        RPC_PORT=5222,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'viacoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: __import__('viacoin_subsidy').getBlockBaseValue(height+1),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=24, # s
        SYMBOL='VIA',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Viacoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Viacoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.viacoin'), 'viacoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    viacoin_testnet=math.Object(
        P2P_PREFIX='a9c5ef92'.decode('hex'),
        P2P_PORT=25223,
        ADDRESS_VERSION=127,
        RPC_PORT=25222,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'viacoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: __import__('viacoin_subsidy').getBlockBaseValue_testnet(height+1),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=24, # s
        SYMBOL='tVIA',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Viacoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Viacoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.viacoin'), 'viacoin.conf'),
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
