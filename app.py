import sys
import os

import tornado.ioloop
import tornado.web

from tornado.log import enable_pretty_logging

sys.path.insert(1, os.path.join(sys.path[0], 'lib'))

import config
import log
from log import info
from handlers.buildings import BuildingsByZipCodeHandler, BuildingsByAddYearHandler


def make_app(conf):
    settings = {
        'conf' : conf
    }
    return tornado.web.Application([
        (r"/buildings/by_zip_code/((?:\d+(?:,\d+)*)*)", BuildingsByZipCodeHandler, settings),
        (r"/buildings/by_year/((?:\d+(?:,\d+)*)*)", BuildingsByAddYearHandler, settings)
    ])

if __name__ == "__main__":
    log.init()
    enable_pretty_logging()
    conf = config.load()
    app = make_app(conf)
    app.listen(conf['http_port'])
    info('Listening on port %d' % conf['http_port'])
    tornado.ioloop.IOLoop.current().start()
