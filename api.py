from flask import Flask, request, jsonify, render_template
import json

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def carregar (arquivo):
    with open (arquivo, 'r') as f:
        return json.load(f)

    
def salvar (arquivo, object):
    with open(arquivo, 'w') as f:
        json.dump(object, f, indent=4)

@app.get('/pecas-camisas/<int:id>') # localhost/pecas-camisas/1
def get_camisa_pr_id(id):
    camisas = carregar('camisas.json')

    for camisa in camisas:
        if camisa.get ('id') == id:
            return jsonify (camisa), 200
        
    return jsonify({"mensagem": "Camisa não existe"}), 404

@app.get('/pecas-calcas/<int:id>') 
def get_calcas_pr_id(id):
    calcas = carregar('calcas.json')

    for calca in calcas:
        if calca.get ('id') == id:
            return jsonify (calca), 200
        
    return jsonify({"mensagem": "Calça não existe"}), 404

@app.get('/pecas-sapatos/<int:id>')
def get_sapatos_pr_id(id):
    sapatos = carregar('sapatos.json')

    for sapato in sapatos:
        if sapato.get ('id') == id:
            return jsonify (sapato), 200
        
    return jsonify({"mensagem": "Sapatos não existe"}), 404

@app.get('/pecas-agasalhos/<int:id>')
def get_agasalhos_pr_id(id):
    agasalhos = carregar('agasalhos.json')

    for agasalho in agasalhos:
        if agasalho.get ('id') == id:
            return jsonify (agasalho), 200
        
    return jsonify({"mensagem": "Agasalho não existe"}), 404
    
@app.put('/pecas-camisas/<int:id>')
def atualizar_camisa(id):
    camisas = carregar('camisas.json')
    dados_camisas = request.json

    #validações

    for camisa in camisas:
        if camisa.get ("id")== id:
            camisa.update(dados_camisas)
            salvar("camisas.json", camisas)
            return jsonify({"mensagem":"ok"}), 200
    return jsonify({"mensagem":"não encontrado"}),404

@app.delete('/pecas-camisas/<int:id>')
def deletar_camisa(id):
    camisas = carregar("camisas.json")

    for camisa in camisas:
        if camisa.get('id')==id:
            camisas.remove(camisa)
            salvar("camisas.json", camisas)
            return jsonify({"mensagem":"Deletado"}), 200
    return jsonify ({"mensagem":"Não encontrado"}), 404
    
@app.put('/pecas-calcas/<int:id>')
def atualizar_calcas(id):
    calcas = carregar('calcas.json')
    dados_calcas = request.json
    
    for calca in calcas:
        if calca.get("id") == id:
            calca.update(dados_calcas)
            salvar("calcas.json", calcas)
            return jsonify({"mensagem":"Ok"}), 200
    return jsonify({"mensagem":"Não encontrado"}), 404
    
@app.delete('/pecas-calcas/<int:id>')
def deletar_calcas(id):
    calcas = carregar('calcas.json')
    for calca in calcas:
        if calca.get("id")==id:
            calcas.remove(calca)
            salvar("calcas.json", calcas)
            return jsonify({"mensagem":"deletado!"}),200
    return jsonify({"mensagem":"Não encontrado!"}),404


@app.put('/pecas-sapatos/<int:id>')
def atualizar_sapatos(id):
    sapatos = carregar('sapatos.json')
    dados_sapatos = request.json
    
    for sapato in sapatos:
        if sapato.get("id") == id:
            sapato.update(dados_sapatos)
            salvar("sapatos.json", sapatos)
            return jsonify({"mensagem":"Ok"}), 200
    return jsonify({"mensagem":"Não encontrado"}), 404
    
@app.delete('/pecas-sapatos/<int:id>')
def deletar_sapatos(id):
    sapatos = carregar('sapatos.json')
    for sapato in sapatos:
        if sapato.get("id")==id:
            sapatos.remove(sapato)
            salvar("sapatos.json", sapatos)
            return jsonify({"mensagem":"deletado!"}),200
    return jsonify({"mensagem":"Não encontrado!"}),404

@app.put('/pecas-agasalhos/<int:id>')
def atualizar_agasalhos(id):
    agasalhos = carregar('agasalhos.json')
    dados_agasalhos = request.json
    
    for agasalho in agasalhos:
        if agasalho.get("id") == id:
            agasalho.update(dados_agasalhos)
            salvar("agasalhos.json", agasalhos)
            return jsonify({"mensagem":"Ok"}), 200
    return jsonify({"mensagem":"Não encontrado"}), 404
    
