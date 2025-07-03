# Painel-de-Vagas
Repositório utilizado para subir a atividade prática da disciplina de padrões de projeto


Este projeto demonstra o uso do protocolo **MQTT** com o broker **Mosquitto** para simular um sistema de monitoramento de vagas de estacionamento, utilizando Python e Flask.

 Tecnologias Utilizadas

- Python 3.x  
- Flask  
- paho-mqtt  
- Mosquitto (via Docker)  
- Postman (para simulação das requisições)

---

A aplicação simula:

- Uma **API Flask** que publica mensagens MQTT (entrada/saída de veículos).
- Um **cliente MQTT** (monitor) que se inscreve em um tópico e atualiza em tempo real o número de vagas ocupadas.
- O **broker Mosquitto** gerencia a comunicação entre API e monitor.

---

Configurar o docker:

docker compose up -d

Crie um ambiente Virtual:

python -m venv venv
.\venv\Scripts\activate

Instalar Dependências:

pip install -r requirements.txt


Execute o monitor de vagas:

python monitor_vagas.py

Resultado esperado: Conectado ao broker MQTT!

Inicie em outro terminal o servidor Flask:

python app.py
A API estará disponível em http://127.0.0.1:5000

Teste de entrada e saída do veículo(postman):

POST http://localhost:5000/vaga

Corpo da requisição:

{
  "acao": "entrada"
}
ou
{
  "acao": "saida"
}

Resultado esperado no console do Postman:

{
    "message": "Evento 'entrada' publicado com sucesso!"
}

ou

{
    "message": "Evento 'saida' publicado com sucesso!"
}

Resultado esperado, no terminal do monitor:

Carro entrou. Vagas ocupadas: 3/10
ou
Carro saiu. Vagas ocupadas: 2/10






