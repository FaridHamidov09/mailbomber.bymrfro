import os
import smtplib
import time

os.system("cls")
print("                                                                     ")
print("███╗   ███╗ █████╗ ██╗██╗         ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ ")
print("████╗ ████║██╔══██╗██║██║         ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗")
print("██╔████╔██║███████║██║██║         ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝")
print("██║╚██╔╝██║██╔══██║██║██║         ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗")
print("██║ ╚═╝ ██║██║  ██║██║███████╗    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║")
print("╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
print("Created by MR.FRO")
print("---------------------------------------------------")
mails=input("Your mail(gmail):")
passw=input("Your password:")
hmail=input("Boming mail:")
content=input("Mail Content:")
tim=input("Wait Time:")
messagec=input("Message Number:")
mail=smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login(mails,passw)
i=0
while(i<int(messagec)):
    time.sleep(int(tim))
    mail.sendmail(mails,hmail,content)
    i=i+1
