from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    username = request.args.get("username")
    return render_template("index.html", username=username)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        return redirect(f"/?username={username}")
    return '''
        <form method="post">
            <input type="text" name="username">
            <input type="submit" value="Submit">
        </form>
    '''


if __name__ == "__main__":
    app.run(debug=True)
