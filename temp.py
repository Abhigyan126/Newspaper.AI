"""import requests

# Specify the URL of the webpage you want to download
url = "https://www.businesstoday.in/latest/trends/story/they-are-nowhere-near-being-modest-until-iitians-humorous-take-on-modesty-sparks-debate-among-netizens-ankur-warikoo-weighs-in-449275-2024-10-08?utm_source=rssfeed"

# Send a GET request to the specified URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a file
    with open('webpage.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("Webpage downloaded successfully!")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")"""

"""
import requests
from bs4 import BeautifulSoup

# Replace this URL with the news webpage you want to scrape
url = "https://www.businesstoday.in/latest/trends/story/they-are-nowhere-near-being-modest-until-iitians-humorous-take-on-modesty-sparks-debate-among-netizens-ankur-warikoo-weighs-in-449275-2024-10-08?utm_source=rssfeed"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all text from the webpage
    all_text = soup.get_text(strip=True)

    # Optional: You can split the text into lines or paragraphs for better formatting
    lines = all_text.splitlines()
    formatted_text = [line for line in lines if line]  # Remove empty lines

    # Print all the text
    for line in formatted_text:
        print(line)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
"""


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email credentials
sender_email = 'from.news.paper.ai@gmail.com'
receiver_email = 'abhigyanpandey.cug@gmail.com'
password = 'newspaper@123@987'

# Create the MIMEMultipart object
msg = MIMEMultipart('alternative')
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "News"

# Create the plain-text and HTML version of your message
text = """\
Hi,
This is a plain text message.
"""
html = """\
<html>
  <body>
    <h1>Hello!</h1>
    <p>This is an <b>HTML</b> email with <a href="https://www.example.com">a link</a>.</p>
  </body>
</html>
"""

# Attach both the plain text and HTML version
msg.attach(MIMEText(text, 'plain'))
msg.attach(MIMEText(html, 'html'))

# Set up the SMTP server
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()

# Log in to your email account
smtp_server.login(sender_email, password)

# Send the email
smtp_server.sendmail(sender_email, receiver_email, msg.as_string())

# Close the server connection
smtp_server.quit()

print("Email sent successfully!")
