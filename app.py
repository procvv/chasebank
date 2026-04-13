from flask import Flask, render_template, request, redirect
from datetime import datetime
import random

app = Flask(__name__)

balance = 255.00

@app.route("/")
def home():
    return render_template("home.html", balance=balance)

@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    global balance
    if request.method == "POST":
        amount = float(request.form["amount"])
        balance += amount
        return redirect(f"/receipt?amount={amount}")
    return render_template("deposit.html")

@app.route("/receipt")
def receipt():
    amount = float(request.args.get("amount"))
    now = datetime.now()
    last4 = random.randint(1000, 9999)
    tx_id = random.randint(100000000000, 999999999999)

    return render_template("receipt.html",
                           amount=amount,
                           date=now.strftime("%m/%d/%Y %H:%M"),
                           last4=last4,
                           tx_id=tx_id)

if __name__ == "__main__":
    app.run(debug=True)