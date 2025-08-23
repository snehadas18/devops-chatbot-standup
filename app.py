from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# temporary "DB" - in real projects use SQLite/Postgres
standups = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        yesterday = request.form["yesterday"]
        today = request.form["today"]
        blockers = request.form["blockers"]

        standups.append({
            "name": name,
            "yesterday": yesterday,
            "today": today,
            "blockers": blockers
        })
        return redirect(url_for("report"))

    return render_template("index.html")

@app.route("/report")
def report():
    return render_template("report.html", reports=standups)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
