from pyzm.helpers.Base import Base


class Group(Base):
    def __init__(self, api=None, group=None):
        self.group = self._edit_group(group)
        self.api = api

    def _edit_group(self, group):
        monitores = group['Monitor']
        del(group['Monitor'])
        group['Group']['Monitors'] = monitores
        return group

    def get(self):
        """Returns group object

        Returns:
            :class:`server.packages.zoneminder.group.Group`: Group object
        """
        return self.group['Group']

    def name(self):
        """Returns group name

        Returns:
            string: group name
        """
        return self.group['Group']['Name']

    def id(self):
        """Returns group Id

        Returns:
            int: Group Id
        """
        return int(self.group['Group']['Id'])
