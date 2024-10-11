from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Using render_template of Flask to reder the html
@app.route("/home")
def home():
      return render_template("tutorial.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
      filePath = "/Users/admin/Documents/Others/python-projects/weather_api_app/data_small/TG_STAID" + str(station).zfill(6)+ ".txt"
      df = pd.read_csv(filePath, skiprows=20, parse_dates=["    DATE"])
      temperature = df.loc[df["    DATE"] == "1860-09-06"]['   TG'].squeeze() / 10

      return {
            "station": station,
            "date": date,
            "temperature": temperature
      }

if __name__ == '__main__':
      app.run(debug=True)