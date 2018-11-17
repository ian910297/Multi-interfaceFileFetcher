"""
This is an easy implementation for transfer model file based on ethernet.

@author: FATESAIKOU
@date  : 16/11/2018
"""

from InterfaceBase import InterfaceBase

class Scp( InterfaceBase ):
    def __init__( self, name, address, model_root, script_dir ):
        self.__name__       = name
        self.__address__    = address
        self.__model_root__ = model_root
        self.__script_dir__ = script_dir

    def HasFile( self, model_name ):
        pass

    def GetFile( self, model_name ):
        pass

    def GetProfile( self ):
        pass

class Ftp( InterfaceBase ):
    def __init__( self, name, address, model_root, script_dir ):
        self.__name__       = name
        self.__address__    = address
        self.__model_root__ = model_root
        self.__script_dir__ = script_dir

    def HasFile( self, model_name ):
        pass

    def GetFile( self, model_name ):
        pass

    def GetProfile( self ):
        pass
