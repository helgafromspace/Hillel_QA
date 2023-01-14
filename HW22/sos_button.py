
# Observer pattern

class SOSButton:

    def __init__(self, is_clicked=True):
        self.subscribers = []
        self.is_clicked = is_clicked

    def notify(self,subscriber):
        subscriber.update(self.sos_button_alert())

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self,subscriber):
        self.subscribers.remove(subscriber)
    def notify_all(self):
        for subscriber in self.subscribers:
            subscriber.update(self.sos_button_alert())
    def sos_button_alert(self):
        if self.is_clicked:
            return 'SOS message'
        else:
            return 'No alert'
