from django.shortcuts import render

from .simulator import RACERS, simulate


def setup(request):
    # Show the page where the user chooses the racers
    return render(request, "race/setup.html", {"racers": RACERS})


def run_race(request):
    # Send visitors back to the setup page if they open this URL directly
    if request.method != "POST":
        return setup(request)

    # Get the racers selected by the user, with a maximum of four racers
    selected_ids = request.POST.getlist("racers")[:4]

    # A race needs at least two racers
    if len(selected_ids) < 2:
        return render(request, "race/setup.html", {
            "racers": RACERS,
            "error": "Choose at least two racers.",
        })

    # Run the race and send the results to the results page
    distance = int(request.POST.get("distance", 1900))
    race_results = simulate(selected_ids, distance)
    return render(request, "race/results.html", race_results)
