from flask import Flask, render_template, request
from password_checker import check_strength

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    suggestions = []
    entropy = 0

    if request.method == "POST":
        password = request.form["password"]
        strength, suggestions, entropy = check_strength(password)

    return render_template("index.html", strength=strength, suggestions=suggestions, entropy=entropy)

if __name__ == "__main__":
    app.run(debug=True)
