# <h1 align="center">Directory-Scanner-Tool ☠️ ☠️ </h1>

# Description:
    Directory brute force is used to find hidden and often forgotten directories on a site to try to compromise. 
    Some various automated tools and scripts retrieve the status of the directory which is brute-forced from custom wordlists.

# Installation:
    sudo git clone https://github.com/mrnazu/Directory-Scanner-Tool.git

# Usage:
    python3 directory.py http://url/ path_of_wordlist or Directory.txt

# Example:
    python3 directory.py http://google.com/ Directory.txt
    
   ![dir](https://user-images.githubusercontent.com/108541991/189699396-cba97a99-1627-474f-bac1-f60f3e0a3d6d.jpg)

# The Code:
    For this script we need two modules, requests and sys.
    We need requests to send get requests to the url, 
    and sys to send arguments from the command line.
    and also we need two inputs:
        =>  Url of the target
        =>  The path of wordlist



