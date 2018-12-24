"""
This is a basic class defined for policy instance.

@author: demonic
@date  : 17/11/2018
"""

from pprint import pprint

from .PolicyBase import PolicyBase

import random
import itertools
import bisect
import math
import time

class SoftmaxPolicy( PolicyBase ):
    def __init__( self, communicators, timerate=0.8 ):
        self.__communicators__ = {
            comm.GetName(): comm for comm in communicators
        }
        self.__profiles__ = {
            comm.GetName(): comm.GetProfile()
            for comm in communicators
        }
        self.__BuildMaps__()
        self.timerate = timerate

    def __BuildMaps__( self ):
        self.__action_map__ = { int(r): {} for r in list(self.__profiles__.items())[0][1].keys() }
        self.__state_map__ = list(self.__action_map__.keys())
        self.__state_map__.sort()

        for filesize in self.__action_map__.keys():
            #print('filesize', filesize)
            for comm_name in self.__communicators__.keys():
                #print('action_map', self.__action_map__[filesize])
                self.__action_map__[ filesize ][ comm_name ] = {}
                self.__action_map__[ filesize ][ comm_name ]['value'] = \
                    sum(self.__profiles__[ comm_name ][ str(filesize) ]) / len(self.__profiles__[ comm_name ][ str(filesize) ])
                self.__action_map__[ filesize ][ comm_name ]['timestamp'] = time.time()
                self.__action_map__[ filesize ][ comm_name ]['times'] = 0

        pprint(self.__state_map__)
        pprint(self.__action_map__)

    def __DecodeState__( self, filesize ):
        for i in range(len(self.__state_map__)):
            s = self.__state_map__[i]
            if s > filesize:
                break
            now_state = s

        return now_state

    def __WeightChoice__( self, weighted_dict ):
        comm_names = list(weighted_dict.keys())
        comm_ws = [1 / weighted_dict[n]['value'] for n in weighted_dict.keys()]

        # softmax
        comm_ws_exp = [math.exp(n) for n in comm_ws]
        sum_comm_ws_exp = sum(comm_ws_exp)
        softmax_comm_ws = [round(n / sum_comm_ws_exp, 3) for n in comm_ws_exp]

        # random select
        cumdlist = list(itertools.accumulate(softmax_comm_ws))
        x = random.random() * cumdlist[-1]

        return comm_names[bisect.bisect(cumdlist, x)]

    def Select( self, communicator_names, filesize ):
        # Get correct start state
        now_state = self.__DecodeState__(filesize)

        # Get action cand
        comm_ws = self.__action_map__[ now_state ]

        # Select action
        comm_name = self.__WeightChoice__(comm_ws)

        print("use: " + comm_name)

        return self.__communicators__[ comm_name ]

    def Update( self, communicator_name, transfer_record ):
        print(transfer_record)
        for filename in transfer_record.keys():
            record = transfer_record[filename]
            now_state = self.__DecodeState__(record[0])
            
            value = self.__action_map__[ now_state ][ communicator_name ]['value']
            last_timestamp = self.__action_map__[ now_state ][ communicator_name ]['timestamp']
            timestamp = time.time()
            value = record[1] * self.timerate + value * (1 - self.timerate)
            
            self.__action_map__[ now_state ][ communicator_name ]['timestamp'] = timestamp
            self.__action_map__[ now_state ][ communicator_name ]['times'] += 1
            self.__action_map__[ now_state ][ communicator_name ]['value'] = value
