from flask import Flask, render_template, request
from engine.matcher import load_problems, find_best_problem

app = Flask(__name__)

problems = load_problems()

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        user_input = request.form.get("user_input")
        matched = find_best_problem(user_input, problems)

        if matched:
            result = {
                "problem": matched["problem"],
                "title": matched["title"],
                "eastern": matched["eastern_philosophy"],
                "western": matched["western_philosophy"],
                "psychology": matched["psychology"],
                "steps": matched["actionable_steps"]
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
