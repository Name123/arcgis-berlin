
from .const import TYPES_TO_SQL, LAT_FIELD, LONG_FIELD

from collections import OrderedDict

class EmptyResponse(Exception):
    def __str__(self):
        return "Empty response from ArgGIS server"

class ArcGISResponse:
    def __init__(self, json):
        self._json = json


    @property
    def features(self):
        return self._json['features']

    @property
    def fields(self):
        return self._json['fields']

    def empty(self):
        return not len(self)

    def __len__(self):
        return len(self.features)

    @property
    def primary_key(self):
        return self._json['uniqueIdField']['name']

    @staticmethod
    def name(field):
        return field['name']

    @staticmethod
    def coords(field):
        return field['geometry']['points'][0]

    def __getitem__(self, n):
        return self.features[n]


    def keys(self):
        if self.empty():
            raise EmptyResponse
        return sorted(self[0]['attributes'].keys()) + [ LAT_FIELD, LONG_FIELD ]
        

    def __iter__(self):
        return (OrderedDict(
            sorted(list(f['attributes'].items())) + 
                [(LAT_FIELD, self.__class__.coords(f)[0]),
                (LONG_FIELD, self.__class__.coords(f)[1])
            ]) for f in self.features
        )
        

    @staticmethod
    def sql_type(field):
        return TYPES_TO_SQL[field['type']]
        
    
