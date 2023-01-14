# Observer pattern

from abc import ABC, abstractmethod

class Observer(ABC):

    def update(self, context):
        pass

class ParentUserMobileClient(Observer):

    def update(self, message):
        print(f'MOBILE:{message}')


class ParentUserWebClient(Observer):

    def update(self, message):
        print(f'WEB: {message}')