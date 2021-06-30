#using this program you can send whatsapp message instantly
#pip install pywhatkit
import pywhatkit
k=input("enter phone number with country code")
m=input("enter instant message to be sent")
s=int(input("enter time period in sec"))

pywhatkit.sendwhatmsg_instantly(k,m,s)

