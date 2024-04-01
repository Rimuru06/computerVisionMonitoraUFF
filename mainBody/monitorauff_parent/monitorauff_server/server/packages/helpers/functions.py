import uuid
import hashlib


def generate_id():
    return str(uuid.uuid4())

# Gera hash MD5 de imagem


def generate_hash_md5(imagem_recebida):
    return hashlib.md5(imagem_recebida).hexdigest()
