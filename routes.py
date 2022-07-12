# https://www.youtube.com/watch?v=RIoC1YOY4yc
from flask import Flask, request
from main import insertUsuario

app = Flask("apiFlask")

@app.route("/olamundo", methods=["GET"]) 
def olaMundo():
    return {"olaMundo": "Ola mundo api"}

@app.route("/cadastra/usuario", methods=["POST"]) 
def cadastrarUsuario():

    body = request.get_json()

    # verificar se todos os dados foram enviados
    if("nome" not in body):
        return gerarResponse(400, "O parametro `nome` é obrigatório e não foi enviado.")
    if("email" not in body):
        return gerarResponse(400, "O parametro `email` é obrigatório e não foi enviado.")
    if("senha" not in body):
        return gerarResponse(400, "O parametro `senha` é obrigatoório e não foi enviado.")

    usuario = insertUsuario(body["nome"], body["email"], body["senha"])
    return gerarResponse(200, "Usuário criado com sucesso!", "user", usuario)

def gerarResponse(status, mensagem, nome_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_conteudo and conteudo):
        response[nome_conteudo] = conteudo

    return response

app.run()