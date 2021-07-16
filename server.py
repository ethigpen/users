from flask import Flask, render_template, redirect, request
from users import User

app = Flask(__name__)
app.secret_key = 'running out of ideas'

@app.route("/users")
def index():
    users = User.get_all_users()
    return render_template("index.html", users = users)
            
@app.route("/users/new")
def create_page():
    
    return render_template("create.html")

@app.route("/users/create", methods=['POST'])
def create():
    User.create_user(request.form)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)

