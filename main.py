import aspose.email as ae
import os
import cleantext
from NameFilter import namefiltering

unprocessedDir = "unprocessed/"
processedDir = "processed/"
count = 0

bad_words = ['China', 'Mobile:', 'Tel', 'Samsung', 'Mob.', 'mobile', "Phone ", "phone", "Tel.", "tel.", "Fax", "fax", "Mobile", "Mainz"]

# Create MailMessage instance by loading an email .eml file
for file in os.listdir(unprocessedDir):
    count += 1
    message = ae.MailMessage.load(unprocessedDir + file)

    # Initializes empty string for each email, adds top sender/receivers/subject/priority to file (not found in body)
    content = ""
    content += "From: " + str(message.from_address)
    for receiver in enumerate(message.to):
        content += "To: " + str(receiver[1])
    content += "Subject: " + str(message.subject)
    content += "Priority: " + str(message.priority)

    # adds body of email chain to file (includes previous email communication)
    content += str(message.body)

    # cuts down file name
    substring = file[0:6]

    # text normalization/cleaning. removes email-addresses and urls (images, company websites, etc.) from email body
    content = cleantext.replace_emails(str(content), replace_with="")
    content = cleantext.replace_urls(str(content), replace_with="")

    content = namefiltering(content)

    # filter out lines from content that contain bad words
    content = content.splitlines()
    for line in content:
        if any(bad_word in line for bad_word in bad_words):
            content.remove(line)
    content = '\n'.join(content)

    # write a function that splits content into multiple files
    # split content at "From: " and "Von: " and store each part in a new file
    # name the files with the substring and a number
    content = content.split('From:')
    for index, part in enumerate(content):
        f = open(processedDir + substring + str(index), "w", encoding='utf-8')
        f.write(part)
        f.close()

test = os.listdir(processedDir)
for i in test:
    if i.endswith("0"):
        os.remove(os.path.join(processedDir, i))










