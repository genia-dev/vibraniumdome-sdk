import os

from traceloop.sdk import Traceloop

class VibraniumDome:
    @staticmethod
    def init(
        app_name: str
    ) -> None:
        if 'VIBRANIUM_DOME_BASE_URL' not in os.environ:
            os.environ['TRACELOOP_BASE_URL'] = "http://localhost:5001"
        else:
            os.environ['TRACELOOP_BASE_URL'] = os.environ['VIBRANIUM_DOME_BASE_URL']

        if 'VIBRANIUM_DOME_API_KEY' not in os.environ:
            raise ValueError("VIBRANIUM_DOME_API_KEY is not set")

        Traceloop.init(app_name=app_name, headers = {"Authorization": f"Bearer {os.environ['VIBRANIUM_DOME_API_KEY']}",})