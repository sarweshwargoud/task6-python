from flask import Flask, render_template, request

app = Flask(__name__)

# Home / portfolio page + contact form
@app.route("/", methods=["GET", "POST"])
def home():
    message_sent = False
    submitted_data = {}

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        user_message = request.form.get("message")

        # For now we just print it in the terminal (no DB / email needed)
        print("New contact form submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {user_message}")

        submitted_data = {
            "name": name,
            "email": email,
            "message": user_message,
        }
        message_sent = True

    return render_template("index.html",
                           message_sent=message_sent,
                           submitted=submitted_data)


if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True)
