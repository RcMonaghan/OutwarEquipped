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
		table = soup.find( "table", {"id":"characterTable"} )
		for Accounts in table.findAll('a', attrs={'href': re.compile("^http://")}):
			Account = Accounts.get('href')
			AccountName = Accounts.get('target')
			pattern = 'PLAY!'
			result = re.match(pattern, AccountName)
			if Accounts.text != "PLAY!":
				me = s.get(Account)
				print("######################################################")
				print(Accounts.text + " Is wearing ")
				print("######################################################")
				Equipped = s.get('https://sigil.outwar.com/equipment')
				Bags = s.get('https://sigil.outwar.com/backpack')
				Equipsoup = BeautifulSoup(Equipped.content, 'html.parser')
				Bagsoup = BeautifulSoup(Bags.content, 'html.parser')
				for a in Equipsoup.find_all('img'):
					print(a['alt'])
					print("--------------------------------")
				print("##########################")
				print("       Bags")
				print("##########################")
				for b in Bagsoup.find_all('img', alt=True):
					print(b['alt'])
					print("--------------------------------")
				else:
					pass


ItemGrab()
