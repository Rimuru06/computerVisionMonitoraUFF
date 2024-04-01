from rest_framework import serializers

from server.packages.zoneminder.monitor.monitor_dto_serializer import MonitorDTOSerializer


class GroupDTOSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    parent_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    monitors = MonitorDTOSerializer(many=True)
