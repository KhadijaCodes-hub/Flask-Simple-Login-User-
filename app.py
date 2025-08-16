from flask import Flask,request,Response,redirect,url_for,session

app = Flask(__name__) #__name__ = Tells flask that this file is the main file of our website
app.secret_key="supersecret"  # Secret key is used to lock sessions

# HOMEPAGE (Login Page)
@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username = request.form.get("username") # Here we are reading the data sent by the user
        password = request.form.get("password")

        if username=="admin" and password=="123":
            session["user"]= username  # Store in session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid Credentials. Try Again.",mimetype="text/plain") # text/HTML (By-default)

    return '''
        <h2>Login</h2>
        <form method="POST">
        Username : <input type="text" name="username"><br>
        Password : <input type="password" name="password"><br>
        <input type="submit" value="Login">
        </form>
'''        

# Welcome page (After Login)
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2>Welcome, {session["user"]}!</h2>
            <a href={url_for("logout")}>Logout</a>
        '''
    return redirect(url_for("login"))

# Logout route
@app.route("/logout")
def logout():
    session.pop("user",None) # If user is not stored in session for some reason then None will prevent from error.
    return redirect(url_for("login"))
