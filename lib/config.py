
import yaml
import sys
import os

import utils

from log import info, error

IS_FROZEN = getattr(sys, 'frozen', False)

HOME_DIR = os.path.join(os.path.dirname(sys.executable)) \
    if IS_FROZEN else \
    os.path.dirname(os.path.abspath(__file__)).replace('lib', '')


DATA_DIR = os.path.join(HOME_DIR, 'data')
CONF_DIR = os.path.join(HOME_DIR, 'conf')



CONF_MAIN_FILE = 'main.yaml'
CONF_FILE_DEFAULT = os.path.join(CONF_DIR, CONF_MAIN_FILE)

CONF_DEFAULTS = {
    'db_path' : os.path.join(DATA_DIR, 'arcgis.db'),
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
        error('Failed to load file %s: %s' % (fname, exc))
    return conf

def load(conf_file=None):
    conf_file = conf_file or CONF_FILE_DEFAULT
    utils.makedirs([CONF_DIR, DATA_DIR])
    info("Loading config at %s" % conf_file)
    load_file(CONF, conf_file)
    return CONF
