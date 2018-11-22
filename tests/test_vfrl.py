"""
A test file for ModelGetter (very first rl)

@author: FATESAIKOU
@date  : 17/11/2018
"""

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from ModelGetter.ModelGetter import ModelGetter
import json
import random
import time

CONFIG = sys.argv[1]

def load_config( config_path ):
    with open(config_path, 'r') as src:
        config_obj = json.loads(src.read())

    return config_obj

def extract_config( config_obj ):
    if_desc = []

    for n in config_obj.keys():

        if_info = config_obj[n]
        if 'wifi' not in if_info.keys():
            continue

        if_desc.append('Scp,' + n + '_scp,'+ if_info['wifi'] + ',' + if_info['model_root'] +',../scripts')
        if_desc.append('Ftp,' + n + '_ftp,'+ if_info['wifi'] + ',' + if_info['model_root'] +',../scripts')

        if 'bluetooth' in if_info.keys():
            if_desc.append('Bluetooth,' + n + '_bt,'+ if_info['wifi'] + ',' +
                    if_info['bluetooth'][0] +  ',' + if_info['bluetooth'][1] + ',model_root,../scripts')

    return if_desc

def main():
    config_obj = load_config( CONFIG )
    if_desc = extract_config( config_obj )
    p_desc = 'VFRL'

    mg = ModelGetter(interface_descriptors=if_desc, policy_descriptor=p_desc)

    cnt = 0
    while True:
        target_model = random.choice([ "mdl1", "mdl2" ])

        time_cost = mg.GetModel(target_model)
        cnt += 1
        print("[Round {}][Cost {}]".format(cnt, time_cost))


if __name__ == '__main__':
    main()

