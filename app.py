from flask import Flask, render_template, request
from calc_pixels import calc_pixels

app = Flask(__name__)

#Define the Home Page
@app.route("/")
def home():
    return render_template("home.html")

#Define the Input Page
@app.route("/input/", methods = ["POST", "GET"])
def input():
    try:
        #Initialize variables to accept inputs from a POST request
        dims = (int(request.form["h"]), int(request.form["w"]))
        c1 = (float(request.form["c1x"]), float(request.form["c1y"]))
        c2 = (float(request.form["c2x"]), float(request.form["c2y"]))
        c3 = (float(request.form["c3x"]), float(request.form["c3y"]))
        c4 = (float(request.form["c4x"]), float(request.form["c4y"]))
        corner_points = [c1, c2, c3, c4]
        sol = calc_pixels(dims, corner_points)
        return render_template("output.html",
                                height = dims[0], width = dims[1], output = sol)
    except:
        #Return to the Input Page if the user enters malformed inputs
        return render_template("input.html")

if __name__ == "__main__":
    app.run(port = 5000)