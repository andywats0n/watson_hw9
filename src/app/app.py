from flask import Flask, render_template

app = Flask(__name__)

# landing page
@app.route("/")
def home():
    return render_template("index.html", name='home')


## viz pages
# @app.route("/")
# def home():
#     return render_template("index.html", name='home')


# @app.route("/")
# def home():
#     return render_template("index.html", name='home')


# @app.route("/")
# def home():
#     return render_template("index.html", name='home')


# @app.route("/")
# def home():
#     return render_template("index.html", name='home')


## comparison page
# @app.route("/")
# def home():
#     return render_template("index.html", name='home')


## data page
# @app.route("/")
# def home():
#     return render_template("index.html", name='home')


if __name__ == "__main__":
    app.run(debug=True)
