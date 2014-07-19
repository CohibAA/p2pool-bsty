from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    viacoin=math.Object(
        PARENT=networks.nets['viacoin'],
        SHARE_PERIOD=12, # seconds
        CHAIN_LENGTH=24*60*60//12, # shares
        REAL_CHAIN_LENGTH=24*60*60//12, # shares
        TARGET_LOOKBEHIND=100, # shares
        SPREAD=75, # blocks
        IDENTIFIER='e56c8153003ff886'.decode('hex'),
        PREFIX='5f6feddad82fc2cd'.decode('hex'),
        P2P_PORT=4223,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=4222,
        BOOTSTRAP_ADDRS='via.altmine.net'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-via',
        VERSION_CHECK=lambda v: True,
    ),
    viacoin_testnet=math.Object(
        PARENT=networks.nets['viacoin_testnet'],
        SHARE_PERIOD=12, # seconds
        CHAIN_LENGTH=24*60*60//12, # shares
        REAL_CHAIN_LENGTH=24*60*60//12, # shares
        TARGET_LOOKBEHIND=100, # shares
        SPREAD=75, # blocks
        IDENTIFIER='81d8b4e3586137e3'.decode('hex'),
        PREFIX='63828c41275aef3c'.decode('hex'),
        P2P_PORT=24223,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=24222,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
