import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "estacionamento/vagas"

vagas_totais = 10 
vagas_ocupadas = 0

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT!")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Falha na conexão, código {rc}")

def on_message(client, userdata, msg):
    global vagas_ocupadas
    mensagem = msg.payload.decode() 

    if mensagem == "entrada":
        if vagas_ocupadas < vagas_totais:
            vagas_ocupadas += 1
            print(f"Carro entrou. Vagas ocupadas: {vagas_ocupadas}/{vagas_totais}")
        else:
            print("Estacionamento cheio! Nenhuma vaga disponível.")
    elif mensagem == "saida":
        if vagas_ocupadas > 0:
            vagas_ocupadas -= 1
            print(f"Carro saiu. Vagas ocupadas: {vagas_ocupadas}/{vagas_totais}")
        else:
            print("Estacionamento já está vazio.")
    else:
        print(f"Mensagem desconhecida recebida: {mensagem}")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()
