from aspose.email import MailMessage
import os

unprocessedDir = "unprocessed/"
processedDir = "processed/"
count = 0
# Create MailMessage instance by loading an Eml file
for file in os.listdir(unprocessedDir):
    count += 1
    message = MailMessage.load(unprocessedDir + file)
    content = ""
    content += "sender: " + str(message.from_address)

    for receiver in enumerate(message.to):
        content += "receiver: " + str(receiver[1])

    content += "Subject: " + message.subject

    content += "Priority: " + str(message.priority)

    content += message.body

    substring = file[0:6]

    f = open(processedDir+substring+str(count), "w", encoding='utf-8')
    f.write(content)
    print("processed file: " + file)
    f.close()