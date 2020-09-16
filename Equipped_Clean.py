import requests
from bs4 import BeautifulSoup
import re


# Fill in your details here to be posted to the login form.
payload = {
    'login_username': '',
    'login_password': ''
}


def ItemGrab():
    Gods = []
    CurrentSpawn = []
    with requests.Session() as s:
        p = s.post('https://sigil.outwar.com/login', data=payload)
        me = s.get('http://sigil.outwar.com/myaccount')
        soup = BeautifulSoup(me.content, 'html.parser')
        for Accounts in soup.findAll('a', attrs={'href': re.compile("^http://")}):
            Account = Accounts.get('href')
            AccountName = Accounts.get('target')
            pattern = 'PLAY!'
            result = re.match(pattern, AccountName)
            if Accounts.text != "PLAY!":
                me = s.get(Account)
                #print(Account)
                print(Accounts.text + " Is wearing ")
                print("-------------------------------")
                Equipped = s.get('https://sigil.outwar.com/equipment')
                Equipsoup = BeautifulSoup(Equipped.content, 'html.parser')
                for a in Equipsoup.find_all('img'):
                    print(a['alt'])
                print("--------------------------------")
            else:
                pass

ItemGrab()



# def GodWatch():
#     Gods = []
#     CurrentSpawn = []
#     with requests.Session() as s:
#         webhook.send("Starting a new session")
#         p = s.post('https://sigil.outwar.com/login', data=payload)
#         while True:
#             now = datetime.now()
#             current_time = now.strftime("%H:%M:%S")
#             print(current_time)
#
#             me = s.get('https://sigil.outwar.com/world?suid=1034264&serverid=1')
#             vault = s.get('https://sigil.outwar.com/raidtools')
#             soup = BeautifulSoup(vault.content, 'html.parser')
#             for a in soup.find_all("a", text=re.compile('Teleport to ')):
#                 God = a.text.replace("Teleport to ", "")
#                 CurrentSpawn.append(God)
#                 if (God in Gods):
#                     pass
#                 else:
#                     print(God + " HAS SPAWNED")
#                     webhook.send(God + " HAS SPAWNED at " + current_time)
#                     Gods.append(God)
#             for GodCheck in Gods:
#                 if (GodCheck in CurrentSpawn):
#                     pass
#                 else:
#                     webhook.send(GodCheck + " Has died " + current_time)
#                     Gods.remove(GodCheck)
#                     GodsKilled = s.get('https://sigil.outwar.com/godstatus')
#                     soup = BeautifulSoup(GodsKilled.content, 'html.parser')
#                     for a in soup.find_all("a", text=re.compile(GodCheck)):
#                         KillLogLink = a.get('href')
#                         KillLog = s.get('https://sigil.outwar.com/' + KillLogLink)
#                         KillLogContents = BeautifulSoup(KillLog.content, 'html.parser')
#                         for tag in KillLogContents.findAll("a", text=re.compile('items')):
#                             DropsDirty = tag['onmouseover']
#                             DropsClean = DropsDirty.replace("popup(event,'<b>", " ")
#                             DropsClean = DropsClean.replace("<br><br>", " ")
#                             DropsClean = DropsClean.replace(" </b>')", " ")
#                             webhook.send("Items Dropped from " + GodCheck + " " + DropsClean)
#             CurrentSpawn = []
#
#
# GodWatch()
