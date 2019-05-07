#Script para publicação de dados

import paho.mqtt.client as paho
from random import randint
from time import sleep

##### Configurações #####
broker="1.1.1.1"         #IP (str)
port=1883                #Porta (int)
intervalo_publicacao=10  #Tempo em segundos (int)
usuario='xxxxx'          #Nome do usuário (str)
senha='xxxxx'            #Senha (str)

cliente_mqtt = paho.Client('python-mqtt')

def configura_mqtt():
    cliente_mqtt.username_pw_set(username=usuario,password=senha)
    cliente_mqtt.connect(broker,port)
    cliente_mqtt.loop_start()


def publica_dados():
    while True:
        temperatura = randint(20,40)
        cliente_mqtt.publish("infnet/laboratorio/temperatura",temperatura, qos=1, retain=True)
        print(f'Temperatura: {temperatura}')
        sleep(intervalo_publicacao)

def main():
    configura_mqtt()
    publica_dados()

main()

