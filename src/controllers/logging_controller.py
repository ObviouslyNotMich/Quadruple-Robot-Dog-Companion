import os
import logging
import asyncio

# Logging class logs all errors
class LoggingController:
    def __init__(self, log_file='logs/error_log.txt'):
        self.log_file = log_file
        self._create_logs_folder()
        # TODO: Add where the logging happened (file/line)
        logging.basicConfig(filename=self.log_file, level=logging.NOTSET, format='%(levelname)s | %(asctime)s | %(message)s')

    async def log(self, message, error_level):
        await asyncio.to_thread(self._log, message, error_level)

    def _log(self, message, error_level):
        match(error_level):
            case logging.ERROR:
                logging.error(message)
            case logging.INFO:
                logging.info(message)
            case logging.DEBUG:
                logging.debug(message)
            case logging.WARNING:
                logging.warning(message)
            case logging.CRITICAL:
                logging.critical(message)
            case _:
                logging.warning(f"Tried to log something but no logging level was given: {message}")

    def _create_logs_folder(self):
        logs_dir = os.path.dirname(self.log_file)
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

# TODO: Delete later
# # Example Usage:
# async def main():
    
# Run the async function
async def main():
    logger = LoggingController()

    # Example asynchronous logging
    await logger.log("This is an error message", logging.ERROR)
    await logger.log("This is an info message", logging.INFO)
    await logger.log("This is a debug message", logging.DEBUG)
    await logger.log("This is a warning message", logging.WARNING)
    await logger.log("This is a critical message", logging.CRITICAL)
    await logger.log("This is a custom message", 25)  # Example of a custom logging level

if __name__ == "__main__":
    asyncio.run(main())
