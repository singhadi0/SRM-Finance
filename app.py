
#session["stock"] is like session["symbol"]

import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session,flash,url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    username = db.execute("SELECT username FROM users WHERE id = ?",session["user_id"])[0]["username"]
    record = db.execute("SELECT symbol, SUM(shares) AS total_shares, AVG(avg_price) as price, SUM(price)  AS total_spent FROM record WHERE user_id = ? GROUP BY symbol", session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = ?" , session["user_id"])
    symbols = db.execute("SELECT DISTINCT symbol FROM record WHERE user_id = ?",session["user_id"])
    current_stocks = []
    for row in symbols:
        stock = lookup(row["symbol"])
        current_stocks.append(stock)

    return render_template("index.html", record = record , cash = cash[0]["cash"],stocks = current_stocks,username = username)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""             #concept of pressing buttons
                                          #when u press a button <input/button name = "buy_button" /> this buy_button key is passes in url's body request.get dictionary.
                                          #u find that key when method = post   thats the logic of button trigger



    if request.method == "POST":





        if "name" in request.form:

            stock = lookup(request.form.get("name"))

            if stock != None :
                session["stock"] = request.form.get("name").upper()
                return render_template("buy.html",placeholder = stock)
            else :
                 return apology("symbol not found")

        elif "buy_button" in request.form:        #button has been pressed!
              stock = lookup(session["stock"])
              number = request.form.get("number")
              total_price = stock["price"]*int(number)
              cash = db.execute("SELECT cash FROM users WHERE id = ?",session["user_id"])

              if(cash[0]['cash'] >= total_price) and int(number) >= 1:
                 db.execute("UPDATE users SET cash = cash - ? WHERE id = ?",total_price,session["user_id"])
                 db.execute("INSERT INTO record (user_id,symbol,shares,price,avg_price) VALUES (?,?,?,?,?)",session["user_id"],session["stock"].upper(),number,total_price,total_price/int(number))

                 message =  "bought  "+  number + "  shares of " + stock["name"]
                 category = "success"
                 return render_template("buy.html",placeholder = stock , message = message,category = category)
              else:

                 message = "not enought money"
                 category = "danger"
                 return render_template("buy.html",placeholder = stock, message = message,category = category)





    return render_template("buy.html",placeholder = None )


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    record = db.execute("SELECT * FROM record WHERE user_id = ?",session["user_id"])


    return render_template("history.html", record = record)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":



                # Ensure username was submitted
                if not request.form.get("username"):
                    return apology("must provide username", 403)

                # Ensure password was submitted
                elif not request.form.get("password"):
                    return apology("must provide password", 403)

                # Query database for password for the corresponding username typed
                rows = db.execute(
                    "SELECT * FROM users WHERE username = ?", request.form.get("username")
                )

                # Ensure username exists and password is correct
                if len(rows) != 1 or not check_password_hash(
                    rows[0]["hash"], request.form.get("password")
                ):
                    return apology("invalid username and/or password", 403)

                # Remember which user has logged in
                session["user_id"] = rows[0]["id"]

                flash("logged in successfully!")
                # Redirect user to home page
                return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/change_password", methods = ["GET", "POST"])
@login_required
def change_password():
                #type current pasword , check if it matches with current username typed
                #type new password

          if request.method == "POST":
                current_pass = request.form.get("current_password")
                real_pass = db.execute(    "SELECT hash FROM users WHERE id = ?"   , session["user_id"]     )[0]["hash"]
                if(check_password_hash(real_pass,current_pass)):
                    new_pass = request.form.get("new_password")
                    if(new_pass):
                        db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(new_pass) , session["user_id"])
                        return redirect("/login")
          return render_template("change_password.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()


    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":

       stock = lookup(request.form.get("name"))


       if stock != None :
           return render_template("quoted.html",placeholder = stock)
       else :
           return apology("symbol not found")

    else:

      return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])  #Fill out the register form ✅ Insert into database ✅ Redirect to login ✅
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password or not request.form.get("confirmation"):
            return apology("not provided username or password")

        if db.execute("SELECT username FROM users WHERE username = ? ", username ):
            return apology("username already taken")

        if password != request.form.get("confirmation"):
            return apology("password not matched")


        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
                 username, generate_password_hash(password)
        )


        return redirect("/login")


    return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    stock = None


    message = ""
    category = ""
    if request.method == "POST":

        if "name" in request.form :
            session["symbol"] = request.form.get("name").upper()                                                      #this name is from symbol wla input<>      type= "text" name = "name"

            session["message"] = ""
            session["category"] = ""
        elif "number" in request.form and session.get("symbol") is not None:
             session["pressed"] = request.form.get("number")
             stock = lookup(session["symbol"])
             number = int(request.form.get("number"))
             price = stock["price"]*number                                         #!!! here I wasnt aware to write number as name="number"         #this name is from sell wla input<>        type= "number" name = "number"
             if(db.execute("SELECT symbol FROM record WHERE user_id = ? and symbol = ?",session["user_id"],session["symbol"]) and
                int(number) <= db.execute("SELECT SUM(shares) FROM record WHERE user_id = ? and symbol = ?",session["user_id"] ,session["symbol"])[0]["SUM(shares)"]) and int(number) >=1:

                db.execute("UPDATE users SET cash = cash + ? WHERE id = ?",price, session["user_id"])
                db.execute("INSERT INTO record (user_id,symbol ,shares ,price,avg_price) VALUES (?,?,?,?,?)",session["user_id"],session["symbol"],-number,-price,price/number)
                session["message"] = "sold " + str(number) + " stocks of " + stock["name"]
                session["category"] = "success"
             else:
                session["message"] = "not enough shares!"
                session["category"] = "danger"

             session.pop("symbol",None)  #just after one redirect it clears the sesion, which clears the screen, use for refresh page, earlier it used to  display last stock even after page refresh (due to post thing, so using new GET(url_for()) to render clean everytime at refresh)
        return redirect(url_for("sell"))

    #GET request
    message = session.pop("message","")
    category = session.pop("category","")
    if("symbol" in session):
        stock = lookup(session["symbol"])



    return render_template("sell.html",stock = stock,message = message, category = category)



