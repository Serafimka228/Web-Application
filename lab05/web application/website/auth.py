import traceback
from flask import Blueprint, flash, render_template, request, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password_repeat = request.form.get("password-repeat")
        if check_reg_data(username, password, password_repeat):
            if register_in_db(username, password):
                return redirect(url_for("views.main_page"))
            else:
                flash("User creation error. Try again later...", category="error")
    return render_template("Registration.html")


@auth.route("/log-in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            return render_template("Login.html")
        user = User.query.filter_by(name=username).first()
        if user:
            if check_password_hash(user.password_hash, password):
                login_user(user, remember=True)
                return redirect(url_for("views.main_page"))
            else:
                flash("Incorrect password", category="error")
        else:
            flash("Incorrect username", category="error")
    return render_template("Login.html")


@auth.route("/log-out", methods=["POST", "GET"])
@login_required
def log_out():
    if request.method == "POST" or request.method == "GET":
        logout_user()
        return redirect(url_for("auth.log_in"))


def check_reg_data(username, password, password_repeat):
    user = User.query.filter_by(name=username).first()
    if user:
        flash("Username already exists", category="error")
        return False
    elif len(username) < 4 or len(username) > 32:
        flash(
            "Username length must be more than 4 characters and less than 32",
            category="error",
        )
        return False
    elif len(password) < 8 or len(password) > 32:
        flash(
            "Password length must be more than 8 characters and less than 32",
            category="error",
        )
        return False
    elif password != password_repeat:
        flash("Passwords are not equal", category="error")
        return False
    else:
        return True


def register_in_db(username, password):
    new_user = User(name=username, password_hash=generate_password_hash(password))
    try:
        db.session.add(new_user)
        db.session.flush()
        db.session.commit()
    except:
        db.session.rollback()
        traceback.print_exc()
        print("sign_up db error")
        return False
    login_user(new_user, remember=True)
    return True
