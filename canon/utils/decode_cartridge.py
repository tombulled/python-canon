from .. import constants

"""
Imports:
    ..constants

Contains:
    decode_cartridge()
"""

def decode_cartridge(cartridge, legacy=False):
    """
    Decode a cartridge (list of 3 indexs)
    ... into human-readable values
    """

    lvl = constants.ink.LVL[cartridge[constants.ink.INDEX_LVL]]
    mrk = constants.ink.MRK[cartridge[constants.ink.INDEX_MRK]]
    col = constants.ink.COL[cartridge[constants.ink.INDEX_COL]]
    sym = constants.ink.SYM[cartridge[constants.ink.INDEX_SYM]]

    sym_message = constants.messages.MESSAGES[sym]

    level = constants.ink.LEVEL[cartridge[constants.ink.INDEX_LEVEL]]
    message = constants.ink.MESSAGE[cartridge[constants.ink.INDEX_MESSAGE]]
    colour = constants.ink.COLOUR[cartridge[constants.ink.INDEX_COLOUR]]
    code = constants.ink.CODE[cartridge[constants.ink.INDEX_CODE]]

    decoded_cartridge = \
    {
        '_legacy': \
        {
            'lvl': lvl,
            'mrk': mrk,
            'col': col,
            'sym': sym,
            'sym_message': sym_message,
        },
        'level': level,
        'message': message,
        'colour': colour,
        'code': code,
    }

    if not legacy:
        decoded_cartridge.pop('_legacy')

    return decoded_cartridge
