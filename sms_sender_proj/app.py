from flask import Flask, jsonify, request
from services import send_sms_service

app = Flask(__name__)

@app.route("/sms_sender/", methods=["POST"])
def sms_sender_view():
    try:
        request_data = request.get_json()
        response=send_sms_service(to=request_data['to'],message=request_data['message'])
        return (
            jsonify(
                {"Data":dict(response.messages[0])}
            ),
            200,
        )
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to send sms"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
