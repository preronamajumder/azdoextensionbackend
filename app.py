from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from auth import *
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

    token = auth_header.split(" ")[1]
    data = request.json
    question = data.get("question", "")
    org = data.get("org", "")
    print(org)

    #Validate token with Azure DevOps
    status, text = validate_azdo_token(token, org)
    if not status:
        # abort(401, "Invalid Azure DevOps token")
        return jsonify({
            "answer": text,
            "status": "error"
        })

    #Get question
    try:

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