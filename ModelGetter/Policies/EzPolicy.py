"""
This is a basic class defined for policy instance.

@author: FATESAIKOU
@date  : 17/11/2018
"""

from .PolicyBase import PolicyBase

import random

class DummyPolicy( PolicyBase ):
    def __init__( self, communicators ):
        self.__communicator__ = {
            comm.GetName(): comm for comm in communicators
        }

    def Select( self, communicator_names, filesize ):
        return self.__communicator__[ random.choice(communicator_names) ]

    def Update( self, transfer_record ):
        pass
