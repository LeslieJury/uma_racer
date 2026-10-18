from django.shortcuts import render

from .simulator import RACERS, simulate


def setup(request):
    return render(request, "race/setup.html", {"racers": RACERS})


def run_race(request):
    if request.method != "POST":
        return setup(request)

    selected_ids = request.POST.getlist("racers")[:4]

    if len(selected_ids) < 2:
        return render(request, "race/setup.html", {
            "racers": RACERS,
            "error": "Choose at least two racers.",
        })

    distance = int(request.POST.get("distance", 1900))
    race_results = simulate(selected_ids, distance)
    return render(request, "race/results.html", race_results)
