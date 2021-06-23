from flask import Blueprint, render_template, request, flash

from . import encrypt

views = Blueprint("views", __name__)


@views.route("/",  methods=["GET", "POST"])
def home():
    if request.method == "POST":
        option = request.form.get("option")
        article = str(request.form.get("article").lower())
        print(article)
        print(option)
        if len(article) < 5:
            flash("Your message is too short it must be up to 5 char")
        if option == "Encrypt":
            reveal = encrypt.en(article)
            return render_template("encrypt.html", reveal=reveal)
        if option == "1":
            reveal = encrypt.de(article)
            return render_template("decrypt.html", reveal=reveal)
        
    return render_template("base.html")

