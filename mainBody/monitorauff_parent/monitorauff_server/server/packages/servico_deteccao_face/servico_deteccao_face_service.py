from server.packages.tipo_servico.tipo_servico_model import TipoServico, TipoServicoEnum


class ServicoDeteccaoFaceService():

    def get_tipo(self) -> TipoServico:
        return TipoServico.objects.get(id=TipoServicoEnum.DETECCAO_FACE.value)

    def ativar_servico(self, monitor_id: int):
        # TODO: Ativar serviço aqui
        print("Serviço Ativado")
        return None

    def desativar_servico(self, monitor_id: int):
        print("Serviço Desativado")
        return None
