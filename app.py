from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from auth import validate_azdo_token
from services.service import generate_response

app = Flask(__name__)
CORS(app)


@app.route("/ask", methods=["POST"])
def ask():
    #Extract token
    auth_header = request.headers.get("Authorization")
    print("Authorization Header: ", auth_header)
    if not auth_header:
        abort(401, "Missing Authorization header")

    # token = auth_header.split("")[1]
    token = auth_header

    #Validate token with Azure DevOps
    # if not validate_azdo_token(token):
    #     abort(401, "Invalid Azure DevOps token")

    #Get question
    try:
        data = request.json
        question = data.get("question", "")

        if not question:
            return jsonify({"error": "No question provided"}), 400
        
    except Exception as e:
        print("Error: ", e)
        return jsonify({"error": "Failed to process request"}), 500

    #Generate mock response
    answer = generate_response(question)

    return jsonify({
        "answer": answer,
        "status": "success"
    })


if __name__ == "__main__":
    app.run(debug=True)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000)