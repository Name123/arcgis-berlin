Extract data on Berlin buildings from ArcGIS database, provide some API 
for data retrieval.


# ----- Deployment: ------
sudo apt-get install python3 sqlite3 libsqlite3-dev 

cd arcgis-berlin

pip3 install -r requirements.txt

# ----- Import data: ------

python3 tools/import.py

sqlite3 data/arcgis.db < sql/update.sql

# ----- Run app: ------

python3 app.py

# ----- Run tests: ------
python3 tests/test_api.py

# ----- Access API: ------

curl http://localhost:8888/buildings/by_zip_code/[zip_code_1, ..., zip_code_n]

curl http://localhost:8888/buildings/by_year/[zip_code_1, ..., zip_code_n]
