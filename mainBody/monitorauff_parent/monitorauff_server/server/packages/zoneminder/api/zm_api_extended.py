import pyzm.api as py_zmapi

from .helpers.groups import Groups


class ZMApiExtended(py_zmapi.ZMApi):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Groups = None

    def groups(self, options={}):
        """Returns list of groups."""

        if options.get('force_reload') or not self.Groups:
            self.Groups = Groups(api=self)
        return self.Groups
