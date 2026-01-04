from django.shortcuts import render
from django.http import HttpResponse


SYMBOLS = ["🍒", "🍋", "🍏", "🍍", "⭐"]


def index(request, id):
    return HttpResponse("</h1>%s</h1>" % id)

def spin(request):
    import random
    result = [random.choice(SYMBOLS) for _ in range(3)]
    win = len(set(result)) == 1

    return render(request, "core/slot.html", {
        "result": result,
        "win": win,
    })











# def spin(request):
#     import random
#     result = [random.choice(SYMBOLS) for _ in range(3)]
#     if len(set(result)) == 1:
#         message = "Wygrana!"
#     else:
#         message = "Spróbuj ponownie!"

#     return HttpResponse(f"{"|".join(result)}<br>{message}")

