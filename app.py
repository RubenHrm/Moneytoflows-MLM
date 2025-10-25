import os
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    html_content = """
    <html>
        <head>
            <meta charset="utf-8">
            <title>Moneytoflows</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background: linear-gradient(to bottom, #000, #d4af37);
                    color: white;
                    margin: 0;
                    padding: 0;
                }
                h1 span {
                    color: #d4af37;
                }
                a {
                    background: #d4af37;
                    color: black;
                    padding: 10px 20px;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                }
                a:hover {
                    background: #b8962e;
                }
            </style>
        </head>
        <body>
            <h1>Bienvenue sur <span>Moneytoflows</span> 💸</h1>
            <p>Découvrez comment gagner de l’argent en partageant notre ebook 📘</p>
            <p>Recevez <b>20% de commission</b> (soit 1,7 $) par filleul parrainé !</p>
            <a href="#">Commencez dès maintenant 🚀</a>
        </body>
    </html>
    """
    return render_template_string(html_content)

@app.route("/health")
def health():
    """Endpoint pour vérifier que le service tourne"""
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
