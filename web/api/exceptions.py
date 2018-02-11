class HTTPException(Exception):
    def __init__(self, message, status_code, payload):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload


class HTTPMessage(object):
    MISSING_FILE_PART = ('Missing file part', '1001')
    NOT_EXTENSION_ALLOWED = ('Not extension allowed', '1002')
    FILE_IS_TOO_LARGE = ('File is too large', '1003')


class HTTPBadRequest(HTTPException):
    def __init__(self, message, payload=None):
        HTTPException.__init__(self, message, 400, payload)
        self.status_code = 400
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message[0]
        rv['code'] = self.message[1]
        return rv

class HTTPPayloadTooLarge(HTTPException):
    def __init__(self, message, payload=None):
        HTTPException.__init__(self, message, 413, payload)
        self.status_code = 413
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message[0]
        rv['code'] = self.message[1]
        return rv