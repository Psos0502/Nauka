from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
# STRONA STARTOWA
def index(request):
    return HttpResponse("Witaj w kasynie!")















# FUNKCJA ODPOWIADAJACA ZA LOGIKE GRY
def spin(request):
    if request.method == "POST" and "reset" in request.POST:
        request.session.flush()
        return redirect("spin") 

    if "bet" not in request.session:
        request.session["bet"] = 10

    if "balance" not in request.session:
        request.session["balance"] = 1000

    result = []
    win = False
    payout = 0
    bankrut = False

    multipliers = {
        "🍒": 3,
        "🍋": 4,
        "🍏": 5,
        "🍍": 6,
        "⭐": 10,
    }
    if request.method == "POST":

        if "set_bet" in request.POST:
            request.session["bet"] = int(request.POST["set_bet"])

        elif "spin" in request.POST:

            bet = request.session["bet"]
            balance = request.session["balance"]

            if balance >= bet:

                SYMBOLS = ["🍒", "🍋", "🍏", "🍍", "⭐"]
                result = [random.choice(SYMBOLS) for _ in range(3)]

                if len(set(result)) == 1:
                    multiplier = multipliers.get(result[0])
                    win = True
                    payout = bet * multiplier
                else:
                    win = False
                    payout = -bet

                balance += payout
                request.session["balance"] = balance

    bet = request.session["bet"]            
    balance = request.session["balance"]
    if balance == 0:
        bankrut = True

    return render(request, "core/slot.html", {
        "result": result,
        "win": win,
        "payout": payout,
        "bet": bet,
        "balance": balance,
        "bankrut": bankrut,
    })