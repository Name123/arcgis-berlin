from arcgis.response import ArcGISResponse
from arcgis.const import LAT_FIELD, LONG_FIELD


def init_from_arcgis(conn, a_response):
    fields_str = ','.join(['%s %s' % (ArcGISResponse.name(f), ArcGISResponse.sql_type(f)) for f in a_response.fields ] + [
        '%s Float' % LAT_FIELD, '%s Float' % LONG_FIELD
    ])
    sql = """
        CREATE TABLE IF NOT EXISTS buildings (%s)
    """ % fields_str
    conn.execute(sql)
    
def get_last_id(conn, primary_key):
    sql = "SELECT %s FROM buildings ORDER BY %s DESC LIMIT 1" % (
        primary_key, primary_key
    )
    r = conn.execute(sql).fetchone()
    return r[0] if r else 0

def add_from_arcgis(conn, response):
    if response.empty():
        print("No data in response!")
        return
    keys_str = ','.join(response.keys())
    placeholders_str = ','.join(map(lambda _ : '?', response.keys()))
    values = [ list(f.values()) for f in response ]
    with conn:
        sql = """
        INSERT INTO buildings(%s) VALUES (%s)
        """ % (keys_str, placeholders_str)
        conn.executemany(sql, values)
        
                     
    
    
