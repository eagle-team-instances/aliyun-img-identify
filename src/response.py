from flask import jsonify


def success(data, msg):
    return jsonify({'code': 0, 'data': data, 'msg': msg})


def fail(msg, error={}):
    return jsonify({'code': -1, 'msg': msg, 'error': error, })
