import sys
import logging
import os

from functools import partial

logger = None

def init(*agrs, **kwargs):
    global logger

    log_level = logging.DEBUG if kwargs.get('debug') else logging.INFO
    logger = logging.getLogger('main')

    formatter = logging.Formatter(
        '{%(levelname)s}:%(asctime)s.%(msecs)03d %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.setLevel(log_level)


def write(msg, level):
    if not logger:
        logging.error("Log module not initialized, run log.init before usage")
        sys.exit(1)
    log_f = getattr(logger, level, None)
    log_f(msg)


warn = partial(write, level='warn')
info = partial(write, level='info')
debug = partial(write, level='debug')
error = partial(write, level='error')
