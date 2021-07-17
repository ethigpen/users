from flask import Flask, render_template, redirect, request
from users import User

app = Flask(__name__)
app.secret_key = "running out of ideas"

@app.route("/users")
def index():
    users = User.get_all_users()
    return render_template("index.html", users = users)

@app.route("/users/new")
def create_page():
    
    return render_template("create.html")

@app.route("/users/create", methods=["POST"])
def create():
    User.create_user(request.form)
    return redirect("/users")

@app.route("/users/<int:id>/delete")
def delete(id):
    data = {
        'id': id
    }
    User.delete_user(data)
    return redirect("/users")

@app.route("/users/<int:id>")
def show(id):
    data = {
        'id': id
    }
    user = User.get_user(data)
    return render_template("show.html", user = user)

@app.route("/users/<int:id>/edit")
def edit_user(id):
    data = {
        'id': id
    }
    user = User.get_user(data)
    return render_template("edit.html", user = user)

@app.route("/users/<int:id>/update", methods = ["POST"])
def update_user(id):
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect("/users")



if __name__ == "__main__":
    app.run(debug=True)

