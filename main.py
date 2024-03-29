from flask import Flask, render_template, request
import datetime
import smtplib
import os

my_mail = os.environ.get('email')
password = os.environ.get('password')

app = Flask(__name__)
current_year = datetime.datetime.now().year
app.config['SECRET_KEY'] = os.environ.get('secret_key')


def send_email(name, email, message):
    email_message = f"Subject:New Message from Portfolio website\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_mail, password)
        connection.sendmail(email, my_mail, email_message)


@app.route('/')
def index():
    return render_template('index.html', current_year=current_year)


@app.route('/contact-me', methods=["POST", "GET"])
def contact_me():
    if request.method == "POST":
        name = request.form['Name']
        email = request.form['Email']
        message = request.form['Message']
        send_email(name, email, message)
    return render_template('contact_me.html')


if __name__ == '__main__':
    app.run(debug=True)
