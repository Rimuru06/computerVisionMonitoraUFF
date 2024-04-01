from config import env


class AppConstants:

    @staticmethod
    def get_api_path():
        return env.str("ZONEMINDER_API_URL")
