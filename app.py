from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# Replace this with a long random value before deploying publicly.
app.secret_key = "change-this-secret-key-for-your-project"

OUTFITS = {
    "formal": {
        "title": "Formal Wear",
        "intro": "Polished looks for presentations, interviews, and formal occasions.",
        "items": [
            {
                "name": "Classic Office Look",
                "image": "formal_1.jpg",
                "description": "A crisp shirt paired with tailored trousers and clean formal shoes. Keep accessories minimal for a neat, professional finish."
            },
            {
                "name": "Smart Blazer Outfit",
                "image": "formal_2.jpg",
                "description": "Layer a well-fitted blazer over a shirt or simple top. Neutral colours make this outfit easy to coordinate."
            },
            {
                "name": "Elegant Formal Look",
                "image": "formal_3.jpg",
                "description": "Choose a structured outfit in complementary colours, with polished footwear and understated accessories."
            },
        ],
    },
    "college-casual": {
        "title": "College Casual",
        "intro": "Comfortable, practical outfits for classes and campus days.",
        "items": [
            {
                "name": "Everyday Denim",
                "image": "college_1.jpg",
                "description": "Pair jeans with a comfortable T-shirt or top and sneakers."
            },
            {
                "name": "Relaxed Layers",
                "image": "college_2.jpg",
                "description": "Combine a casual shirt, overshirt, or hoodie with simple bottoms for an easy layered look."
            },
            {
                "name": "Simple and Sporty",
                "image": "college_3.jpg",
                "description": "Try a breathable top, relaxed-fit trousers, and comfortable shoes for a laid-back campus outfit."
            },
        ],
    },
    "party": {
        "title": "Party Wear",
        "intro": "Dress-up ideas for celebrations, dinners, and nights out.",
        "items": [
            {
                "name": "Chic Evening Look",
                "image": "party_1.jpg",
                "description": "Build the outfit around one standout piece and finish with dressier shoes and a small accessory."
            },
            {
                "name": "Statement Style",
                "image": "party_2.jpg",
                "description": "Use a bold colour, interesting texture, or statement accessory while keeping the rest of the look balanced."
            },
            {
                "name": "Classic Party Outfit",
                "image": "party_3.jpg",
                "description": "Choose a well-fitting outfit with coordinated footwear and accessories for a polished party-ready finish."
            },
        ],
    },
}


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            session["name"] = name
            return redirect(url_for("home"))
        return render_template("login.html", error="Please enter your name.")
    return render_template("login.html")


@app.route("/home")
def home():
    if not session.get("name"):
        return redirect(url_for("login"))
    return render_template("home.html", name=session["name"])


@app.route("/occasion/<occasion>")
def occasion(occasion):
    if not session.get("name"):
        return redirect(url_for("login"))
    outfit_data = OUTFITS.get(occasion)
    if outfit_data is None:
        return redirect(url_for("home"))
    return render_template(
        "occasion.html",
        name=session["name"],
        occasion=occasion,
        outfit_data=outfit_data,
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
