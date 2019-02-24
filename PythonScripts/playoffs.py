from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

scores = pd.read_csv("Weeklyscores.csv")

@app.route('/playoffs')
def index ():
    return render_template("playoffs.html", name1 = scores.iat[0,1], s1 = scores.iat[0,2], name2 = scores.iat[1,1], s2= scores.iat[1,2])

if __name__ == "__playoffs__":
    app.run(debug=True)
    