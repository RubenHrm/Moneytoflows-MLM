import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Moneytoflows</title>
        </head>
        <body style='font-family: Arial; text-align: center; background: linear-gradient(to bottom, #000, #d4af37); color: white;'>
            <h1>Bienvenue sur <span style='color: #d4af37;'>Moneytoflows</span> 💸</h1>
            <p>Découvrez comment gagner de l’argent en partageant notre ebook 📘</p>
            <p>Recevez <b>20% de commission</b> (soit 1,7 $) par filleul parrainé !</p>
            <a href="#" style='background: #d4af37; color: black; padding: 10px 20px; text-decoration: none; border-radius: 5px;'>Commencez dès maintenant 🚀</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Lance le serveur sur Deployra (ou localement)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
