import sys
import os

import tornado.ioloop
import tornado.web

sys.path.insert(1, os.path.join(sys.path[0], 'lib'))

import config
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
    conf = config.load()
    app = make_app(conf)
    app.listen(conf['http_port'])
    print('Listening on port %d' % conf['http_port'])
    tornado.ioloop.IOLoop.current().start()
