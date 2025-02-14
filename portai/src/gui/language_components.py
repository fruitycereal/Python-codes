import customtkinter as ctk
import logging

class LanguageSelector:
    AVAILABLE_LANGUAGES = {
        "English": "en",
        "Thai": "th",
        "Japanese": "ja"
    }

    def __init__(self, frame, simulator, status_callback=None):
        self.simulator = simulator
        self.status_callback = status_callback
        self.logger = logging.getLogger(__name__)
        self.current_language = "en"  # Default language
        
        # Create language selection frame
        self.language_frame = ctk.CTkFrame(frame)
        self.language_frame.pack(side="right", padx=10)
        
        # Add label
        self.label = ctk.CTkLabel(
            self.language_frame,
            text="Language:",
            font=("Helvetica", 12)
        )
        self.label.pack(side="left", padx=(0, 5))
        
        # Add dropdown
        self.language_var = ctk.StringVar(value="English")
        self.language_dropdown = ctk.CTkOptionMenu(
            self.language_frame,
            values=list(self.AVAILABLE_LANGUAGES.keys()),
            variable=self.language_var,
            command=self.change_language,
            width=120
        )
        self.language_dropdown.pack(side="left")

    def change_language(self, language_name):
        self.current_language = self.AVAILABLE_LANGUAGES[language_name]
        self.logger.info(f"Language changed to: {language_name} ({self.current_language})")
        self.simulator.set_language(self.current_language)
        if self.status_callback:
            self.status_callback(f"Language changed to {language_name}")

    def get_current_language(self):
        return self.current_language

    def set_enabled(self, enabled):
        state = "normal" if enabled else "disabled"
        self.language_dropdown.configure(state=state)
        self.label.configure(text_color="white" if enabled else "gray") 