@app.delete('/pecas-agasalhos/<int:id>')
def deletar_agasalhos(id):
    agasalhos = carregar('agasalhos.json')
    for agasalho in agasalhos:
        if agasalho.get("id")==id:
            agasalhos.remove(agasalho)
            salvar("agasalhos.json", agasalhos)
            return jsonify({"mensagem":"deletado!"}),204
    return jsonify({"mensagem":"Não encontrado!"}),404

    
@app.post('/pecas-camisas')
def criar_camisa():
    dados_camisa = request.json


    tamanhos_camisa= ['PP','P','M','G','GG']
    if dados_camisa.get('tamanho') not in tamanhos_camisa:
        return jsonify({"mensagem": "Tamanho inválido!"}), 422
    
    if not dados_camisa.get('doador'):
        return jsonify({"mensagem" : "Nome de Doador é necessário."}), 400

    if dados_camisa.get('cor') not in dados_camisa:
        return jsonify({"mensagem": "Cor inválido!"}), 422

    if dados_camisa.get('sexo') not in dados_camisa:
        return jsonify({"mensagem": "Sexo inválido!"}), 422

    if dados_camisa.get('qualidade') not in dados_camisa:
        return jsonify({"mensagem": "Qualidade inválida!"}), 422

    if not dados_camisa.get('peca')=="Camisa":
        return jsonify({"mensagem" : "Nomear peça como camisa é obrigatório."}), 422

    with open ('camisas.json', 'r') as f:
        camisas = json.load(f)

    if dados_camisa is None:
        return jsonify({"mensagem": "Campo Obrigatório"}),400

    if not isinstance(dados_camisas.get('peca'), str):
        return jsonify({"erro": "Campo 'Peca' é obrigatório ser nome."}),422

    if not isinstance(dados_camisas.get('doador'), str):
        return jsonify({"erro": "Campo 'Doador' é obrigatório ser nome."}),422

    if not isinstance(dados_camisas.get('tamanho'), str):
        return jsonify({"erro": "Campo 'Tamanho' é obrigatório ser nome."}),422

    if not isinstance(dados_camisas.get('sexo'), str):
        return jsonify({'erro': "Campo 'Sexo' é obrigatório ser nome"}), 422

    if not isinstance(dados_camisas.get('marca'), str):
        return jsonify({'erro': "Campo 'Marca' é obrigatório ser nome"}), 422
    
    if not isinstance(dados_camisas.get('cor'), str):
        return jsonify({"erro": "Campo 'Cor' é obrigatório ser nome"}),422


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

    tamanhos_sapato=["34", "35", "36", "37", "38", "39", "40", "41"]

    if dados_sapatos.get('tamanho') not in tamanhos_sapato:
        return jsonify({"mensagem" : "Tamanho inválido!"}), 422

    if dados_sapatos.get('cor') not in dados_sapatos:
        return jsonify({"mensagem": "Cor inválido!"}), 422

    if dados_sapatos.get('sexo') not in dados_sapatos:
        return jsonify({"mensagem": "Sexo inválido!"}), 422

    if dados_sapatos.get('qualidade') not in dados_sapatos:
        return jsonify({"mensagem": "Qualidade inválida!"}), 422

    if not dados_sapatos.get('doador'):
        return jsonify({"mensagem" : "Nome de Doador é necessário."}), 400

    if not dados_sapatos.get('peca')=="Sapato":
        return jsonify({"mensagem" : "Nomear peça como sapato é obrigatório."}), 400

    with open ('sapatos.json', 'r') as f:
        sapatos = json.load(f)

    if dados_sapatos is None:
        return jsoinfy({"mensagem": "Campo Obrigatório!"}), 400

    if not isinstance(dados_sapatos.get('peca'), str):
        return jsonify({"erro": "Campo 'Peca' é obrigatório ser nome."}),422

    if not isinstance(dados_sapatos.get('doador'), str):
        return jsonify({"erro": "Campo 'Doador' é obrigatório ser nome."}),422

    if not isinstance(dados_sapatos.get('tamanho'), str):
        return jsonify({"mensagem": "Tamanho é inválido!"}), 422

    if not isinstance(dados_sapatos.get('sexo'), str):
        return jsonify({'erro': "Campo 'Sexo' é obrigatório ser nome"}), 422

    if not isinstance(dados_sapatos.get('marca'), str):
        return jsonify({'erro': "Campo 'Marca' é obrigatório ser nome"}), 422

    if not isinstance(dados_sapatos.get('cor'), str):
        return jsonify({"erro": "Campo 'Cor' é obrigatório ser nome"}),422



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
    if not dados_agasalhos.get('tamanho') not in tamanhos_agasalho:
        return jsonify({"mensagem": "Tamanho é inválido!"}), 422

    if not dados_agasalhos.get('doador'):
        return jsonify({"mensagem" : "Nome de Doador é necessário."}), 400

    if dados_agasalhos.get('cor') not in dados_agasalhos:
        return jsonify({"mensagem": "Cor inválido!"}), 422

    if dados_agasalhos.get('sexo') not in dados_agasalhos:
        return jsonify({"mensagem": "Sexo inválido!"}), 422

    if dados_agasalhos.get('qualidade') not in dados_agasalhos:
        return jsonify({"mensagem": "Qualidade inválida!"}), 422

    if not dados_agasalhos.get('peca')=='Agasalho':
        return jsonify({"mensagem" : "Nomear peça como Agasalho é obrigatório."}), 400

    if dados_agasalhos is None:
        return jsonify({"mensagem": "Campo Obrigatório"}),400

    if not isinstance(dados_agasalhos.get('peca'), str):
        return jsonify({"erro": "Campo 'Peca' é obrigatório ser nome."}),422

    if not isinstance(dados_agasalhos.get('doador'), str):
        return jsonify({"erro": "Campo 'Doador' é obrigatório ser nome."}),422

    if not isinstance(dados_agasalhos.get('tamanho'), str):
        return jsonify({"erro": "Campo 'Tamanho' é obrigatório ser nome."}),422

    if not isinstance(dados_agasalhos.get('sexo'), str):
        return jsonify({'erro': "Campo 'Sexo' é obrigatório ser nome"}), 422

    if not isinstance(dados_agasalhos.get('marca'), str):
        return jsonify({'erro': "Campo 'Marca' é obrigatório ser nome"}), 422

    if not isinstance(dados_agasalhos.get('cor'), str):
        return jsonify({"erro": "Campo 'Cor' é obrigatório ser nome"}),422


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

    tamanho_calca=["30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41"]

    if dados_calcas is None:
        return jsonify({"mensagem": "Campo Obrigatório"}),400

    if dados_calcas.get('tamanho') not in dados_calcas:
        return jsonify({"mensagem": "Tamanho inválido!"}), 422

    if dados_calcas.get('cor') not in dados_calcas:
        return jsonify({"mensagem": "Cor inválido!"}), 422

    if dados_calcas.get('sexo') not in dados_calcas:
        return jsonify({"mensagem": "Sexo inválido!"}), 422

    if dados_calcas.get('qualidade') not in dados_calcas:
        return jsonify({"mensagem": "Qualidade inválida!"}), 422

    if not dados_calcas.get('doador'):
        return jsonify({"mensagem": "Nome do Doador é essencial."}), 400
    
    if not dados_calcas.get('peca')=='Calça':
        return jsonify({"mensagem": "Nomear peça como calça é obrigatório."}), 400

    if not isinstance(dados_calcas.get('peca'), str):
        return jsonify({"erro": "Campo 'Peca' é obrigatório ser nome."}),422

    if not isinstance(dados_calcas.get('doador'), str):
        return jsonify({"erro": "Campo 'Doador' é obrigatório ser nome."}),422

    if not isinstance(dados_calcas.get('tamanho'), str):
        return jsonify({'erro': "Campo 'Tamanho' é obrigatório ser número"}),422

    if not isinstance(dados_calcas.get('sexo'), str):
        return jsonify({'erro': "Campo 'Sexo' é obrigatório ser nome"}), 422

    if not isinstance(dados_calcas.get('marca'), str):
        return jsonify({'erro': "Campo 'Marca' é obrigatório ser nome"}), 422



    if not isinstance(dados_calcas.get('cor'), str):
        return jsonify({"erro": "Campo 'Cor' é obrigatório ser nome"}), 422

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
    camisas = carregar('camisas.json')

    cor = request.args.get('cor') #https://.../pecas-camisas?cor...
    sexo = request.args.get('sexo')
    tamanho = request.args.get ('tamanho')
    qualidade = request.args.get ('qualidade')
    marca = request.args.get ('marca')

    resultado=[]
    status=404

    for camisa in camisas:
        if cor and camisa.get('cor').lower() != cor.lower():
            continue
        if sexo and camisa.get('sexo').lower() != sexo.lower():
            continue
        if qualidade and camisa.get('qualidade').lower() != qualidade.lower():
            continue
        if marca and camisa.get('marca').lower() != marca.lower():
            continue
        if tamanho and camisa.get('tamanho').lower() != tamanho.lower():
            continue
        
        
        resultado.append(camisa)
        status=200

    return jsonify(resultado), status



