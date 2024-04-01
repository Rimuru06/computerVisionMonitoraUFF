from rest_framework.response import Response


def not_implemented():
    data = {
        'status': 'error',
        'message': 'Recurso não implementado'
    }

    return Response(data=data, status=404)


def not_found(nome_recurso: str):
    data = {
        'status': 'error',
        'message': '{} não encontrado'.format(nome_recurso)
    }

    return Response(data=data, status=404)


def bad_request(message: str):
    data = {
        'status': 'error',
        'message': message
    }

    return Response(data=data, status=400)

# Erro 500


def internal_server_error(message: str):
    data = {
        'status': 'error',
        'message': message
    }

    return Response(data=data, status=500)
