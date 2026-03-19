from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load data
try:
    with open("data.json", "r") as file:
        data = json.load(file)
except:
    data = {}

def cocok(pesan, kunci):
    kata_pesan = set(pesan.lower().split())
    kata_kunci = set(kunci.lower().split())
    return len(kata_pesan & kata_kunci) > 0

def cari_jawaban(pesan):
    for kunci in data:
        if cocok(pesan, kunci):
            return data[kunci]
    return None

@app.route("/chat", methods=["POST"])
def chat():
    pesan = request.json["pesan"].lower()

    if "harga" in pesan:
        return jsonify({"jawaban": "Harga produk ini 50rb 😊"})

    elif "stok" in pesan:
        return jsonify({"jawaban": "Stok masih ada 👍"})

    elif "lokasi" in pesan:
        return jsonify({"jawaban": "Kami dari Jakarta 📍"})

    jawaban = cari_jawaban(pesan)

    if jawaban:
        return jsonify({"jawaban": jawaban})
    else:
        return jsonify({"jawaban": "Belum tahu 😅"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
