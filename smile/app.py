from rapidsms.apps.base import AppBase

class Messaging(AppBase):

	def handle(self, msg):
		if msg.text == 'SMILE':
			msg.respond('Al-Atqia Mosque, King Faisal Street, Hebron. 15 February 2014, 0800-1700')
			return True
		return False

