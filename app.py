from flask import Flask, jsonify
import random

app = Flask(__name__)

charadas = [
    {'id': 1, 'charada': 'Qual a diferença entre o padre e o bule?', 'resposta': 'O padre é de muita fé, o bule é de por café.'},
    {'id': 2, 'charada': 'O que é que o padre tem uma, o papa tem duas e Jesus nenhuma?', 'resposta': 'A letra P'},
    {'id': 3, 'charada': 'Por que Adão não tinha sogra?', 'resposta': 'Porque ele morava no paraíso'},
    {'id': 4, 'charada': 'O que são 5 pontinhos pretos no palco, dançando e cantando?', 'resposta': 'Os Black Street Boys'},
    {'id': 5, 'charada': 'Qual fruta quer ser um instrumento musical?', 'resposta': 'Gra-viola'},
    {'id': 6, 'charada': 'O que acontece quando uma cobra deve para outra cobra?', 'resposta': 'A cobra cobra a cobra'},
    {'id': 7, 'charada': 'Um cachorro passou por um cinema e viu pedras, areia e tijolos. Qual o nome do filme?', 'resposta': 'Nenhum, o cinema estava em obras.'},
    {'id': 8, 'charada': 'Pedrinho disse para sua mãe que estava sendo chamado de mentiroso na escola. O que sua mãe respondeu?', 'resposta': 'Mas você ainda está de férias.'},
    {'id': 9, 'charada': 'Qual é a diferença entre a panela e o pinico?', 'resposta': 'Se você não sabe, nunca me convide para almoçar na sua casa.'},
    {'id': 10, 'charada': 'O que de noite tem cabeça e de dia perde?', 'resposta': 'O travesseiro'}
]

@app.route('/', methods = ['GET'])
def index():
    return 'API está ligada!'

@app.route('/charadas', methods=['GET'])
def charada():
    charada = random.choice(charadas)
    return jsonify(charada)

@app.route('/charadas/id/<int:id>', methods=['GET'])
def busca(id):
    for charada in charadas:
        if charada['id'] == id:
            return jsonify(charada), 200
    
    else:
        return jsonify({'mensagem': 'ERRO! Charada não encontrada.'})
    

if __name__ == '__main__':
    app.run()




