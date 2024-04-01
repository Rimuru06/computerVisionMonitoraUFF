from server.packages.zoneminder.api import zmapi


class BaseService():

    def __init__(self):
        self.zmapi = zmapi
