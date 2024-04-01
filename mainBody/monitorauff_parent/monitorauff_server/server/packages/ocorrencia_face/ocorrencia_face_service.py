import os
from PIL import Image
import io

from server.packages.helpers.functions import generate_id, generate_hash_md5

IMAGES_PATH = "media/deteccoes/faces"


class OcorrenciaFaceService():

    def find_faces_semelhantes(self, imagem_recebida):
        # * Chama o serviço de comparação de faces e retorna a lista de faces encontradas.

        # TODO: Implementar a chamada ao serviço de comparação de faces.

        # Salvar imagem em disco (para testes)
        # TODO: Remover essa linha quando o serviço de comparação de faces estiver funcionando.
        self.salvar_imagem_face_em_disco(imagem_recebida)

        # * Retorna os ids da faces encontradas.
        # Dados mockados
        return [2, 5, 6, 12]

    def apos_salvar(self):
        # TODO: Implementar
        pass

    def salvar_imagem_face_em_disco(self, imagem_recebida):
        nome = generate_id()
        im = Image.open(io.BytesIO(imagem_recebida))
        im.save(f"{IMAGES_PATH}/{nome}.png")
        im.close()

        return f"{nome}.png"

    def trata_request_imagem(self, request):
        imagem_recebida = request.data['file'].read()
        nome_imagem = self.salvar_imagem_face_em_disco(imagem_recebida)
        md5 = self.generate_hash_md5(imagem_recebida)

        request.data['img_filename'] = nome_imagem
        request.data['data_md5'] = md5

        return request

    def deletar_imagem_face(self, nome_imagem):
        path = f"{IMAGES_PATH}/{nome_imagem}"
        if os.path.isfile(path):
            os.remove(path)

    def generate_hash_md5(self, imagem_recebida):
        return generate_hash_md5(imagem_recebida)

    def atualizar_imagem_em_lote(self, classe):
        '''
            USADO SOMENTE EM DESENVOLVIMENTO
        '''
        # Pega a imagem em disco
        im = Image.open(f"{IMAGES_PATH}/default.png")
        md5 = self.generate_hash_md5(im.tobytes())

        for i in range(1, 21):
            nome = generate_id()
            im.save(f"{IMAGES_PATH}/{nome}.png")

            # Atualiza img_filename e md5 no banco
            classe.objects.filter(id=i).update(
                img_filename=f"{nome}.png", data_md5=md5)

        im.close()
