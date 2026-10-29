from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_level(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score < 30:
        return "Noob 🐣"
    elif score < 50:
        return "Beginner 🎮"
    elif score < 70:
        return "Pro 🥇"
    elif score < 90:
        return "Expert 🔥"
    else:
        return "Legend 👑"


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        player = request.form.get("player", "").strip()
        game = request.form.get("game", "").strip()

        try:
            score = float(request.form.get("score", ""))

            if not player or not game:
                raise ValueError("Enter the player and game names.")

            level = calculate_level(score)

            result = {
                "player": player,
                "game": game,
                "score": score,
                "level": level
            }

        except ValueError as exc:
            error = str(exc)

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)