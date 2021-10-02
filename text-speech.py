# Import the Gtts module for text  to speech conversion 
# import Os module to start the audio file

from gtts import gTTS 
import os

#-----------------I have a file to convert voice
def first(file):
    try: 
      fh = open(file, "r")
      myText = fh.read().replace("\n", " ")

     # Language selection
      language = 'en'
      output = gTTS(text=myText, lang=language, slow=False)
      output.save("output.mp3")
      fh.close()
 
    # Play the converted file 
      os.system("start output.mp3 ")

    except FileNotFoundError as jaw:
       print("\n\n****FILE NOT FOUND CHECK IT AGAIN******\n\n")
 
#-----------------create a file and get content
def second(c_file):
    #create file
    op= open(c_file, "x")
    content=input("\nWRITE SOMTHING>>>")
    op = open(c_file,"w")
    op.write(content)
    op.close()


print(""" 
 BEFORE YOU CHECH , YOU MUST NEED GTTS AND OS MODULES
 (YOU CAN INSTALL LIKE **PIP INSTALL GTTS OS**)\n\n
 ##--------------------------------------------##
 #|                                            |#
 #|    TEXT TO VOICE CONVERTER                 |#
 #|                                            |#
 #|                  BY.....                   |#
 #|                                            |#
 #|                |*| cyber_jawahar           |#
 #|                                            |#
 ##--------------------------------------------##
 \n \n
 *-----------------------------------*
 |                                   |
 |    1 >> I HAVE A FILE             |
 |                                   |
 |    0 >> I WANT TO CREATE          |
 *-----------------------------------*   
 \n\n
 """)


check =int(input("\n SELECT ANY ONE >>>>>"))

if check==1:
    file=input("\nENTER THAT FILE NAME>>>")
    first(file)

elif check==0:
    c_file=input("\nCREATE FILE NAME>>>>")
    second(c_file)
    first(c_file)

else:
    print("\n *****CHOOSE CORRECT ONE (1/0)*****")
    os.system("python text-speech.py")

