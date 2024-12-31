from controllers.logging_controller import LoggingController


class SpeechToTextController:

    def __init__(self, session) -> None:
        self.logger = session.logger