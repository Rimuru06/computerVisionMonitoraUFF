# https://zoneminder.readthedocs.io/en/latest/api.html#examples

from server.packages.zoneminder.monitor.monitor_dto import MonitorDTO


class GroupDTO():

    def __init__(self, **kwargs):

        self.id: int = kwargs.get('Id', None)
        self.parent_id: int = kwargs.get('ParentId', None)
        self.name: str = kwargs.get('Name', None)
        self.monitors: list[MonitorDTO] = []

        received_monitors = kwargs.get('Monitors')

        if received_monitors is not None:
            for monitor in received_monitors:
                self.monitors.append(MonitorDTO(**monitor))

    def __str__(self):
        return self.name
