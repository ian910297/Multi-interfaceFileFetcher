"""
This is a abstract class defined for interface instance.

@author: FATESAIKOU
@date  : 16/11/2018
"""

import abc

class InterfaceBase( abc.ABC ):
    @abc.abstractmethod
    def __init__( self, name, address, model_root ):
        return NoImplemented

    @abc.abstractmethod
    def HasFile( self, model_name ):
        return NoImplemented

    @abc.abstractmethod
    def GetFile( self, model_name, save_path ):
        return NoImplemented

    @abc.abstractmethod
    def GetProfile( self ):
        return NoImplemented
