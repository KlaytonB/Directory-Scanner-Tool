Description:
    Directory brute force is used to find hidden and often forgotten directories on a site to try to compromise. 
    Some various automated tools and scripts retrieve the status of the directory which is brute-forced from custom wordlists.

Usage:
    python3 directory.py http://url/ path_of_wordlist

The Code:
    For this script we need two modules, requests and sys.
    We need requests to send get requests to the url, 
    and sys to send arguments from the command line.
    and also we need two inputs:
        =>  Url of the target
        =>  The path of wordlist


# Directory-Scanner-Tool
