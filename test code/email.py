import os
os.system("echo -e 'Subject: Riasztás\r\n\r\nRiasztás!' |msmtp --debug --from=default -t RecieverEmail@gmail.com")
