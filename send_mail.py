import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    username = 'f1574131a4d23d'
    password = '02319077b0854c'

    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"

    message = f"""<h3>New feedback submission</h3>
    <ul>
        <li>Customer: {customer}</li>
        <li>Dealer: {dealer}</li>
        <li>Rating: {rating}</li>
        <li>Comments: {comments}</li>
    </ul>"""

    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender
    msg['To'] = receiver

    # Send mail
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(username, password)
        server.sendmail(sender, receiver, msg.as_string())
