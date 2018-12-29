#!/usr/bin/env python3

import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..', 'lib'))

import db.sync.misc as db
import db.sync.buildings as buildings
import arcgis.request as arcgis

import config

BATCH_SIZE = 1000


def fetch_all(id_obj_start, batch_size):
    while True:
        id_obj_end = id_obj_start + batch_size
        print('Fetching next batch: from %d to %d' % (id_obj_start, id_obj_end))
        response = arcgis.fetch_range(id_obj_start, id_obj_end)
        yield response
        print('Fetched %d records' % len(response))
        if len(response) < batch_size:
            print('All data fetched')
            raise StopIteration
        id_obj_start = id_obj_end


def load_data(conn, id_obj_start, batch_size):
    for response in fetch_all(id_obj_start, batch_size):
        buildings.add_from_arcgis(conn, response)

def run():
    conf = config.load()
    conn = db.connect(conf['db_path'])
    response = arcgis.fetch_row(1) # use this response to build tables from schema, discard the data
    buildings.init_from_arcgis(conn, response)
    last_id = buildings.get_last_id(conn, response.primary_key)
    load_data(conn, last_id, BATCH_SIZE)
    
    

if __name__ == '__main__':
    run()
