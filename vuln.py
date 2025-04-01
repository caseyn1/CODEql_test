from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    return f"<h1>Helloo, {name}</h1>"  # 🔥 Reflected XSS

if __name__ == "__main__":
    app.run()