@app.route("/pecas-calcas", methods=["GET"])
def page_calcas ():
    calcas = carregar('calcas.json')

    cor = request.args.get('cor') #https://.../pecas-calcas?cor...
    sexo = request.args.get('sexo')
    tamanho = request.args.get ('tamanho')
    qualidade = request.args.get ('qualidade')
    marca = request.args.get ('marca')

    resultado=[]
    status=404

    for calca in calcas:
        if cor and calca.get('cor').lower() != cor.lower():
            continue
        if sexo and calca.get('sexo').lower() != sexo.lower():
            continue
        if qualidade and calca.get('qualidade').lower() != qualidade.lower():
            continue
        if marca and calca.get('marca').lower() != marca.lower():
            continue
        if tamanho and calca.get('tamanho').lower() != tamanho.lower():
            continue
        
        resultado.append(calca)
        status=200

    return jsonify(resultado), status

@app.route("/pecas-sapatos", methods=["GET"])
def page_sapatos():
    sapatos = carregar('sapatos.json')

    cor = request.args.get('cor') #https://.../pecas-camisas?cor...
    sexo = request.args.get('sexo')
    tamanho = request.args.get ('tamanho')
    qualidade = request.args.get ('qualidade')
    marca = request.args.get ('marca')

    resultado=[]
    status=404

    for sapato in sapatos:
        if cor and sapato.get('cor').lower() != cor.lower():
            continue
        if sexo and sapato.get('sexo').lower() != sexo.lower():
            continue
        if qualidade and sapato.get('qualidade').lower() != qualidade.lower():
            continue
        if marca and sapato.get('marca').lower() != marca.lower():
            continue
        if tamanho and sapato.get('tamanho').lower() != tamanho.lower():
            continue
        
        resultado.append(sapato)
        status=200

    return jsonify(resultado), status
    
