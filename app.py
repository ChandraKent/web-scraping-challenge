from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import os

app = Flask(__name__)


#dbclient = MongoClient(mongodb_uri)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
app.config["MONGO_URI"] = "mongodb+srv://<badchai>:<badkitty6!>@cluster-apc2i.mongodb.net/test?retryWrites=true&w=majority/mars_app"
mongo = PyMongo(app)

@app.route("/")
def home():
    mars_info = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def scrape():
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_image()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_weather()
    mars_data = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("Scraping Successful", code=302)

if __name__ == "__main__":
    app.run(debug=True)