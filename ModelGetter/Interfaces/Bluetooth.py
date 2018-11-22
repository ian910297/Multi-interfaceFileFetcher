"""
This is an easy implementation for transfer model file based on bluetooth.

@author: FATESAIKOU
@date  : 16/11/2018
"""

from .InterfaceBase import InterfaceBase

import subprocess
import json

class Obexftp( InterfaceBase ):
    def __init__( self, name, ip_address, bluetooth_address,
            bluetooth_channel, model_root, script_dir ):
        self.__name__              = name
        self.__ip_address__        = ip_address
        self.__bluetooth_address__ = bluetooth_address
        self.__bluetooth_channel__ = bluetooth_channel
        self.__model_root__        = model_root
        self.__script_dir__        = script_dir
        self.__profile__           = None

    def __RenewProfile__( self ):
        profile_str = subprocess.check_output([
            self.__script_dir__ + '/bluetooth_test.sh',
            self.__ip_address__,
            self.__model_root__,
            self.__bluetooth_address__,
            self.__bluetooth_channel__,
            self.__model_root__,
            '16384'
        ]).decode('utf8')

        self.__profile__ = json.loads(profile_str)

    def GetName( self ):
        return self.__name__

    def GetFileInfo( self, model_name ):
        filelist_str = subprocess.check_output([
            self.__script_dir__ + '/bluetooth_list.sh',
            self.__bluetooth_address__,
            self.__bluetooth_channel__,
            self.__model_root__
        ]).decode('utf8')

        list_result = json.loads(filelist_str)

        if model_name not in list_result.keys():
            return None

        return list_result[model_name]

    def GetFile( self, model_name ):
        report_str = subprocess.check_output([
            self.__script_dir__ + '/bluetooth_get.sh',
            self.__bluetooth_address__,
            self.__bluetooth_channel__,
            self.__model_root__,
            model_name,
            self.__model_root__
        ]).decode('utf8')

        return json.loads(report_str)

    def GetProfile( self, renew=False ):
        if renew or self.__profile__ == None:
            self.__RenewProfile__()

        return self.__profile__
