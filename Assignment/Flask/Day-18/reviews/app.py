from flask import Flask, render_template

app = Flask(__name__)

@app.route("/comments")
def comments():

    comments_data = [
        {"username": "Rohan", "comment": "Awesome", "likes": 150, "flagged": False},
        {"username": "Pranav", "comment": "Fuck this photo", "likes": 20, "flagged": True},
        {"username": "Prasad", "comment": "Awesome " *30, "likes": 250, "flagged": False},
        {"username": "Vedant", "comment": "Nice", "likes": 90, "flagged": False}
    ]

    # Inappropriate words
    bad_words = ["Fuck"]

    # Process comments
    for c in comments_data:
        # Trim comment
        c["comment"] = c["comment"].strip()

        # Replace inappropriate words
        for word in bad_words:
            c["comment"] = c["comment"].replace(word, "***")

    # Statistics
    total_comments = len(comments_data)
    total_flagged = len([c for c in comments_data if c["flagged"]])
    most_liked = max(comments_data, key=lambda x: x["likes"])
    all_usernames = ", ".join([c["username"].upper() for c in comments_data])

    return render_template(
        "index.html",
        comments=comments_data,
        total_comments=total_comments,
        total_flagged=total_flagged,
        most_liked=most_liked,
        all_usernames=all_usernames
    )


if __name__ == "__main__":
    app.run(debug=True)