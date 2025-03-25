from flask import Flask, render_template, jsonify, request
import requests

app = Flask (__name__)

@app.route('/', methods=['GET','POST'])
def principal():
    return render_template ('principal.html')

@app.route('/login-cadastro', methods=['GET','POST'])
def loginCadastro():
    modo = request.args.get('modo','login') # Pega o 'modo' da URL (padrão: login)
    return render_template ('login-cadastro.html', modo=modo)    

@app.route('/sobre')
def sobre():
    return render_template ('sobre.html')


GOOGLE_CLIENT_ID = "589440849402-41stfmbd6jof40rgihp4dqdrgfjig4v3.apps.googleusercontent.com"

def token_verificacao_google(token):
    """Verifica se o token JWT do Google é válido."""
    google_url = "https://oauth2.googleapis.com/tokeninfo"
    response = requests.get(f"{google_url}?id_token={token}")
    return response.json() if response.status_code == 200 else None

@app.route("/login-google", methods=["POST"])
def login_google():
    data = request.json
    token = data.get("token")

    user_info = token_verificacao_google(token)
    if user_info and user_info.get("aud") == GOOGLE_CLIENT_ID:
        return jsonify({
            "nome": user_info["nome"],
            "email": user_info["email"],
            "foto": user_info["foto"]
        })
    else:
        return jsonify({"error": "Token inválido"}), 401

if __name__ == '__main__':
    app.run(debug=True)

