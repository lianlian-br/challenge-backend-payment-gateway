# Provider Servers

This Project runs the servers that represent the following providers:

## Boletaria

**Port**: 3001

### Endpoints

**POST** /boleto/new

Example Body:
```
{
    "amount": 15.45,
    "consumer": {
        "documentType": "CPF",
        "documentNumber": "69159467053",
        "name": "Mr. Lian Lian"
    }
}
```

Example Reponse:
```
{
    "barCode": "691594670531756652025158734240146475291357"
}
```

## MeuBoleto

**Port**: 3002

### Endpoints

**POST** /generate

Example Body:
```
{
    "boleto_value": 15,
    "buyer_cpf": "69159467053",
    "buyer_name": "Mr. Lian Lian"
}
```

Example Reponse:
```
{
    "bar_code": "691594670535077755454085284952927795888224",
    "status": "SUCCESS"
}
```

## EzCredit

**Port**: 4001

### Endpoints

**POST** /credit-card

Example Body:
```{
    "amount": 15,
    "customer": {
        "cpf": "69159467053",
        "name": "Mr. Lian Lian"
    },
    "cardData": {
        "cvv": "123",
        "cardholderName": "Lian Lian de Araujo",
        "expirationDate": "2029-01-01",
        "number": "0123456789012345"
    }
}
```

Example Reponse:
```
{
    "status": "SUCCESS"
}
```

# Running

## Using Docker

### Requirements
[ ] Docker \

### Steps

First, you need to build the image, from this folder, run:

```
docker build . -t server-providers
```

And then, to run the servers, use the following command:

```
docker run -it --network=host -p 3001:3001 -p 3002:3002 -p 4001:4001 server-providers
```

## Using Make

### Requirements
[ ] Python 3 \
[ ] Python 3 Pip \
[ ] Make

### Steps

Just run `make run`

## Using Python

### Requirements
[ ] Python 3 \
[ ] Python 3 Pip

### Steps

First, you need to update your dependencies, from this folder, run:

```
python3 -m pip install --upgrade -r requirements.txt
```

And then, to run the servers, use the following command:

```
python3 main.py
```

# Causing Internal Server Errors

Any of the providers, when receiving a name containing the word `Error` will cause a 500 error, which can be used to easily test your error treatments.