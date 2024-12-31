import time
from controllers import AI_controller, slam_controller, motion_controller, speech_to_text_controller, text_to_speech_controller, vision_controller

from controllers.logging_controller import LoggingController

logger = LoggingController()

#TODO: code logic. This the main launch file that will boot the robot dog. 
class RobotBoi:
    def __init__(self):
        self.mode = None # Something we can set here 
        self.speech = speech_to_text_controller.SpeechToTextController(session=self.session)
        

    def launch(self):
        print("Launch time: " + time.time())
        # TODO Implement logic
        try:
            # TODO Implement error catch
            pass
        except Exception as e:
            logger.log_error(f"An error occurred: {e}")

