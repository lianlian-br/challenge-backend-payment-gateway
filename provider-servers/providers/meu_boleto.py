from flask import Flask, jsonify, abort, request, make_response
import random

__app = Flask("MeuBoleto")

@__app.route('/generate', methods=['PUT'])
def generate():
    body = request.json

    amount = body.get("boleto_value")
    name = body.get("buyer_name")
    cpf = body.get("buyer_cpf")

    if amount is None or name is None or cpf is None:
        return __error("params.some_missing", "'boleto_value', 'buyer_cpf' and 'buyer_name' should be provided", 400)
    
    if "Error" in name:
        return __error("???", "system has broken!!!", 500)

    min = 10 ** 30
    max = min * 10
    padding = random.randrange(min, max)

    return make_response(jsonify({
      "status" : "SUCCESS",
      "bar_code": f'{cpf}{padding}'
    }), 201)

def run(port):
    __app.run(port = port)

def __error(code, message, status):
    return make_response(jsonify({
      "error" : {
        "message": message,
        "code": code
      }
    }), status)