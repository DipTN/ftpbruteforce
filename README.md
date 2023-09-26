# FTPBruteForce 💥
This script will do FTP brute force attack

## 🦦 Download: 
```
git clone https://github.com/DipTN/ftpbruteforce
```

## 🐳 Usage:
```
python ftpbruteforcer.py [-h] -t TARGETHOSTADDRESS -u USERNAME -w PASSWORD
```
- `-h`, `--help` : show this help message and exit
- `-t TARGETHOSTADDRESS`, `--target TARGETHOSTADDRESS` : The address of the host
- `-u USERNAME`, `--username USERNAME` : The username of the host
- `-w PASSWORD`, `--worldlist PASSWORD` : The path of the wordlist

## 🐤 Example:
```
python ftpbruteforcer.py -t 10.10.10.100 -u diptn -w wordlist.txt
```
