#Client messages
CMSG_IDENTIFY = 0
CMSG_BLOCKCHANGE = 5
CMSG_POSITIONUPDATE = 8
CMSG_MESSAGE = 13
#End!
#Server Messages
SMSG_INITIAL = 0
SMSG_KEEPALIVE = 1
SMSG_PRECHUNK = 2
SMSG_CHUNK = 3
SMSG_LEVELSIZE = 4
SMSG_BLOCKCHANGE = 5
SMSG_BLOCKSET = 6
SMSG_SPAWNPOINT = 7
SMSG_PLAYERPOS = 8
SMSG_PLAYERDIR = 11
SMSG_PLAYERLEAVE = 12
SMSG_MESSAGE = 13
SMSG_ERROR = 14

#Sizes of CMSG packets.
PacketSizes = {
    CMSG_IDENTIFY: 130,
    CMSG_BLOCKCHANGE: 8,
    CMSG_POSITIONUPDATE: 9,
    CMSG_MESSAGE: 65
}
#Block types
BLOCK_AIR = 0
BLOCK_ROCK = 1
BLOCK_GRASS = 2
BLOCK_DIRT = 3
BLOCK_STONE = 4
BLOCK_WOOD = 5
BLOCK_PLANK = 5
BLOCK_PLANT = 6
BLOCK_HARDROCK = 7
BLOCK_WATER = 8
BLOCK_STILLWATER = 9
BLOCK_LAVA = 10
BLOCK_STILLLAVA = 11
BLOCK_SAND = 12
BLOCK_GRAVEL = 13
BLOCK_GOLDORE = 14
BLOCK_COPPERORE = 15
BLOCK_COALORE = 16
BLOCK_LOG = 17
BLOCK_LEAVES = 18
BLOCK_SPONGE = 19
BLOCK_GLASS = 20
BLOCK_RED_CLOTH = 21
BLOCK_ORANGE = 22
BLOCK_YELLOW = 23
BLOCK_LIME = 24
BLOCK_GREEN = 25
BLOCK_TEAL = 26
BLOCK_CYAN = 27
BLOCK_BLUE = 28
BLOCK_PURPLE = 29
BLOCK_INDIGO = 30
BLOCK_VIOLET = 31
BLOCK_MAGENTA = 32
BLOCK_PINK = 33
BLOCK_DARKGREY = 34
BLOCK_BLACK = 34
BLOCK_GREY = 35
BLOCK_WHITE = 36
BLOCK_REDFLOWER = 38
BLOCK_MUSHROOM = 39
BLOCK_RED_MUSHROOM = 40
BLOCK_GOLD = 41
BLOCK_STEEL = 42
BLOCK_IRON = 42
BLOCK_DOUBLESTEP = 43
BLOCK_STEP = 44
BLOCK_BRICK = 45
BLOCK_TNT = 46
BLOCK_BOOKCASE = 47
BLOCK_MOSSYROCK = 48
BLOCK_OBSIDIAN = 49
BLOCK_END = 50

DisabledBlocks = set([BLOCK_WATER,BLOCK_STILLWATER,BLOCK_LAVA,BLOCK_STILLLAVA,BLOCK_HARDROCK])

#Permission ranks
#These are subject to change as more ranks are added over time.
# 0 = Builder
# 1 = Operator
# 2 = Admin
# 3 = Owner

RankToName = {
    "" : "",
    "a": "Admin",
    "b": "Builder",
    "o": "Operator",
    "z": "Owner"
}
RankToColour = {
    "" : "",
    "a": "&9", #Blue
    "b": "&a", #Light green
    "o": "&b", #Teal
    "z": "&c" #Red
}
RankToLevel = {
    "" : 5,
    "z": 0xFF,
    "b": 10,
    "o": 20,
    "a": 30,
}