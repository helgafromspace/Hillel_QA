# Observer pattern

from sos_button import SOSButton
from observers import ParentUserMobileClient, ParentUserWebClient

sos_button = SOSButton()
mobile_app = ParentUserMobileClient()
web_app = ParentUserWebClient()

sos_button.subscribe(mobile_app)
sos_button.subscribe(web_app)

sos_button.notify_all()
print('**********')
sos_button.notify(mobile_app)
sos_button.unsubscribe(mobile_app)
print('******')
sos_button.notify_all()