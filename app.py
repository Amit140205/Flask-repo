from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOB = [
    {
        "id" : 1,
        "title" : "Data-Analyst",
        "location" : "Kolkata , India",
        "salary" : "Rs. 10,000"
    },
    {
        "id" : 2,
        "title" : "Data-Scientist",
        "location" : "Lucknow , India",
        "salary" : "Rs. 15,000"
    },
    {
        "id" : 3,
        "title" : "Fontend Developer",
        "location" : "New Delhi, India",
        # "salary" : "Rs. 9,000"
    },
    {
        "id" : 4,
        "title" : "Backend Developer",
        "location" : "Mumbai, India",
        "salary" : "Rs. 17,000"
    }
]

@app.route("/")
def func():
    return render_template("home.html",jobs = JOB,company_name = "Amit's Company")

@app.route("/api/jobs")
def takejobs():
    return jsonify(JOB)

if(__name__ == "__main__"):
    app.run()