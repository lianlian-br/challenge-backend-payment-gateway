from flask import Flask, jsonify, abort, request, make_response
import random

__app = Flask("Boletaria")

@__app.route('/boleto/new', methods=['POST'])
def generate():
    body = request.json

    if body is None:
        return __error("Why?", 400)

    amount = body.get("amount")
    consumer = body.get("consumer")

    if consumer is None:
        return __error("Should contain consumer field", 400)

    name = consumer.get("name")
    cpf = consumer.get("documentNumber")
    doc_type = consumer.get("documentType")

    if (doc_type != "CPF"):
        return __error("Invalid consumer->documentType", 400)

    if amount is None or name is None or cpf is None:
        return __error("Should contain consumer->documentNumber, consumer->name and amount fields", 400)
    
    if "Error" in name:
        return __error("¯\_(ツ)_/¯", 500)

    min = 10 ** 30
    max = min * 10
    padding = random.randrange(min, max)

    return make_response(jsonify({
      "barCode": f'{cpf}{padding}'
    }), 201)

def run(port):
    __app.run(port = port)

def __error(message, status):
    return make_response(jsonify({
      "error_message": message
    }), status)