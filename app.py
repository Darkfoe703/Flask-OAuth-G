import os
from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer import oauth2
from config import Config


# Solo para entornos de desarrollo
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__)
app.config.from_object(Config)

google_bp = make_google_blueprint(
    client_id=app.config["GOOGLE_CLIENT_ID"],
    client_secret=app.config["GOOGLE_CLIENT_SECRET"],
    scope=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
    ],
    redirect_to="dashboard",
)
app.register_blueprint(google_bp, url_prefix="/login")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard")
def dashboard():
    resp = google.get("/oauth2/v3/userinfo")
    if not resp.ok:
        return redirect(url_for("google.login"))
    user_info = resp.json()
    context = {
        "name": user_info.get("name", "Usuario"),
        "email": user_info.get("email", "Email"),
        "image": user_info.get("picture", "Avatar"),
    }
    return render_template("dashboard.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
