"""
34:15
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from notion.client import NotionClient
import notion

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
    items_from_column = []

    client = NotionClient(
        token_v2=str(os.environ.get("Notion_Token")))
    main_page = client.get_block("URL TO MAIN PAGE GOES HERE")
    for main_page_child in main_page.children:  # Going through the main page (Grindset Mindset)
        if type(main_page_child) is notion.block.ColumnListBlock:
            for column_list_child in main_page_child.children:
                for column_child in column_list_child.children:  # Going through everything in the 2 columns
                    items_from_column.append(column_child)
                    if column_child.title == "🧪Things To Learn🧪":
                        things_to_learn_board = column_child.views[0]
                        print(dir(things_to_learn_board))
                        print(dir(things_to_learn_board.collection))
                        print(things_to_learn_board.collection.get())

                        # print(things_to_learn_board.get())
                        # print(things_to_learn_board.group_by)
                        # print(things_to_learn_board.child_list_key)



    current_to_do_list = []

    plaintext = f"""
    Here are your 3 items:
    Task 1: 
    Task 2: 
    Task 3: 
    """

    html = f"""\
           <html>
             <head></head>
             <body>
             <p style="font-size:18px; font-family:Tahoma, sans-serif;">Here are your 3 items:</p>
               <h3>Task 1: </h3>
               <h3>Task 2: </h3>
               <h3>Task 3: </h3>
             </body>
           </html>
           """

    return {
        "plaintext": plaintext,
        "html": html,
        "subject": "🎯 Notion Summary 🎯",
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
    # mail = smtplib.SMTP('smtp.gmail.com', 587)
    #
    # mail.ehlo()
    #
    # mail.starttls()
    #
    # mail.login('basharkevichv@gmail.com', str(os.environ.get("Notion_Reminder_Email_Auth")))
    # mail.sendmail(sender, receiver, msg.as_string())
    # mail.quit()


send_email()