@app.route("/pecas-agasalhos", methods=["GET"])
def page_agasalhos():
    agasalhos = carregar('agasalhos.json')

    cor = request.args.get('cor') #https://.../pecas-camisas?cor...
    sexo = request.args.get('sexo')
    tamanho = request.args.get ('tamanho')
    qualidade = request.args.get ('qualidade')
    marca = request.args.get ('marca')


    resultado=[]
    status=404

    for agasalho in agasalhos:
        if cor and agasalho.get('cor').lower() != cor.lower():
            continue
        if sexo and agasalho.get('sexo').lower() != sexo.lower():
            continue
        if qualidade and agasalho.get('qualidade').lower() != qualidade.lower():
            continue
        if marca and agasalho.get('marca').lower() != marca.lower():
            continue
        if tamanho and agasalho.get('tamanho').lower() != tamanho.lower():
            continue
        
        resultado.append(agasalho)
        status = 200

    return jsonify(resultado), status

@app.route("/pecas-tudo", methods=["GET"])
def page_tudo():
    tudo = []
    for arquivo in ['camisas.json', 'calcas.json', 'sapatos.json', 'agasalhos.json']:
        tudo.extend(carregar(arquivo))
    

    peca = request.args.get('peca')
    sexo = request.args.get('sexo')
    cor = request.args.get ('cor')
    tamanho = request.args.get ('tamanho')
    qualidade = request.args.get ('qualidade')
    marca = request.args.get ('marca')

    resultado=[]
    status=404

    for item in tudo:
        if cor and item.get('cor').lower() != cor.lower():
            continue
        if sexo and item.get('sexo').lower() != sexo.lower():
            continue
        if peca and item.get('peca').lower() != peca.lower():
            continue
        if qualidade and item.get('qualidade').lower() != qualidade.lower():
            continue
        if marca and item.get('marca').lower() != marca.lower():
            continue
        if tamanho and item.get('tamanho').lower() != tamanho.lower():
            continue
        
        resultado.append(item)
        status=200
    
    return jsonify(resultado), status



if __name__ == "__main__":
    app.run(debug=True)

