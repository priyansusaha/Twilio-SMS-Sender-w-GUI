from tkinter import *
from twilio.rest import Client

window = Tk()
window.title("SMS")
window.iconbitmap("sms.ico")
window.config(background="#292929")
window.geometry("293x200")

account_sid = '***ACCOUNT SID***' #Make a Twilio A/c and paste the Account SID
auth_token = '***AUTH TOKEN***' #Make a Twilio A/c and paste the Auth Token
client = Client(account_sid, auth_token)

Label(window,text="SMS", font=("Times", "36", "bold italic"), bg="#292929", fg="yellow").place(x=100,y=-1)
cc = Entry(window,width=4, font=("Helvetica", "20", "bold italic"),justify='center', fg="yellow", bg="#696969")
cc.place(x=10,y=55)
cc.insert(0,"+91")
number = Entry(window,width=13, font=("Helvetica", "20", "bold italic"), fg="yellow", bg="#696969",justify='center')
number.place(x=85,y=55)
text = Entry(window, bg="#696969", width=18, font=("Helvetica", "20", "bold italic"), fg="yellow")
text.place(x=10, y=100)

def quit(s_window):
    s_window.destroy()

def send():
    cc_ = cc.get()
    num_ = number.get()
    phonenumber = f'{cc_},{num_}'
    msg = text.get()
    if len(num_)!=10:
        notValid=Tk()
        notValid.title("SMS")
        notValid.iconbitmap("sms.ico")
        notValid.config(background="#292929")
        notValid.geometry("293x100")
        Label(notValid, text="Not Valid Number", font=("Times", "24", "bold italic"), bg="#292929", fg="yellow").pack()
        Button(notValid, text="OK",font=("Times", "10", "bold italic"), command= lambda: quit(notValid)).pack()
    else:
        message = client.messages.create(
                              body=msg,
                              from_='+16503539608',
                              to=phonenumber
                          )
        print(message.sid)
    text.delete(0,len(msg))
    number.delete(0,len(num_))

sendButton= Button(window, text="SEND", width=38, height=2, command=lambda:send()).place(x=10,y=145)

window.mainloop()
