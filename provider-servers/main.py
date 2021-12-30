from providers import boletaria, ez_credit, meu_boleto
from threading import Thread

if __name__ == "__main__":

    t1 = Thread(target = lambda: boletaria.run(port=3001))
    t2 = Thread(target = lambda: meu_boleto.run(port=3002))
    t3 = Thread(target = lambda: ez_credit.run(port=4001))

    t1.start()
    t2.start()
    t3.start()
