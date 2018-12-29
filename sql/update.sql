-- index for searching by zip code (Postleitzahl)

CREATE INDEX IF NOT EXISTS idx_plz ON buildings(plz);

-- index for searching by the record add year 

CREATE INDEX IF NOT EXISTS idx_year on buildings(strftime('%Y', str_datum));
