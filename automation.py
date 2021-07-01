# Alright is a python wrapper that helps you automate WhatsApp web using python, giving you the capability to send messages, images, video, and files to both saved and unsaved contacts without having to rescan the QR code every time.


# The following liobraries can be used to automate whatsapp

# pywhatkit
# pywhatsapp
# PyWhatsapp
# WebWhatsapp-Wrapper
# Alright
# 

# The following code is used to send messages using alright
from alright import WhatsApp
messenger = WhatsApp()
messenger.find_user('2557xxxxxz')
messages = ['Type your message here']
for message in messages:  
        messenger.send_message(message)   

# The folloewing code is used to send videos
from alright import WhatsApp
messenger = WhatsApp()
messenger.find_user('mobile')
messenger.send_video('path-to-video')

# To send documents
from alright import WhatsApp
messenger = WhatsApp()
messenger.find_user('mobile')
messenger.send_file('path-to-file')
