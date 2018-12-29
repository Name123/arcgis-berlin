import tornado

import db.async.buildings as buildings

from .misc import fmt_response
from .misc import ERROR_WRONG_PLZ

class BuildingsByZipCodeHandler(tornado.web.RequestHandler):
    def initialize(self, conf):
        self.conf = conf

    async def get(self, zip_code_str):
        """
            No need to validate the argument - already done by tornado in routing regexp.
            Pass the whole zip code string to SQL IN operator instead.
        """
        res = await buildings.cnt_by_zip_code(self.conf['db_path'], zip_code_str)
        self.write(fmt_response(res, error=not res and ERROR_WRONG_PLZ))


class BuildingsByAddYearHandler(tornado.web.RequestHandler):
    def initialize(self, conf):
        self.conf = conf
        
    async def get(self, zip_code_str):
        res = await buildings.cnt_by_add_year(self.conf['db_path'], zip_code_str)
        self.write(fmt_response(res, error=not res and ERROR_WRONG_PLZ))
