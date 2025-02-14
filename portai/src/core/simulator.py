import logging
from pathlib import Path
from .api_client import APIClient
from .audio_manager import AudioManager
from .portfolio_manager import PortfolioManager
from .interview_session import InterviewSession
from .assistant_manager import AssistantManager
from src.config.interview_config import InterviewConfig
import asyncio

class InterviewSimulator:
    def __init__(self):
        self.api_client = APIClient()
        self.assistant_manager = AssistantManager()
        self.config = InterviewConfig()
        self.audio_manager = AudioManager(self.api_client)
        self.portfolio_manager = PortfolioManager(self.api_client, self.assistant_manager)
        self.session = InterviewSession(self.api_client, self.assistant_manager, self.config)
        self.logger = logging.getLogger(__name__)

    async def read_portfolio(self, file_path):
        try:
            validation_result = await self.portfolio_manager.validate_portfolio(file_path)
            if validation_result["valid"]:
                self.session.set_portfolio_data(validation_result["data"])
            return validation_result
        except Exception as e:
            self.logger.error(f"Error processing portfolio file: {str(e)}")
            return {
                "is_valid": False,
                "message": f"Error processing portfolio file: {str(e)}",
                "data": None,
            }

    async def start_interview(self):
        return await self.session.start_interview()

    async def submit_answer(self, answer):
        return await self.session.submit_answer(answer)

    async def text_to_speech(self, text):
        return await self.audio_manager.text_to_speech(text)

    async def play_audio(self, file_path):
        return await self.audio_manager.play_audio(file_path)

    async def record_audio(self, duration=None, stop_event=None, callback=None, language=None):
        return await self.audio_manager.record_audio(duration, stop_event, callback, language)

    def set_language(self, language_code):
        self.session.set_language(language_code)

    def cleanup(self):
        self.api_client.cleanup()
        self.portfolio_manager.cleanup()
