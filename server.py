import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home1():
    return render_template("index.html")


@app.route("/<string:page_name>")
def home(page_name):
    return render_template(page_name)


def write_to_file(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    with open("database.txt", "a+") as file:
        file.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open("database.csv", newline="", mode="a+") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database,
            delimiter=",",
            quotechar="|",
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_details():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            return "Did not save the data, Please try again."
    else:
        message = "Something went wrong"
        return message
