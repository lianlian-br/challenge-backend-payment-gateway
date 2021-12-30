# Programming Challenge Lian Lian Brasil

In this challenge, you will create an application that expose a RESTful API focused in payments. With this challenge, we wish to observe both your design decisions and code, so we will, in most cases, only define some requirements and leave the design decisions to you!

We will provide a project that mocks answers and will serve as a payment provider, with more details in their [README](./provider-servers/README.md).

Also, we recommend you read the entire spec before starting your project.

# Endpoints

## Login

Should have one endpoint that allows an client to authenticate.

[ ] Should follow OAuth 2.0 [client credentials grant type](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/) format. \
[ ] Should return the access_token as a JWT token.

There is no need to implement every detail of the grant type spec, an endpoint that receives the id and secret, check for their validity and returns the token is enough.

## Payment Creation

Should have one or multiple endpoints, which allow creation of boleto or credit card payments.

### Boleto

[ ] Should receive at least:
- JWT Bearer Token
- Payment Amount
- Buyer:
    - CPF
    - Name

[ ] Should answer at least:
- Transaction Id
- Transaction Status
- Payment Amount
- Provider
- Barcode Number
- Buyer:
    - CPF
    - Name

[ ] Should, usually, select a new Boleto provider(**MeuBoleto** or **Boletaria**) to execute the transaction every request. \
[ ] Should allow locking provider every request, so every boleto is provided by the same provider, via an application parameter. In case no parameter is given, both should be considered, as defined in the previous requirement. \
[ ] Should deny any transaction above an amount, parameterized in the application.

### Credit Card

[ ] Should receive at least:
- JWT Bearer Token
- Payment Amount
- Buyer:
    - CPF
    - Name
- Credit Card:
    - Credit Card Number
    - Cardholder Name
    - Expiration Date
    - CVV

[ ] Should answer at least:
- Transaction Id
- Transaction Status
- Payment Amount
- Provider
- Buyer:
    - CPF
    - Name
- Credit Card:
    - Credit Card Number First 6 Digits
    - Credit Card Number Last 4 Digits
    - Cardholder Name
    - Expiration Date

[ ] Should execute the transaction every request using the credit card provider **EzCredit**. \
[ ] Should deny any transaction above an amount, parameterized in the application.

## Payment Query

This feature should allow the client to query two types of payment, boleto or credit card.

### Query By Id

Should have one or multiple endpoints, which allow query of boleto or credit card payments.
[ ] Should receive at least:
- JWT Bearer Token
- Transaction Id

[ ] Should answer all saved information for the payment type. \
[ ] Should return transaction only if executed by the client of the JWT Bearer Token.

### Query Between Dates

Should have one or multiple endpoints, which allow query of boleto or credit card payments between two dates.

[ ] Should receive at least:
- JWT Bearer Token
- Start Date (Optional)
- End Date (Optional)
- Page Number (Optional)
- Page Size (Optional)

[ ] Should answer all saved information for the payment type. \
[ ] Should answer in a paginated response. \
[ ] Should consider start date and end date as the start and end of times, respectively, in case they are null. \
[ ] Should have default page number as the first page. \
[ ] Should have default page size parameterized in the application. \
[ ] Should return only transactions executed by the client of the JWT Bearer Token.

# Extra Clarifications

## Payment Providers

- Boleto: MeuBoleto, Boletaria.
- Credit Card: EzCredit.

## Payments Status

- GENERATED - When a Boleto has been generated but not paid yet.
- DENIED - When a transaction is denied because of any detail.
- FAILED - When an error with a third party occur.
- PAID - When a transaction has been marked as paid.

Those status are mandatory, but in case you need any other status, you can feel free to create them.

## Message Format

All endpoints shall only accept and answer JSON, including error messages.

## Errors

Error messages should follow the following format:

```json
{ 
    "code": "error.code",
    "message": "This error happens because of stuff."
}
```

Should have one for multiple error codes for the following special cases and return then when needed:
- Path Not Found
- Unauthorized Access to Authenticated Endpoints
- Missing Fields
- Transaction Not Found
- Third Party Failure
- Any other error you may think relevant
- Any other unexpected error

## Setup

At startup, the application should be initialized with some data, so some checks can be easier. Some of the data is:
[ ] At least two different client credentials for different clients. \
[ ] At least one transaction per day in a period of at least two months in the past. \
[ ] At least one transaction for each client.

This can be done in a hardcoded manner, but we highly suggest the setup is done via a file read at startup by your application.

## Application Requirements

[ ] Don't save credit card information like complete card number or CVV. \
[ ] Maximum transaction amount for Boleto and Credit Card should allow for different values, if needed. \
[ ] The default format for dates will be yyyy-MM-dd. \
[ ] The default format for datetimes will be yyyy-mm-dd'T'hh:mm:ssZ. \
[ ] All dates should be represented considering we are at GMT-3(America/Sao_Paulo). Datetimes *can* be at other timezones. \
[ ] Amounts should be considered only to have exactly two decimal places. \
[ ] Client Secret should be persisted as a hash and not as plain text. \
[ ] In case of HTTP request fails, the information shall be logged to the console.

## Extra Requirements

[ ] Delivered as a public git repository with source code. \
[ ] Written using Kotlin or Java. \
[ ] Gradle as build tool. \
[ ] Spring Boot. \
[ ] Unit Tests using JUnit. \
[ ] Integrated Tests. \
[ ] A README explaining how to run your application.

## Tips

- We recommend using an in-memory database, such as HSQLDB. In case it is not possible, or is harder, you can create a docker compose that starts the application and database.
- You can use as many extra libraries as needed for parsing(Jackson, Gson, Moshi, etc), HTTP Clients(Retrofit, Feign, etc), test assertions(Hamcrest, AssertJ, etc) and so on. Also I should say there is no need to using any of these libraries.
- There is no need to covering all your code with tests, just some basic unit tests and one or other integration tests should be enough.
- You can use either the Web or Webflux Spring starters.
- For startup setup, the [EventListener](https://www.baeldung.com/running-setup-logic-on-startup-in-spring#3-an-applicationlistener) annotation can help you.
- You can separate the persisted data in as many or as few tables or collections as you want.
- Using [spring-dotenv](https://github.com/paulschwarz/spring-dotenv) can help a lot in configurating the environment.
- The provider choice at boleto generation can be done randomly, or in an alternating way, whatever is easier for you.
- You can receive transactions amount with more or less than two decimal places, but the persisted and return value should always have two decimal places.
- You are not required to follow the same variable names that we used.
