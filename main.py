from flask import Flask, render_template, request

app = Flask(__name__)


# ------ Website Pages ------- #
@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def receive_data():
    if request.method == 'POST':
        login_username = request.form['username']
        login_password = request.form['password']
        return render_template("login_success.html", username=login_username, password=login_password)
    return render_template("login_fail.html")


if __name__ == "__main__":
    app.run(debug=True)
