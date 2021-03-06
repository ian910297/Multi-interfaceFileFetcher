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
    def Select( self, communicator_names, filesize ):
        return NoImplemented

    @abc.abstractmethod
    def Update( self, communicator_name, transfer_record ):
        return NoImplemented

