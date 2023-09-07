from aspose.email import MailMessage
import os
import cleantext

unprocessedDir = "unprocessed/"
processedDir = "processed/"
count = 0

# Create MailMessage instance by loading an email .eml file
for file in os.listdir(unprocessedDir):
    count += 1
    message = MailMessage.load(unprocessedDir + file)

    # Initializes empty string for each email, adds top sender/receivers/subject/priority to file (not found in body)
    content = ""
    content += "sender: " + str(message.from_address)
    for receiver in enumerate(message.to):
        content += "receiver: " + str(receiver[1])
    content += "Subject: " + str(message.subject)
    content += "Priority: " + str(message.priority)

    # adds body of email chain to file (includes previous email communication)
    content += str(message.body)

    # cuts down file name
    substring = file[0:6]

    # text normalization/cleaning. removes email-addresses and urls (images, company websites, etc.) from email body
    content = cleantext.replace_emails(str(content), replace_with="")
    content = cleantext.replace_urls(str(content), replace_with="")

    # opens a new temporary FULL file and writes content to it
    f = open("FULL"+substring+str(count), "w", encoding='utf-8')
    f.write(content)
    print("processed file: " + file)
    f.close()

    # writing emails adds unessecary \n, fixed by iterating over FULL file and writing every second line to final file
    with open("FULL"+substring+str(count), "r", encoding='utf-8') as in_file, open(processedDir+substring+str(count), "w", encoding='utf-8') as out_file:
        for index, line in enumerate(in_file):
            if (index + 1) % 2:
                out_file.write(line)
    # deletes temp FULL file
    os.remove("FULL"+substring+str(count))
