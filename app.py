
from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from flask import redirect, url_for



app = Flask(__name__)

# ✅ Simple "email send" simulation (password-free)
def send_email(name, email, phone, business, message):
    # Real email ke liye SMTP aur credentials chahiye
    # Bina password ke hum sirf console me print karenge
    print("---- Email Simulation ----")
    print(f"To: your_email@example.com")
    print(f"Subject: New Contact Form Submission")
    print(f"Body:\nName: {name}\nEmail: {email}\nPhone: {phone}\nBusiness: {business}\nMessage: {message}")
    print("--------------------------")

# ✅ WhatsApp message (opens browser WhatsApp)
def send_whatsapp(name, phone, business, message):
    text = f"New Lead 🚀\nName: {name}\nPhone: {phone}\nBusiness: {business}\nMessage: {message}"
    whatsapp_url = f"https://wa.me/9528951373?text={text.replace(' ', '%20')}"
    return whatsapp_url



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/marketing')
def marketing():
    return render_template("marketing.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/pricing')
def pricing():
    return render_template("pricing.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")




@app.route('/contact', methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        business = request.form.get("business")
        message = request.form.get("message")

        # Email simulation
        send_email(name, email, phone, business, message)

        # Generate WhatsApp URL
        whatsapp_url = send_whatsapp(name, phone, business, message)

        # Redirect to WhatsApp
        return redirect(whatsapp_url)

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)