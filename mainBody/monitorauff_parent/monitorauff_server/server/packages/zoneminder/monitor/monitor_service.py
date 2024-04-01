from server.packages.base.base_service import BaseService
from server.packages.zoneminder.monitor.monitor_dto_serializer import \
    MonitorDTOSerializer

from .monitor_dto import MonitorDTO


class MonitorService(BaseService):

    def get_monitors(self):
        monitors_dtos = []
        monitors = self.zmapi.monitors().list()
        for monitor in monitors:
            monitors_dtos.append(MonitorDTO(**monitor.get()))

        return MonitorDTOSerializer(monitors_dtos, many=True).data

    def get_monitor(self, monitor_id: int):
        monitor = self.zmapi.monitors().find(monitor_id)

        if monitor is not None:
            return MonitorDTOSerializer(MonitorDTO(**monitor.get())).data

        return None
