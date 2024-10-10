from flask import Flask, render_template

app = Flask(__name__)

# Using render_template of Flask to reder the html
@app.route("/home")
def home():
      return render_template("tutorial.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
      temperature = 23
      return {
            "station": station,
            "date": date,
            "temperature": temperature
      }

if __name__ == '__main__':
      app.run(debug=True)