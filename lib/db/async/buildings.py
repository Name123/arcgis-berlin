import aiosqlite

async def cnt_by_zip_code(db_path, zip_code_str=None):
     async with aiosqlite.connect(db_path) as conn:
          sql = """
             SELECT plz, COUNT(*) FROM buildings 
          """ + ((" WHERE plz IN (%s)" % zip_code_str) if zip_code_str else "") + """
          GROUP BY plz"""
          cursor = await conn.execute(sql)
          rows = await cursor.fetchall()
          await cursor.close()
          return { x[0] : x[1] for x in rows }


async def cnt_by_add_year(db_path, zip_code_str=None):
     async with aiosqlite.connect(db_path) as conn:
          sql = """
             SELECT strftime('%Y', str_datum) as year, COUNT(*) FROM buildings 
          """ + ((" WHERE plz IN (%s)" % zip_code_str) if zip_code_str else "") + """
          GROUP BY year
          ORDER BY year
          """
          cursor = await conn.execute(sql)
          rows = await cursor.fetchall()
          await cursor.close()
          return rows
