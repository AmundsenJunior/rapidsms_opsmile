from rapidsms.apps.base import AppBase
import string

class Messaging(AppBase):

	def handle(self, msg):

		msg_txt = msg.text.upper().split()
		msg_len = len(msg_txt)

		if msg_txt[0] == 'SMILE' and msg_len < 3:
			msg.respond('Please reply with municipality.')
			return True
		elif msg_txt[2:] != []:
			location = string.join(msg_txt[2:])
			# Next implementation of this should be a dict to handle regions (municipalities that are nearest to a particular clinic)
			if location == 'HEBRON':
				msg.respond('Al-Atqia Mosque, King Faisal Street, Hebron. 15-20 February 2014, 0800-1700')
				return True
			elif location == 'NABLUS':
				msg.respond('Fatimid School, Omar Ibn Al-Khattab Street, Nablus. 15-20 February 2014, 0800-1700')
				return True
			elif location == 'RAFAH':
				msg.respond('Alrahma Mosque, Othman Bn Afaan, Rafah. 15-20 February 2014, 0800-1700')
				return True
			elif location == 'RAMALLAH':
				msg.respond('Alrahman Mosque, Alsawsan Street, Ramallah. 15-20 February 2014, 0800-1700')
				return True
			elif location == 'GAZA':
				msg.respond('Omary Mosque, Omar Al-Mukhtar Street, Gaza. 15-20 February 2014, 0800-1700')
				return True
			elif location == 'JERUSALEM':
				msg.respond('Maha Pharmacy, Steah Street, Jerusalem. 15-20 February 2014, 0800-1700')
				return True
			elif location == 'BETHLEHEM':
				msg.respond('Beit Jala Hospital, Madares Street, Bethlehem. 15-20 February 2014, 0800-1700')
				return True
			elif location == 'JERICHO':
				msg.respond('Al Satafi Pharmacy, Jamal Abd Al-Naser, Jericho. 15-20 February 2014, 0800-1700')
				return True
			else:
			# invalid or unknown locations
			# flag to admin in DB for investigation and manual response
				msg.respond('Location unknown. Operation Smile will investigate and respond soon with more information.')
				return True 

		else:
			return False

