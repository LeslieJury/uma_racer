import random


RACERS = [
    # These values are used when the race score is calculated
    {
        "id": "special_week",
        "name": "Special Week",
        "speed": 82,
        "stamina": 78,
        "power": 76,
    },
    {
        "id": "tokai_teio",
        "name": "Tokai Teio",
        "speed": 86,
        "stamina": 70,
        "power": 80,
    },
    {
        "id": "mejiro_mcqueen",
        "name": "Mejiro McQueen",
        "speed": 78,
        "stamina": 90,
        "power": 74,
    },
    {
        "id": "silence_suzuka",
        "name": "Silence Suzuka",
        "speed": 90,
        "stamina": 72,
        "power": 75,
    },
]

TRACK = [
    # The race checks each section from top to bottom
    {"name": "Opening Straight", "type": "straight", "length": 400},
    {"name": "First Corner", "type": "corner", "length": 250},
    {"name": "Uphill Section", "type": "uphill", "length": 150},
    {"name": "Backstretch", "type": "straight", "length": 500},
    {"name": "Final Corner", "type": "corner", "length": 300},
    {"name": "Final Straight", "type": "final straight", "length": 300},
]


def simulate(selected_ids, distance):
    racers = []
    events = []

    # Keep only the racers selected on the setup page
    for racer in RACERS:
        if racer["id"] in selected_ids:
            racers.append(
                {
                    "name": racer["name"],
                    "speed": racer["speed"],
                    "stamina": racer["stamina"],
                    "power": racer["power"],
                    "score": 0,
                }
            )

    # Give every racer a score for every section of the track
    for section in TRACK:
        for racer in racers:
            # Speed and a small random number give each racer a starting score
            score = random.randint(1, 10) + racer["speed"] // 10

            # Longer races make stamina more useful
            stamina_bonus = (racer["stamina"] * distance) // 10000
            score += stamina_bonus

            # Power helps in corners
            if section["type"] == "corner":
                score += racer["power"] // 10

            # Strong racers can activate an ability on the uphill
            if (
                section["type"] == "uphill"
                and racer["power"] >= 75
            ):
                score += 5
                events.append(f"{racer['name']} uses Uphill Strength.")

            # Every racer gets a small bonus on the final straight
            if section["type"] == "final straight":
                score += 5
                events.append(f"{racer['name']} uses Final Spurt.")

            racer["score"] += score

    # The highest score finishes in first place
    racers.sort(key=lambda racer: racer["score"], reverse=True)
    return {"racers": racers, "events": events, "track": TRACK, "distance": distance}
