import random
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Get data from notion
def get_notion_data():
    """
    Gets data from Notion regarding:
    -All of Current List-
    -Things to Learn: Current Focus TODO
    -Books To Read: Current Focus TODO
    -1 Powerful Quote TODO
    -All Goals on main page TODO
    :return:
    """
    info_list = [
        "Don't criticize, condemn or complain.",
        "Give honest and sincere appreciation",
        "Arouse in the other person an eager want",
        "Become genuinely interest in other people",
        "Smile",
        "Remember that person's name is the sweetest and most important sound in any language.",
        "Be a good listener. Encourage others to talk about themselves.",
        "Talk in terms of the other person's interests.",
        "Make the other person feel important- and do it sincerely.",
        "The only way to win an argument is to avoid it.",
        "Show respect for the other person's opinions. Never say \"You're wrong\".",
        "If you are wrong, admit it quickly and emphatically.",
        "Begin in a friendly way.",
        "Get the other person saying \"Yes, yes\" immediately",
        "Let the other person do a great deal of the talking.",
        "LEADERSHIP: Begin with praise and honest appreciation.",
        "LEADERSHIP: Call attention to people's mistakes indirectly.",
        "LEADERSHIP: Talk about your own mistakes before criticizing the other person.",
        "LEADERSHIP: Ask questions instead of giving direct orders.",
        "LEADERSHIP: Let the other person save face.",
        "LEADERSHIP: Praise the slightest improvement and praise every improvement. Be hearty in your praise",
        "LEADERSHIP: Give the other person a fine reputation to live up to",
        "LEADERSHIP: Use encouragement. Make the fault seem easy to correct",
        "LEADERSHIP: Make the other person happy about doing the thing you suggest.",
    ]

    tip_to_send = random.choice(info_list)

    plaintext = f""" """

    html = f"""\
           <html>
             <head></head>
             <body>
             <p style="font-size:18px; font-family:Tahoma, sans-serif;">{tip_to_send}</p>
             </body>
           </html>
           """

    return {
        "plaintext": plaintext,
        "html": html,
        "subject": "🎯 How To Win Friends and Influence People - TIP 🎯",
    }


def send_email():
    notion_data = get_notion_data()
    sender = "basharkevichv@gmail.com"
    receiver = "basharkevichv@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = notion_data["subject"]
    msg['From'] = sender
    msg['To'] = receiver

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(notion_data["plaintext"], 'plain')
    part2 = MIMEText(notion_data["html"], 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('basharkevichv@gmail.com', str(os.environ.get("Work_Email_App_Password")))
    mail.sendmail(sender, receiver, msg.as_string())
    mail.quit()


send_email()
