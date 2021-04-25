import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
os.system("clear")
os.system("figlet AL-AlamySploit")
print ("Create By : AL-AlamySploit"
print ("YouTube   : https://www.youtube.com/c/ALAlamyTube")
print ("github    : https://github.com/AL-AlamySploit")
print ("Facebook  : https://www.facebook.com/ALAlamy.Tube")
print ("Website   : https://al-alamy-tube.blogspot.com")
print ("Twitter   : https://twitter.com/ALAlamy67")
print ("           [1]> Brute Force              ")
print ("           [2]> DDos Attack              ")
print ("           [3]> NMap PortScanner         ")
print ("           [4]> Install Tools Hacking    ")
print 
print " [0]> Exit "
print
A = raw_input("A7Y >> ")

if A == "1" or A == "01":
  os.system("python2 brute.py")

elif A == "2" or A == "02":
    os.system("clear")
    os.system("figlet DDOS Attack")
    ip = raw_input("IP Address : ")
    port = raw_input("Port       : ")
    packet =raw_input("Packet     : ")
    os.system("python2 pntddos %s %s %s" % (ip, port, packet))

elif A == "3" or A == "03":
    os.system("clear")
    os.system("figlet NMap Scan")
    host = raw_input("Host : ")
    os.system("nmap %s" % (host))

elif A == "4" or A == "04":
    os.system("python2 lazymux.py")
    
elif A == "0" or A == "00":
    sys.exit()
    
else:
     print "\nERROR: Wrong Input"
     timeout(3)
     restart_program()
