#Add views here

from portfolio import app
from flask import render_template

@app.route("/")
@app.route("/<menu>")
def main(menu=""):
    menu_items = ["All projects", "About us", "Photos"]
    return render_template("frontpage/layout.html", menu_items=menu_items, current_menu=menu)


if __name__=="__main__":
    print("Main")