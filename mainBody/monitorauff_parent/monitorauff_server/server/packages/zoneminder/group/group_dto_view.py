import server.packages.helpers.response_helper as responseHelper
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from server.packages.zoneminder.group.group_dto_serializer import GroupDTOSerializer
from .group_service import GroupService


class GroupDTOViewSet(viewsets.ViewSet):

    group_service = GroupService()

    def list(self, request):
        return Response(self.group_service.get_groups())

    def create(self, request):
        return responseHelper.not_implemented()

    def retrieve(self, request, pk=None):
        if pk is None or not str.isnumeric(pk):
            return responseHelper.bad_request("ID deve ser numérico")

        finded_group = self.group_service.get_group(int(pk))

        if finded_group is None:
            return responseHelper.not_found('Group')

        return Response(finded_group)

    def update(self, request, pk=None):
        return responseHelper.not_implemented()

    def partial_update(self, request, pk=None):
        return responseHelper.not_implemented()

    def destroy(self, request, pk=None):
        return responseHelper.not_implemented()

    @action(detail=False, methods=['get'], url_path='by-monitor', url_name='by-monitor')
    def get_by_monitor(self, request):
        monitor_id = request.query_params.get('monitor_id')

        if monitor_id is None or not str.isnumeric(monitor_id):
            return responseHelper.bad_request("ID deve ser numérico")

        groups = self.group_service.find_by_monitor_id(monitor_id)

        return Response(groups)
