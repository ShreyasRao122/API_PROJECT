from flask import Flask,jsonify,request
from services import generate_qr

app = Flask(__name__)

@app.route("/qrcode/",methods=["POST"])
def qr_code_generator_view():
    try:
        request_data = request.get_json()
        generate_qr(request_data["url"])
        return jsonify({"message": "QR code created Successful"}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to create qr code"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)


