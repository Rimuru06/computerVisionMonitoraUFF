from .zm_api_extended import ZMApiExtended as ZMApi
from server import env

api_options = {
    'apiurl': env.str('ZONEMINDER_API_URL'),
    'portalurl': env.str('ZONEMINDER_PORTAL_URL'),
    'user': env.str('ZONEMINDER_USER'),
    'password': env.str('ZONEMINDER_PASSWORD'),
    'force_reload': True
}

zmapi = ZMApi(options=api_options)
