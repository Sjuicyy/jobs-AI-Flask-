from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

# def index():
#     # Create a Redis client
#     redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

#     # Retrieve the value for a key from Redis
#     value = redis_client.get('key')

#     # Print the value to the console
#     print(value)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/employee")
def employee():
    return render_template("employee.html")

@app.route("/employerold")
def employer_old():
    return render_template("employer(old).html")

@app.route("/filterjobs")
def filterJobs():
    return render_template("filterjobs.html")

@app.route("/findjobs")
def findJobs():
    return render_template("findjobs.html")

@app.route("/jobdetail")
def jobDetail():
    return render_template("job-detail.html")

@app.route("/login")
def logIn():
    return render_template("login.html")

@app.route("/employer")
def newEmployer():
    return render_template("new-employer.html")

@app.route("/postjob")
def postJob():
    return render_template("postjob.html")

@app.route("/signup")
def signUp():
    return render_template("signup.html")

@app.route("/skeleton")
def skeleton():
    return render_template("skeleton.html")


if (__name__) == "__main__":
    app.run(debug=True)