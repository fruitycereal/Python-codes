import asyncio
import logging
from pathlib import Path
import customtkinter as ctk

class AudioManager:
    def __init__(self, simulator):
        self.simulator = simulator
        self.logger = logging.getLogger(__name__)
        self.is_recording = False
        self.stop_recording_event = None

    async def play_question(self, text, status_callback=None, progress_callback=None):
        """Play text as audio using text-to-speech"""
        try:
            if status_callback:
                status_callback("Converting text to speech...")
            if progress_callback:
                progress_callback(True)
            
            self.logger.debug("Converting text to speech...")
            audio_file = await self.simulator.text_to_speech(text)

            if audio_file and Path(audio_file).exists():
                if status_callback:
                    status_callback("Playing audio...")
                self.logger.debug(f"Playing audio from file: {audio_file}")
                await self.simulator.play_audio(audio_file)
                self.logger.debug("Audio playback completed")
                if status_callback:
                    status_callback("Ready")
            else:
                self.logger.error(f"Invalid audio file path: {audio_file}")
                if status_callback:
                    status_callback("Error generating audio", is_error=True)

        except Exception as e:
            self.logger.error(f"Error in audio playback: {e}")
            if status_callback:
                status_callback("Error playing audio", is_error=True)
        finally:
            if progress_callback:
                progress_callback(False)

    async def handle_voice_input(self, text_widget, status_callback=None, language=None):
        try:
            self.stop_recording_event = asyncio.Event()

            async def update_transcription(text):
                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", text)
                if status_callback:
                    status_callback("Transcribing...")

            transcript = await self.simulator.record_audio(
                stop_event=self.stop_recording_event, 
                callback=update_transcription,
                language=language
            )

            if transcript:
                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", transcript)
                if status_callback:
                    status_callback("Voice input transcribed successfully")
            else:
                if status_callback:
                    status_callback("No speech detected", is_error=True)

        except Exception as e:
            self.logger.error(f"Error processing voice input: {e}")
            if status_callback:
                status_callback("Error processing voice input", is_error=True)
        finally:
            self.is_recording = False

class VoiceInputButton(ctk.CTkButton):
    def __init__(self, master, audio_manager, text_widget, status_callback=None, run_async_callback=None, get_language_callback=None, **kwargs):
        super().__init__(master, text="🎤 Voice Input", state="disabled", **kwargs)
        self.audio_manager = audio_manager
        self.text_widget = text_widget
        self.status_callback = status_callback
        self.run_async_callback = run_async_callback
        self.get_language_callback = get_language_callback
        self.configure(command=self.toggle_voice_recording)

    def toggle_voice_recording(self):
        if not self.audio_manager.is_recording:
            # Clear existing text when starting new recording
            self.text_widget.delete("1.0", "end")

            # Start recording
            self.audio_manager.is_recording = True
            self.configure(text="⏹️ Stop Recording", fg_color=("red", "darkred"))
            if self.status_callback:
                self.status_callback("Recording... Speak clearly and click again to stop")
            if self.run_async_callback:
                # Get current language if callback is provided
                language = self.get_language_callback() if self.get_language_callback else None
                self.run_async_callback(self.audio_manager.handle_voice_input(
                    self.text_widget, 
                    self.status_callback,
                    language
                ))
        else:
            # Stop recording
            if self.audio_manager.stop_recording_event:
                self.audio_manager.stop_recording_event.set()
            if self.status_callback:
                self.status_callback("Finalizing transcription...")
            self.configure(text="🎤 Voice Input", fg_color=("gray75", "gray25")) 
