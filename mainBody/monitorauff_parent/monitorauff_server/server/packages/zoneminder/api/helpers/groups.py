"""
Groups
=========
Holds a list of Groups for a ZM configuration
Given groups are fairly static, maintains a cache of groups
which can be overriden 
"""


from .group import Group
from pyzm.helpers.Base import Base
import pyzm.helpers.globals as g


class Groups(Base):
    def __init__(self, api=None):
        self.api = api
        self._load()

    def _load(self, options={}) -> None:
        g.logger.Debug(2, 'Retrieving groups via API')
        url = self.api.api_url + '/groups.json'
        r = self.api._make_request(url=url)
        grs = r.get('groups')
        self.groups = []
        for gr in grs:
            self.groups.append(Group(group=gr, api=self.api))

    def list(self):
        return self.groups

    def find(self, id=None, name=None):
        """Given an id or name, returns matching group object

        Args:
            id (int, optional): MonitorId of group. Defaults to None.
            name (string, optional): Monitor name of group. Defaults to None.

        Returns:
            :class:`server.packages.zoneminder.group.Group`: Matching group object
        """
        if not id and not name:
            return None
        match = None
        if id:
            key = 'Id'
        else:
            key = 'Name'

        for gr in self.groups:
            if id and gr.id() == id:
                match = gr
                break
            if name and gr.name().lower() == name.lower():
                match = gr
                break
        return match
