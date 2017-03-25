from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	
    return render_template("1.html", title = "this is the title")


if __name__ == "__main__":
    app.run()
