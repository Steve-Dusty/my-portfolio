from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/contact/')
def contact():
    return render_template("contact.html")


@app.route('/projects/')
def projects():
    return render_template("projects.html")


@app.after_request
def add_header(r):
  print("[INFO]===> Adding headers...")
  r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
  r.headers["Pragma"] = "no-cache"
  r.headers["Expires"] = "0"
  return r


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 9999)), debug=True)