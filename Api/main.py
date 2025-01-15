from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa o CORS

app = Flask(__name__)
CORS(app)  # Permite CORS para todas as rotas

@app.route('/api/getPorcentagemDeEventosConcluidos', methods=['POST'])
def getPorcentagemDeEventosConcluidos():
    try:
        # Tenta extrair os dados do corpo da requisição
        data = request.get_json()

        # Verifica se os dados estão presentes e são números
        numeroDeEventos = data.get('numeroDeEventos', None)
        numeroDeEventosConcluidos = data.get('numeroDeEventosConcluidos', None)

        if numeroDeEventos is None or numeroDeEventosConcluidos is None:
            return jsonify({'error': 'Dados ausentes. Ambos os campos "numeroDeEventos" e "numeroDeEventosConcluidos" são obrigatórios.'}), 400

        # Verifica se os valores são números inteiros e maiores que 0
        if not isinstance(numeroDeEventos, (int, float)) or not isinstance(numeroDeEventosConcluidos, (int, float)):
            return jsonify({'error': 'Os valores "numeroDeEventos" e "numeroDeEventosConcluidos" devem ser números.'}), 400

        if numeroDeEventos <= 0:
            return jsonify({'error': '"numeroDeEventos" deve ser maior que zero.'}), 400
        if numeroDeEventosConcluidos < 0 or numeroDeEventosConcluidos > numeroDeEventos:
            return jsonify({'error': '"numeroDeEventosConcluidos" deve estar entre 0 e "numeroDeEventos".'}), 400

        # Realiza o cálculo da porcentagem
        resultadoEmFloat = numeroDeEventosConcluidos / numeroDeEventos
        resultadoEmPorcentagemSemCasasDecimais = round(resultadoEmFloat * 100)

        return jsonify({
            'result': resultadoEmPorcentagemSemCasasDecimais,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro ao processar a requisição: {str(e)}'}), 500

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
