import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html", page_title="Home")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data: 
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_url>")
def about_member(member_url):
    member = {}
    with open("data/company.json", "r") as json_data: 
        data = json.load(json_data)

    for obj in data: 
        if obj["url"] == member_url:
            member = obj

    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank {}, we have received your message".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/carrers")
def carrers():
    return render_template("carrers.html", page_title="Carrers")


if __name__ == "__main__": 
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
