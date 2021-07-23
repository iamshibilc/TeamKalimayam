import os
import requests

variable = requests.get('https://docs.google.com/spreadsheets/d/1Ij4ARxsQAyhlXt0eLnZ8d6MwXxOue5W96Cm3xJP3O90/edit?usp=drivesdk')

username = input (" username : ")
if username in variable.text:
 os.system("cd BotData && bash kalimayam.py")
else:
 print (" Your Username Not Registerd")
