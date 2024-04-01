import server.packages.helpers.response_helper as responseHelper
from rest_framework import viewsets
from rest_framework.response import Response
from server.packages.zoneminder.monitor.monitor_service import MonitorService


class MonitorDTOViewSet(viewsets.ViewSet):

    monitor_service = MonitorService()

    def list(self, request):
        return Response(self.monitor_service.get_monitors())

    def create(self, request):
        return responseHelper.not_implemented()

    def retrieve(self, request, pk=None):
        if pk is None or not str.isnumeric(pk):
            return responseHelper.bad_request("ID deve ser numérico")

        finded_monitor = self.monitor_service.get_monitor(int(pk))

        if finded_monitor is None:
            return responseHelper.not_found('Monitor')

        return Response(finded_monitor)

    def update(self, request, pk=None):
        return responseHelper.not_implemented()

    def partial_update(self, request, pk=None):
        return responseHelper.not_implemented()

    def destroy(self, request, pk=None):
        return responseHelper.not_implemented()
