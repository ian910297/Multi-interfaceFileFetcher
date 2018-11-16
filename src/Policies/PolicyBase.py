"""
This is a abstract class defined for policy instance.

@author: FATESAIKOU
@date  : 16/11/2018
"""

import abc

class PolicyBase( abc.ABC ):
    @abc.abstractmethod
    def __init__( self, communicators ):
        return NoImplemented

    @abc.abstractmethod
    def SelectCommunicator( self, communicators ):
        return NoImplemented

    @abc.abstractmethod
    def UpdatePolicy( self, transfer_record ):
        return NoImplemented

