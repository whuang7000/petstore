import connexion
import logging
from flask import make_response, render_template
from connexion.exceptions import OAuthProblem

#Hardcoded Connexion API key
TOKEN_DB = {
    'asdf1234567890': {
        'uid': 100
    }
}

def apikey_auth(token, required_scopes):
    info = TOKEN_DB.get(token, None)

    if not info:
        raise OAuthProblem('Invalid token')

    return info

app = connexion.App(__name__)
app.add_api('openapi.yaml')
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
	app.run(port=8080)

