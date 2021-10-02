from pytube import YouTube

def high():
    link=input("\n GIVE A YOUTUBE LINK >>>")
    video=YouTube(link)
    print("\n its starting......")
    strem=video.streams.get_highest_resolution()
    strem.download()
    print("\n **COMPLETED**")

def low():
    link=input("\n GIVE A YOUTUBE LINK >>>")
    video=YouTube(link)
    print("\n its starting......")
    strem=video.streams.get_lowest_resolution()
    strem.download()
    print("\n **COMPLETED**")


print("""
 ##--------------------------------------------##
 #|                                            |#           
 #|                                            |#
 #|      YOUTUBE VIDEO DOWNLOAD>>>             |#
 #|                  BY.....                   |#
 #|                                            |#
 #|                    |*| cyber_jawahar       |#
 #|                                            |#
 ##--------------------------------------------##\n
 ##----------------------------------##
 #|                                  |#           
 #|      1 >> HIGH RESOLUTION        |#
 #|      0 >> LOW RESOLUTION         |#
 #|                                  |#
 ##----------------------------------##\n
 """)

a=int(input("ENTER THE NUM  >>>"))

if a==1:
    high()

elif a==0:
    low()

else:
    print("\n GIVE AN CORRECT INPUT")
