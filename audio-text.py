from os import error
import speech_recognition as sr

# --------------audio file convert to text
def audios(path):
    try:
        r = sr.Recognizer()
        with sr.AudioFile(path) as source:
         print("\n***FETCHING YOUR File***")
         audio_text = r.listen(source)
            # using google speech recognition
         print('\n YOUR AUDIO CONVERT INTO TEXT LIKE===>...\n')
         text = r.recognize_google(audio_text)
         return text
    except error:
        print("\n ******ENTER CORRECT FILE(.WAV FORMATED) ********")

#----------------our speech convert to text 
def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
     print("\nit is begin=>>>:")
     audio = r.listen(source,timeout=1,phrase_time_limit=10)
     print(">>>>>DONE. YOUR SPEECH LIKE >>>>>>>>\n")
     text2 = r.recognize_google(audio)
     return text2

#---------------our text stored in file
def files(c_file,contant):
    op= open(c_file, "x")
    op = open(c_file,"w")
    op.write(contant)
    op.close()
       
#---------------this speech not satisfied(try again)
def extra():
    input("\n YOU CAN *ENTER* TO SPEECH>>")
    ret=speech()
    print(ret)
    print("""\n
    ****DO YOU WANT TO CREATE FILE******\n
    #-----------------------------#
    |  0 >> TRY AGIN              |
    |                             |
    |  1 >> CREATE FILE           |
    |                             |
    |  2 >> FINISED--             |
    *-----------------------------* \n
    """)

    efg=int(input("ENTER THE NUMBER==> "))

    if efg==1:
        ghi=input("\n ENTER THE FILE NAME(.txt formated)==>")
        files(ghi,ret)
        print("\n good byeeee....")
    elif efg==2:
        print("\n OK GOOD BYE.....")
    elif efg==0:
        print("waiting")
    else:
         print("\n GIVE A CORRECT OPTIONS")


print("""
 IT HAVE ADDITION,SUBTRACTION,MULTIPLICATION,DIVISION ONLY.IF YOU WANT,YOU CAN ADD WHATEVER IT MAYBE..
 ##--------------------------------------------##
 #|                                            |#
 #|         VOICE TO TEXT CONVERTER            |#
 #|                                            |#
 #|                  BY.....                   |#
 #|                                            |#
 #|                |*| cyber_jawahar           |#
 #|                                            |#
 ##--------------------------------------------##\n

 *-----------------------------------*
 |                                   |
 |  1 >> I HAVE A FILE(.wav foramted)|
 |                                   |
 |  0 >> I WANT TO SPEECH            |
 *-----------------------------------* 

 """)


abc=int(input(">>ENTER THE NUMBER WHICH YOU WANT===>>"))


if abc==1:
    file=input("\n ENTER YOUR FILE (.WAV FORMATED)==>")
    ret=audios(file)
    print(ret)
    print("""\n
    ****DO YOU WANT TO CREATE FILE******
    *-----------------------------------*
    |                                   |
    |  1 >> YES                         |
    |                                   |
    |  0 >> NO                          |
    *-----------------------------------* \n
    """)
    cde=int(input("SELECT ANY ONE===>>"))

    if cde==1:
        efg=input("\n ENTER THE FILE NAME(.txt formated)==>")
        files(efg,ret)
        print("\n......BYE.....\n")
    elif cde==0:
        print("\n GOOD BYE")
    else:
        print("ENTER CORRECT INPUT 0/1")

elif abc==0:
    input("\n YOU CAN *ENTER* TO SPEECH>>")
    ret=speech()
    print(ret)
    print("""\n
    ****DO YOU WANT TO CREATE FILE******\n
    #-----------------------------#
    |  0 >> TRY AGIN              |
    |                             |
    |  1 >> CREATE FILE           |
    |                             |
    |  2 >> FINISED--             |
    *-----------------------------* \n
    """)

    efg=int(input("ENTER THE NUMBER==> "))

    if efg==1:
        ghi=input("\n ENTER THE FILE NAME(.txt formated)==>")
        files(ghi,ret)
        print("\n good byeeee....")
    elif efg==2:
        print("\n OK GOOD BYE.....")
    elif efg==0:
        extra()
    else:
        print("\n GIVE A CORRECT OPTIONS")\

else:
    print("ENETR CORRECT OPTIONS 0 / 1")     
