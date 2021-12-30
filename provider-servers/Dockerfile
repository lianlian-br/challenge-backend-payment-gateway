FROM alpine:3.14

RUN apk add --update --no-cache python3 py3-pip make
EXPOSE 3001
EXPOSE 3002
EXPOSE 4001

WORKDIR /server
COPY ./ ./

RUN make install

CMD [ "make", "run" ]