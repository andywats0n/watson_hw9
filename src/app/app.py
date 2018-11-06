from flask import Flask, render_template

app = Flask(__name__)

# landing page
@app.route("/")
def home():
    return render_template("index.html", name='home')


# viz pages
@app.route("/fig/max_temp")
def max_temp():
    return render_template("max_temp.html", name='max_temp')


@app.route("/fig/humidity")
def humidity():
    return render_template("humidity.html", name='humidity')


@app.route("/fig/cloud_cover")
def cloud_cover():
    return render_template("cloud_cover.html", name='cloud_cover')


@app.route("/fig/wind_speed")
def wind_speed():
    return render_template("wind_speed.html", name='wind_speed')


# comparison page
@app.route("/comparisons")
def comparisons():
    return render_template("comparisons.html", name='comparisons')


# data page
@app.route("/data")
def data():
    return render_template("data.html", name='data')


if __name__ == "__main__":
    app.run(debug=True)
