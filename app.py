from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)

# Initialize Flask-BasicAuth
app.config['BASIC_AUTH_USERNAME'] = 'soshika'
app.config['BASIC_AUTH_PASSWORD'] = '4Jk49mtg=P]T'
basic_auth = BasicAuth(app)


@app.route('/vectorize', methods=['POST'])
@basic_auth.required  # Requires authentication for this endpoint
def vectorize_query():
    data = request.get_json()
    query = data.get('query')

    # Perform vectorization using your Pars-BERT model
    # vectorized_query = vectorizer.vectorize(query)

    # Return the vectorized query as JSON
    return jsonify({'vectorized_query': 'Replace this with the actual vectorized result'})
