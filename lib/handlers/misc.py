STATUS_OK = 'ok'
STATUS_ERROR = 'error'

ERROR_WRONG_PLZ = 'no_such_zip_code'

def fmt_response(result, error=None):
    return {
        'status' : STATUS_OK,
        'result' : result
    } if not error else {
        'status' : STATUS_ERROR,
        'error' : error
    }
