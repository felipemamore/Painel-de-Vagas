from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "estacionamento/vagas"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

@app.route('/vaga', methods=['POST'])
def atualizar_vaga():
    data = request.json
    if not data or 'acao' not in data:
        return jsonify({"error": "Envie JSON com a chave 'acao' (entrada ou saida)"}), 400

    acao = data['acao'].lower()
    if acao not in ['entrada', 'saida']:
        return jsonify({"error": "Ação deve ser 'entrada' ou 'saida'"}), 400

    client.publish(MQTT_TOPIC, acao)
    return jsonify({"message": f"Evento '{acao}' publicado com sucesso!"}), 200

if __name__ == '__main__':
    app.run(debug=True)