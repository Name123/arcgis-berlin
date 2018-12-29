
import yaml
import sys
import os

import utils

IS_FROZEN = getattr(sys, 'frozen', False)

HOME_DIR = os.path.join(os.path.dirname(sys.executable)) \
    if IS_FROZEN else \
    os.path.dirname(os.path.abspath(__file__)).replace('lib', '')


DATA_DIR = os.path.join(HOME_DIR, 'data')
CONF_DIR = os.path.join(HOME_DIR, 'conf')



CONF_MAIN_FILE = 'main.yaml'

CONF_DEFAULTS = {
    'db' : 'arcgis.db',
    'http_port' : 8888
}
CONF = {}

def load_file(conf, fname):
    try:
        with open(fname, 'r') as stream:
            cfg = yaml.load(stream)
            for k in CONF_DEFAULTS.keys():
                conf[k] = cfg.get(k, CONF_DEFAULTS[k])
    except yaml.YAMLError as exc:
        print('Failed to load file %s: %s' % (fname, exc)) # should be log error
    return conf

def postprocess(conf):
    conf['db_path'] = os.path.join(DATA_DIR, conf['db'])    

def load():
    utils.makedirs([CONF_DIR, DATA_DIR])
    load_file(CONF, os.path.join(CONF_DIR, CONF_MAIN_FILE))
    postprocess(CONF)
    return CONF
