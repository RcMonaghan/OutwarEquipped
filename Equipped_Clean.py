import requests
from bs4 import BeautifulSoup
import re
#Enter what you want your filed to be named it will be saved in the same directory as the python file is ran from 
filename = ''
#Enter your username and password
# Fill in your details here to be posted to the login form.
payload = {
    'login_username': '',
    'login_password': ''
}


def ItemGrab():
    Gods = []
    CurrentSpawn = []
    file1 = open(filename+".txt", "w")
    with requests.Session() as s:
        p = s.post('https://sigil.outwar.com/login', data=payload)
        me = s.get('http://sigil.outwar.com/myaccount')
        soup = BeautifulSoup(me.content, 'html.parser')
        table = soup.find( "table", {"id":"characterTable"} )
        #file1 = open("Aretard.txt", "w")
        for Accounts in table.findAll('a', attrs={'href': re.compile("^http://")}):
            Account = Accounts.get('href')
            AccountName = Accounts.get('target')
            pattern = 'PLAY!'
            result = re.match(pattern, AccountName)
            if Accounts.text != "PLAY!":
                me = s.get(Account)
                file1.writelines("######################################################\n")
                file1.writelines(Accounts.text + " Is wearing \n")
                file1.writelines("######################################################\n")
                Equipped = s.get('https://sigil.outwar.com/equipment')
                Bags = s.get('https://sigil.outwar.com/backpack')
                Equipsoup = BeautifulSoup(Equipped.content, 'html.parser')
                Bagsoup = BeautifulSoup(Bags.content, 'html.parser')
                for a in Equipsoup.find_all('img'):
                    file1.writelines((a['alt'])+"\n")
                    file1.writelines("--------------------------------\n")
                file1.writelines("##########################\n")
                file1.writelines("       Bags\n")
                file1.writelines("##########################\n")
                for b in Bagsoup.find_all('img', alt=True):
                    file1.writelines((b['alt'])+"\n")
                    file1.writelines("--------------------------------\n")
                else:
                    pass
    file1.close()


ItemGrab()
