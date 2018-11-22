"""
This is a basic class defined for policy instance.

@author: FATESAIKOU
@date  : 17/11/2018
"""

from pprint import pprint

from .PolicyBase import PolicyBase

import random

class VeryFirstPolicy( PolicyBase ):
    def __init__( self, communicators ):
        self.__communicators__ = {
            comm.GetName(): comm for comm in communicators
        }
        self.__profiles__ = {
            comm.GetName(): comm.GetProfile()
            for comm in communicators
        }
        self.__BuildMaps__()

    def __BuildMaps__( self ):
        self.__action_map__ = { int(r): {} for r in list(self.__profiles__.items())[0][1].keys() }
        self.__state_map__ = list(self.__action_map__.keys())
        self.__state_map__.sort()

        for filesize in self.__action_map__.keys():
            for comm_name in self.__communicators__.keys():
                self.__action_map__[ filesize ][ comm_name ] = \
                    sum(self.__profiles__[ comm_name ][ str(filesize) ]) / len(self.__profiles__[ comm_name ][ str(filesize) ])

        pprint(self.__state_map__)
        pprint(self.__action_map__)

    def __DecodeState__( self, filesize ):
        for i in range(len(self.__state_map__)):
            s = self.__state_map__[i]
            if s > filesize:
                break
            now_state = s

        return now_state


    def Select( self, communicator_names, filesize ):
        # Get correct start state
        now_state = self.__DecodeState__(filesize)

        # Get action cand
        comm_ws = self.__action_map__[ now_state ]

        # Select action
        comm_name = random.choices(list(comm_ws.keys()), weights=[1 / comm_ws[n] for n in comm_ws.keys()])[0]

        return self.__communicators__[ comm_name ]

    def Update( self, communicator_name, transfer_record ):
        for filename in transfer_record.keys():
            record = transfer_record[filename]
            now_state = self.__DecodeState__(record[0])
            self.__action_map__[ now_state ][ communicator_name ] += record[1]
            self.__action_map__[ now_state ][ communicator_name ] /= 2
