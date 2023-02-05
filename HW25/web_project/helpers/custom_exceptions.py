class WebTestingException(Exception):
    def __init__(self,browser):
        self.browser = browser

class UnsupportedBrowserException(WebTestingException):
    def __init__(self,browser):
        super().__init__(browser)
    def __str__(self):
        return 'UnsupportedBrowser'