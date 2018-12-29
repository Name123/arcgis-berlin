ARCGIS_URL_PREF = 'https://services2.arcgis.com/jUpNdisbWqRpMo35/arcgis/rest/services/Berlin_Adressen/FeatureServer/0/query?outFields=*&outSR=4326&f=json'
ARCGIS_URL_KEY_FIELD = 'objectid'

LAT_FIELD = 'LAT'
LONG_FIELD = 'LONG'

TYPES_TO_SQL = {
    'esriFieldTypeInteger' : 'Integer',
    'esriFieldTypeString' : 'Text',
    'esriFieldTypeDouble' : 'Float',
    'esriFieldTypeOID' : 'Integer Primary key'
}
