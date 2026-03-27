from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

@app.post('/pecas-camisas')
def criar_camisa():
    dados_camisa = request.json

    tamanhos_camisa= ['PP','P','M','G','GG']
    if dados_camisa.get('Tamanho') not in tamanhos_camisa:
        return jsonify({"mensagem": "Tamanho inválido!"}), 422
    
    if not dados_camisa.get('Doador'):
        return jsonify({"mensagem" : "Nome de Doador é necessário."}), 400

    if not dados_camisa.get('Peca')=="Camisa":
        return jsonify({"mensagem" : "Nomear peça como camisa é obrigatório."}), 400

    with open ('camisas.json', 'r') as f:
        camisas = json.load(f)

    camisas.append(dados_camisa)

    with open('camisas.json', 'w') as f:
        json.dump(camisas, f, indent=4)

    resposta = {
        "mensagem": "Camisa cadastrada com sucesso!"
        }

    return jsonify(resposta), 201

@app.post('/pecas-sapatos')
def criar_sapatos():
    dados_sapatos = request.json

    tamanhos_sapato=['34','35','36','37','38','39','40','41']
    if dados_sapatos.get ('Tamanho') not in tamanhos_sapato:
        return jsonify({"mensagem": "Tamanho é inválido!"}), 422

    if not dados_sapatos.get('Doador'):
        return jsonify({"mensagem" : "Nome de Doador é necessário."}), 400

    if not dados_sapatos.get('Peca')=="Sapatos":
        return jsonify({"mensagem" : "Nomear peça como sapato é obrigatório."}), 400

    with open ('sapatos.json', 'r') as f:
        sapatos = json.load(f)

    sapatos.append(dados_sapatos)

    with open('sapatos.json', 'w') as f:
        json.dump(sapatos, f, indent=4)

    resposta = {
        "mensagem": "Sapato cadastrado com sucesso!"
        }

    return jsonify(resposta), 201

@app.post('/pecas-agasalhos')
def criar_agasalhos():
    dados_agasalhos = request.json

    tamanhos_agasalho=['PP','P','M','G','GG']
    if not dados_agasalhos.get('Tamanho') not in tamanhos_agasalho:
        return jsonify({"mensagem": "Tamanho é inválido!"}), 422

    if not dados_agasalhos.get('Doador'):
        return jsonify({"mensagem" : "Nome de Doador é necessário."}), 400

    if not dados_agasalhos.get('Peca')=='Agasalho':
        return jsonify({"mensagem" : "Nomear peça como Agasalho é obrigatório."}), 400

    with open ('agasalhos.json', 'r') as f:
        agasalhos = json.load(f)

    agasalhos.append(dados_agasalhos)

    with open('agasalhos.json', 'w') as f:
        json.dump(agasalhos, f, indent=4)

    resposta = {
        "mensagem": "Agasalho cadastrado com sucesso!"
        }

    return jsonify(resposta), 201

@app.post('/pecas-calcas')
def criar_calcas():
    dados_calcas = request.json

    tamanho_calca=['34','35','36','37','38','39','40','41']
    if dados_calcas.get('Tamanho') not in tamanho_calca:
        return jsonify({"mensagem": "Tamanho é inválido!"}), 422

    if not dados_calcas.get('Doador'):
        return jsonify({"mensagem": "Nome do Doador é essencial."}), 400
    
    if not dados_calcas.get('Peca')=='Calça':
        return jsonify({"mensagem": "Nomear peça como calça é obrigatório."}), 400

    with open ('calcas.json', 'r') as f:
        calcas = json.load(f)

    calcas.append(dados_calcas)

    with open ('calcas.json', 'w') as f:
        json.dump(calcas, f, indent=4)

    resposta= {
        "mensagem": "Calça cadastrada com sucesso!"
    }

    return jsonify(resposta), 201

@app.get("/")
def home():
    return render_template("home.html")

@app.route("/pecas", methods=["GET"])
def pecas():
    return render_template("pecas.html")

@app.route("/pecas-camisas", methods=["GET"])
def page_camisas():
    with open ('camisas.json', 'r') as f:
        return jsonify(json.load(f))

@app.route("/pecas-calcas", methods=["GET"])
def page_calcas ():
    with open ('calcas.json', 'r') as f:
        return jsonify(json.load(f))

@app.route("/pecas-sapatos", methods=["GET"])
def page_sapatos():
    with open ('sapatos.json', 'r') as f:
        return jsonify(json.load(f))
    
@app.route("/pecas-agasalhos", methods=["GET"])
def page_agasalhos():
    with open ('agasalhos.json', 'r') as f:
        return jsonify(json.load(f))

@app.route("/pecas-tudo", methods=["GET"])
def page_tudo():
    try:
        with open("camisas.json", "r", encoding="utf-8") as f:
            camisas = json.load(f)
        with open("calcas.json", "r", encoding="utf-8") as f:
            calcas = json.load(f) 

        estoque_total = {
            "camisas": camisas,
            "calcas": calcas
        }
        return jsonify(estoque_total) 

    except FileNotFoundError as e:
        return jsonify({"erro": f"Arquivo nao encontrado: {e.filename}"}), 404



if __name__ == "__main__":
    app.run(debug=True)

"""
Rota                    Método          Descrição
/pecas                  GET             Filtro de pesquisa
/pecas-camisas          GET             Listagem das Camisas
/pecas-calcas           GET             Listagem das Calças
/pecas-sapatos          GET             Listagem dos Sapatos
/pecas-agasalhos        GET             Listagem dos Agasalhos
/pecas-tudo             GET             Listagem de todas as roupas


/pecas-camisas          POST            Cadastro Camisa
/pecas-calcas           POST            Cadastro Calça
/pecas-sapatos          POST            Cadastro Sapato
/pecas-agasalhos        POST            Cadastro Agasalho
"""