from flask import Response, jsonify


def unauthorized() :
    output = {"error":
              {"msg": "401 error: The email or password is invalid."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 401
    return resp


def forbidden() :
    output = {"error":
              {"msg": "403 error: unauthorized."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 403
    return resp


def invalid_route():
    output = {"error":
              {"msg": "404 error: NOT FOUND."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 404
    return resp