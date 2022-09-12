import requests
import sys

intro = """
Directory Bruteforcing Tool

        .--.       .--.
    _  `    \     /    `  _
     `\.===. \.^./ .===./`
            \/`"`\/
         ,  |NAZU|  ,
        / `\|;-.-'|/` \
       /    |::\  |    \
    .-' ,-'`|:::; |`'-, '-.
        |   |::::\|   | 
        |   |::::;|   |
        |   \:::://   |
        |    `.://'   |
By Nazu    .'             `.
    _,'                 `,_
Usage: python3 http://url/ path_of_wordlist
"""
print(intro)
url = sys.argv[1]
wordlist = sys.argv[2]

def write(word):
    f1 = open("Result.txt","a")
    f1.write(word + "\n")

fo = open(wordlist,"r+")
for i in range(2000):
    word = fo.readline(10).strip()
    surl = url + word
    print("Discovering => " + surl)
    response = requests.get(surl)
    print("[+]" , response)
    if (response.status_code == 200):
        print ("[+] Found :- ",surl)
        write(word)
    else:
        pass