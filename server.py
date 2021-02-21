from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)


@app.route("/blog/")
def get_blog():

    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    blog_data = response.json()
    return render_template("blog.html", posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
