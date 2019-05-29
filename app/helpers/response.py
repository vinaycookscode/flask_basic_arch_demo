from flask import json, Response


class ApiResponse(object):
    def __init__(self):
        pass

    @staticmethod
    def response(data, msg, status, http_code=400, mimetype='application/json', errors={}):
        return Response(json.dumps({'data': data, 'status': status, 'msg': msg, 'error': errors}),status=http_code,mimetype=mimetype)