'''
Rota                Método      Descrição                       Campos esperados                Validações necessárias                  Parâmetros                                                  Comportamento
/                   GET         Página Inicial                  nenhum                          sem validação necessária                -----                                                       ------
/pecas              GET         Filtro de pesquisa              nenhum                          sem validação necessária                -----                                                       ------
/pecas-camisas      GET         Listagem das Camisas            nenhum                          sem validação necessária                "cor", "sexo", "tamanho", "qualidade", "marca"              Retorna os Objetos que correspondem ao "=" do parâmetro (200), caso não encontre retorna "[]"
/pecas-calcas       GET         Listagem das Calças             nenhum                          sem validação necessária                "cor", "sexo", "tamanho", "qualidade", "marca"              Retorna os Objetos que correspondem ao "=" do parâmetro (200), caso não encontre retorna "[]"
/pecas-sapatos      GET         Listagem dos Sapatos            nenhum                          sem validação necessária                "cor", "sexo", "tamanho", "qualidade", "marca"              Retorna os Objetos que correspondem ao "=" do parâmetro (200), caso não encontre retorna "[]"
/pecas-agasalhos    GET         Listagem dos Agasalhos          nenhum                          sem validação necessária                "cor", "sexo", "tamanho", "qualidade", "marca"              Retorna os Objetos que correspondem ao "=" do parâmetro (200), caso não encontre retorna "[]"
/pecas-tudo         GET         Listagem de todas as roupas     nenhum                          sem validação necessária                "cor", "sexo", "peca", "tamanho", "qualidade", "marca"      Retorna os Objetos que correspondem ao "=" do parâmetro (200), caso não encontre retorna "[]"

/pecas-camisas      POST        Cadastro Camisa                 Peça, Tamanho, Doador           tipo obrigatório, data string
/pecas-camisas      POST        Cadastro Camisa                 Sexo, Qualidade, Cor, Marca     tipo não obrigatório, data string
/pecas-calcas       POST        Cadastro Calça                  Peça, Tamanho, Doador           tipo obrigatório, data string
/pecas-calcas       POST        Cadastro Calça                  Sexo, Qualidade, Cor, Marca     tipo não obrigatório, data string
/pecas-sapatos      POST        Cadastro Sapato                 Peça, Tamanho, Doador           tipo obrigatório, data string
/pecas-sapatos      POST        Cadastro Sapato                 Sexo, Qualidade, Cor, Marca     tipo não obrigatório, data string
/pecas-agasalhos    POST        Cadastro Agasalho               Peça, Tamanho, Doador           tipo obrigatório, data string
/pecas-agasalhos    POST        Cadastro Agasalho               Sexo, Qualidade, Cor, Marca     tipo não obrigatório, data string
    
/pecas-camisas/<id>         PUT         Atualização Camisa              peca, tamanho, doador           tipo não obrigatório, data string, tamanho deve ser PP/P/M/G/GG      -----                          Atualiza o objeto com o id informado (200), caso não encontre retorna 404
/pecas-camisas/<id>         PUT         Atualização Camisa              sexo, qualidade, cor, marca     tipo não obrigatório, data string                                    -----                          Atualiza o objeto com o id informado (200), caso não encontre retorna 404
/pecas-calcas/<id>          PUT         Atualização Calça               peca, tamanho, doador           tipo não obrigatório, data string, tamanho deve ser 34 ao 41         -----                          Atualiza o objeto com o id informado (200), caso não encontre retorna 404
/pecas-calcas/<id>          PUT         Atualização Calça               sexo, qualidade, cor, marca     tipo não obrigatório, data string                                    -----                          Atualiza o objeto com o id informado (200), caso não encontre retorna 404
/pecas-sapatos/<id>         PUT         Atualização Sapato              peca, tamanho, doador           tipo não obrigatório, data string, tamanho deve ser 34 ao 41         -----                          Atualiza o objeto com o id informado (200), caso não encontre retorna 404
/pecas-sapatos/<id>         PUT         Atualização Sapato              sexo, qualidade, cor, marca     tipo não obrigatório, data string                                    -----                          Atualiza o objeto com o id informado (200), caso não encontre retorna 404
/pecas-agasalhos/<id>       PUT         Atualização Agasalho            peca, tamanho, doador           tipo não obrigatório, data string, tamanho deve ser PP/P/M/G/GG      -----                          Atualiza o objeto com o id informado (200), caso não encontre retorna 404
/pecas-agasalhos/<id>       PUT         Atualização Agasalho            sexo, qualidade, cor, marca     tipo não obrigatório, data string                                    -----                          Atualiza o objeto com o id informado (200), caso não encontre retorna 404

/pecas-camisas/<id>         DELETE      Deletar Camisa                  nenhum                          sem validação necessária                -----                                                       Deleta o objeto com o id informado (200), caso não encontre retorna 404
/pecas-calcas/<id>          DELETE      Deletar Calça                   nenhum                          sem validação necessária                -----                                                       Deleta o objeto com o id informado (200), caso não encontre retorna 404
/pecas-sapatos/<id>         DELETE      Deletar Sapato                  nenhum                          sem validação necessária                -----                                                       Deleta o objeto com o id informado (200), caso não encontre retorna 404
/pecas-agasalhos/<id>       DELETE      Deletar Agasalho                nenhum                          sem validação necessária                -----                                                       Deleta o objeto com o id informado (200), caso não encontre retorna 404

'''
