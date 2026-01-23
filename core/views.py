from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
# STRONA STARTOWA
def index(request):
     if request.method == "POST" and "start_game" in request.POST:
            return redirect("spin")

     return render(request, "core/main_page.html", {
        "message": "Witaj w kasynie",
     })
     

# FUNKCJA ODPOWIADAJACA ZA LOGIKE GRY
def spin(request):
    if request.method == "POST" and "reset" in request.POST:
        request.session.flush()
        return redirect("spin") 

    if "bet" not in request.session:
        request.session["bet"] = 10

    if "balance" not in request.session:
        request.session["balance"] = 1000
    played = request.session.pop("played", False)
    result = request.session.get("result", ["❓", "❓", "❓"])
    win = request.session.pop("win", False)
    payout = request.session.pop("payout", 0)
    bankrut = request.session.get("balance", 0) <= 0

    multipliers = {
        "💣": 3,
        "🐥": 4,
        "🦆": 5,
        "🌪️": 6,
        "🥕": 10,
    }
    if request.method == "POST":

        if "set_bet" in request.POST:
            request.session["bet"] = int(request.POST["set_bet"])

        elif "spin" in request.POST:

            bet = request.session["bet"]
            balance = request.session["balance"]

            if balance >= bet:

                SYMBOLS = ["💣", "🐥", "🦆", "🌪️", "🥕"]
                result = [random.choice(SYMBOLS) for _ in range(3)]

                if len(set(result)) == 1:
                    multiplier = multipliers.get(result[0])
                    win = True
                    payout = bet * multiplier
                else:
                    win = False
                    payout = -bet

                request.session["balance"] += payout

            request.session.update({
                "result": result,
                "win": win,
                "payout": payout,
                "played": True,
            })
            return redirect("spin")


    return render(request, "core/slot.html", {
        "result": result,
        "win": win,
        "payout": payout,
        "bet": request.session["bet"],
        "balance": request.session["balance"],
        "bankrut": bankrut,
        "played": played,
    })