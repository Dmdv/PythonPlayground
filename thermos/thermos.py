from flask import Flask, render_template, url_for

app = Flask(__name__)

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.firstname[0])

@app.route('/')
@app.route('/index')
def index():
    # by default looks in templates folder
   return render_template("index.html", user=User("Dmitry", "Dyachkov"))

@app.route('/add')
def add():
   return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
