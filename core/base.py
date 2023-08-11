import logging
import os

import motor.motor_tornado
from interactions import Client
from interactions import listen
from interactions import logger_name


class CustomClient(Client):
    """Subclass of interactions.Client with our own logger and on_startup event"""

    def __init__(self, python_project_root_dir, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.python_project_root_dir = python_project_root_dir
        self.mongo_motor_client = motor.motor_tornado.MotorClient()

    # you can use that logger in all your extensions
    logger = logging.getLogger(logger_name)

    @listen()
    async def on_startup(self):
        """Gets triggered on startup"""
        # print("super_secret_guild_id", self.super_secret_guild_id)

        self.logger.info(f"{os.getenv('PROJECT_NAME')} - Startup Finished!")
        self.logger.info(
            "Note: Discord needs up to an hour to load your global commands / context menus. They may not appear immediately\n"
        )
