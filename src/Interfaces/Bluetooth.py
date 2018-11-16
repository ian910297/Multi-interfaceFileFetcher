"""
This is an easy implementation for transfer model file based on bluetooth.

@author: FATESAIKOU
@date  : 16/11/2018
"""

from InterfaceBase import InterfaceBase

class Bluetooth( InterfaceBase ):
    def __init__( self, name, address, model_root ):
        self.__name__       = name
        self.__address__    = address
        self.__model_root__ = model_root

    def HasFile( self, model_name ):
        pass

    def GetFile( self, model_name ):
        pass

    def GetProfile( self ):
        pass
