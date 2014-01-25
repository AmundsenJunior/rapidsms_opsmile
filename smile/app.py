from rapidsms.apps.base import AppBase
import string

class Messaging(AppBase):

	def handle(self, msg):
		msg_txt = string.upper(msg.text)
		if msg_txt == 'SMILE':
			msg.respond('Please reply with municipality.')
			return True
		else:
			location = string.lsplit(msg_txt, 'SMILE IN ')

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
				return False

