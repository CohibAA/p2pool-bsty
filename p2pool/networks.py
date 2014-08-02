from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    bitmark=math.Object(
        PARENT=networks.nets['bitmark'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//15, # shares
        REAL_CHAIN_LENGTH=24*60*60//15, # shares
        TARGET_LOOKBEHIND=60, # shares
        SPREAD=15, # blocks
        IDENTIFIER='f45ede06eb19208e'.decode('hex'),
        PREFIX='8738715de4920815'.decode('hex'),
        P2P_PORT=8265,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8266,
        BOOTSTRAP_ADDRS='btm.altmine.net'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-btm',
        VERSION_CHECK=lambda v: True,
    ),
    bitmark_testnet=math.Object(
        PARENT=networks.nets['bitmark_testnet'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//15, # shares
        REAL_CHAIN_LENGTH=24*60*60//15, # shares
        TARGET_LOOKBEHIND=60, # shares
        SPREAD=15, # blocks
        IDENTIFIER='da4ee7e3545af544'.decode('hex'),
        PREFIX='4a14a768ce407892'.decode('hex'),
        P2P_PORT=18265,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=18266,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
