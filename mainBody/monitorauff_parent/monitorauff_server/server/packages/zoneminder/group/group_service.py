from numpy import empty
from server.packages.base.base_service import BaseService
from .group_dto_serializer import GroupDTOSerializer

from .group_dto import GroupDTO


class GroupService(BaseService):

    def __get_groups(self):
        groups_dtos: list[GroupDTO] = []
        groups = self.zmapi.groups().list()
        for group in groups:
            group_dto = GroupDTO(**group.get())
            groups_dtos.append(group_dto)

        return groups_dtos

    def get_groups(self):
        groups_dtos = self.__get_groups()

        return GroupDTOSerializer(groups_dtos, many=True).data

    def get_group(self, group_id: int):
        group = self.zmapi.groups().find(group_id)

        if group is None:
            return None

        group_dto = GroupDTO(**group.get())
        return GroupDTOSerializer(group_dto).data

    def find_by_monitor_id(self, monitor_id: int):
        groups_dtos: list[GroupDTO] = self.__get_groups()
        filtered_groups: list[GroupDTO] = []

        for group in groups_dtos:
            for monitor in group.monitors:
                if monitor.id == monitor_id:
                    filtered_groups.append(group)
                    break

        return GroupDTOSerializer(filtered_groups, many=True).data
