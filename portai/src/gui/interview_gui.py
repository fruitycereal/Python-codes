import os
import json
import logging
import threading
import asyncio
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from src.core.simulator import InterviewSimulator
from src.gui.chat_components import ScrollableChatFrame
from src.gui.audio_components import AudioManager, VoiceInputButton
from src.gui.progress_components import StatusBar, ProgressBar, QuestionProgress
from src.gui.language_components import LanguageSelector
from pathlib import Path


class InterviewGUI:
    def __init__(self):
        self.simulator = InterviewSimulator()
        self.logger = logging.getLogger(__name__)
        self.loop = asyncio.new_event_loop()
        self.available_languages = {
            "English": "en",
            "Thai": "th",
            "Japanese": "ja"
        }
        self.current_language = "en"  # Default language
        self.setup_gui()

    def run_async(self, coro):
        asyncio.run_coroutine_threadsafe(coro, self.loop)

    async def async_select_file(self, file_path):
        self.status_bar.update_status("Validating portfolio...")
        self.progress_bar.show_progress(True)
        self.logger.debug(f"Selected file: {file_path}")

        # TODO: Implement

    def select_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("All Portfolio Files", "*.*"),
                ("PDF Files", "*.pdf"),
                ("Text Files", "*.txt"),
                ("Word Files", "*.docx"),
                ("Markdown Files", "*.md"),
            ]
        )
        if file_path:
            self.file_label.configure(text=os.path.basename(file_path))
            self.run_async(self.async_select_file(file_path))

    def start_interview(self):
        self.start_button.configure(state="disabled")  # Disable immediately when clicked
        self.run_async(self.async_start_interview())

    def disable_input_controls(self):
        self.submit_button.configure(state="disabled")
        self.voice_button.configure(state="disabled")
        self.answer_entry.configure(state="disabled")

    def enable_input_controls(self, is_final=False):
        if not is_final:
            self.submit_button.configure(state="normal")
            self.voice_button.configure(state="normal")
            self.answer_entry.configure(state="normal")

    async def async_start_interview(self):
        self.logger.info("Starting interview...")
        self.status_bar.update_status("Starting interview...")
        self.progress_bar.show_progress(True)
        self.chat_area.clear()

        # Reset question progress
        self.question_progress.update_progress(0)

        # TODO: Implement

    async def async_submit_answer(self, answer):
        self.logger.info("Submitting answer...")
        self.status_bar.update_status("Processing your answer...")
        self.progress_bar.show_progress(True)
        
        # TODO: Implement

    def submit_answer(self):
        answer = self.answer_entry.get("1.0", "end-1c")
        if answer.strip():
            self.run_async(self.async_submit_answer(answer))

    def end_interview(self):
        """End the current interview and reset the UI"""

        if not messagebox.askyesno("End Interview", "Are you sure you want to end the current interview?"):
            return

        # Reset UI state
        self.chat_area.clear()
        self.answer_entry.delete("1.0", "end")
        self.answer_entry.configure(state="normal")
        self.question_progress.update_progress(0)
        
        # Reset buttons
        self.submit_button.pack_forget()
        self.end_button.pack_forget()
        self.start_button.pack(side="left", padx=5)
        self.start_button.configure(state="normal")
        self.voice_button.configure(state="disabled")
        
        # Re-enable controls
        self.language_selector.set_enabled(True)
        self.file_button.configure(state="normal")
        
        # Update status
        self.status_bar.update_status("Interview ended")
        
        # Log the event
        self.logger.info("Interview ended by user")

    def setup_gui(self):
        self.root = ctk.CTk()
        self.root.title("Portfolio Interview Simulator")
        self.root.geometry("1000x800")

        # Configure grid
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Main container
        self.main_container = ctk.CTkFrame(self.root)
        self.main_container.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

        # Header frame with title and theme switch
        self.header_frame = ctk.CTkFrame(self.main_container)
        self.header_frame.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(
            self.header_frame,
            text="Portfolio Interview Simulator",
            font=("Helvetica", 20, "bold"),
        ).pack(side="left", padx=10)

        # Theme switch
        self.theme_switch = ctk.CTkSwitch(
            self.header_frame,
            text="Dark Mode",
            command=self.toggle_theme,
            onvalue="dark",
            offvalue="light",
        )
        self.theme_switch.pack(side="right", padx=10)
        self.theme_switch.select()  # Default to dark mode

        # Language selector
        self.language_selector = LanguageSelector(
            self.header_frame, 
            self.simulator,
            lambda msg, is_error=False: self.status_bar.update_status(msg, is_error)
        )

        # File selection frame
        self.file_frame = ctk.CTkFrame(self.main_container)
        self.file_frame.pack(fill="x", padx=10, pady=5)

        self.file_button = ctk.CTkButton(
            self.file_frame,
            text="Select Portfolio File",
            command=self.select_file,
            width=150,
        )
        self.file_button.pack(side="left", padx=5)

        self.file_label = ctk.CTkLabel(
            self.file_frame, text="No file selected", width=200
        )
        self.file_label.pack(side="left", padx=5)

        # Progress bar
        self.progress_bar = ProgressBar(self.main_container)

        # Interview area with chat panel
        self.content_frame = ctk.CTkFrame(self.main_container)
        self.content_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Chat panel
        self.chat_frame = ctk.CTkFrame(self.content_frame)
        self.chat_frame.pack(side="left", fill="both", expand=True, padx=5)

        # Add question progress frame
        self.progress_frame = ctk.CTkFrame(self.chat_frame)
        self.progress_frame.pack(fill="x", padx=5, pady=5)

        # Question progress
        self.question_progress = QuestionProgress(
            self.progress_frame,
            self.simulator.config.max_questions
        )

        # Chat area
        self.chat_area = ScrollableChatFrame(
            self.chat_frame,
            width=600,
            height=400,
            fg_color="#2B2B2B",  # Darker background for chat area
        )
        self.chat_area.pack(fill="both", expand=True, padx=5, pady=5)

        # Input area frame at the bottom
        self.input_area = ctk.CTkFrame(self.main_container)
        self.input_area.pack(fill="x", side="bottom", padx=10, pady=5)

        # Answer input frame
        self.answer_frame = ctk.CTkFrame(self.input_area)
        self.answer_frame.pack(fill="x", padx=5, pady=5)

        self.answer_entry = ctk.CTkTextbox(self.answer_frame, height=100)
        self.answer_entry.pack(fill="x", padx=5, pady=5)

        # Button frame
        self.button_frame = ctk.CTkFrame(self.answer_frame)
        self.button_frame.pack(fill="x", padx=5, pady=5)

        # Create a container frame for buttons
        self.buttons_container = ctk.CTkFrame(self.button_frame, fg_color="transparent")
        self.buttons_container.pack(side="left", padx=5)

        # Audio manager
        self.audio_manager = AudioManager(self.simulator)

        # Voice input button
        self.voice_button = VoiceInputButton(
            self.buttons_container,
            self.audio_manager,
            self.answer_entry,
            lambda msg, is_error=False: self.status_bar.update_status(msg, is_error),
            run_async_callback=self.run_async,
            get_language_callback=lambda: self.language_selector.get_current_language(),
            width=150
        )
        self.voice_button.pack(side="left", padx=5)

        # Submit and start buttons
        self.submit_button = ctk.CTkButton(
            self.buttons_container,
            text="Submit Answer",
            command=self.submit_answer,
            width=150,
        )
        self.submit_button.pack(side="left", padx=5)
        self.submit_button.pack_forget()  # Initially hidden

        self.start_button = ctk.CTkButton(
            self.buttons_container,
            text="Start Interview",
            command=self.start_interview,
            width=150,
            state="disabled",
        )
        self.start_button.pack(side="left", padx=5)

        # End Interview button (initially hidden)
        self.end_button = ctk.CTkButton(
            self.buttons_container,
            text="End Interview",
            command=self.end_interview,
            width=150,
            fg_color="red",
            hover_color="darkred"
        )
        self.end_button.pack(side="left", padx=5)
        self.end_button.pack_forget()  # Initially hidden

        # Status bar
        self.status_bar = StatusBar(self.main_container)
        self.status_bar.pack(fill="x", side="bottom", padx=10, pady=5)

    def toggle_theme(self):
        if self.theme_switch.get() == "dark":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    def display_message(self, sender, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        display_text = message  # Default to original message
        message_type = None  # Default message type

        # TODO: Implement

    def run(self):
        self.logger.info("Starting application...")

        def run_event_loop():
            asyncio.set_event_loop(self.loop)
            self.loop.run_forever()

        threading.Thread(target=run_event_loop, daemon=True).start()

        try:
            self.root.mainloop()
        finally:
            self.loop.call_soon_threadsafe(self.loop.stop)
            self.simulator.cleanup()
