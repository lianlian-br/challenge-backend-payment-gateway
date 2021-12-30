from flask import Flask, jsonify, abort, request, make_response

__app = Flask("EzCredit")

@__app.route('/credit-card', methods=['POST'])
def generate():
    body = request.json

    amount = body.get("amount")

    if amount is None:
        return __error_not_nullable("amount")

    customer = body.get("customer")

    if customer is None:
        return __error_not_nullable("customer")

    name = customer.get("name")

    if name is None:
        return __error_not_nullable("customer.name")

    cpf = customer.get("cpf")

    if cpf is None:
        return __error_not_nullable("customer.cpf")

    card_data = body.get("cardData")

    if card_data is None:
        return __error_not_nullable("cardData")

    card_no = card_data.get("number")

    if card_no is None:
        return __error_not_nullable("card_no")

    cvv = card_data.get("cvv")

    if cvv is None:
        return __error_not_nullable("cvv")

    cardholder_name = card_data.get("cardholderName")

    if cardholder_name is None:
        return __error_not_nullable("cardholderName")

    expiration_date = card_data.get("expirationDate")

    if expiration_date is None:
        return __error_not_nullable("expirationDate")
    
    if "Error" in name:
        return __error("¯\_(ツ)_/¯", 500)

    return make_response(jsonify({
      "status" : "SUCCESS"
    }), 200)

def run(port):
    __app.run(port = port)

def __error_not_nullable(field):
    return __error(f'Not Nullable: "{field}"', 400)

def __error(message, status):
    return make_response(jsonify({
      "error" : {
        "message": message
      }
    }), status)