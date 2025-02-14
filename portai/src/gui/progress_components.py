import customtkinter as ctk

class StatusBar(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Ready", anchor="w", **kwargs)

    def update_status(self, message, is_error=False):
        self.configure(text=message, text_color="red" if is_error else "white")

class ProgressBar(ctk.CTkProgressBar):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.set(0)
        self.pack_forget()

    def show_progress(self, show=True):
        if show:
            self.pack(fill="x", padx=10, pady=5)
            self.start()
        else:
            self.stop()
            self.pack_forget()

class QuestionProgress:
    def __init__(self, progress_frame, max_questions):
        self.max_questions = max_questions
        
        # Question counter
        self.counter_label = ctk.CTkLabel(
            progress_frame,
            text="Question Progress",
            font=("Helvetica", 12, "bold"),
        )
        self.counter_label.pack(side="left", padx=5)

        # Question progress bar
        self.progress_bar = ctk.CTkProgressBar(progress_frame)
        self.progress_bar.pack(side="right", fill="x", expand=True, padx=5)
        self.progress_bar.set(0)

        # Question counter text
        self.counter_text = ctk.CTkLabel(
            progress_frame,
            text=f"0/{self.max_questions}",
            font=("Helvetica", 12),
        )
        self.counter_text.pack(side="right", padx=5)

    def update_progress(self, current_question, max_questions=None):
        """Update the question counter and progress bar"""
        if max_questions is not None:
            self.max_questions = max_questions

        progress = current_question / self.max_questions
        self.progress_bar.set(progress)
        self.counter_text.configure(text=f"{current_question}/{self.max_questions}")

        # Update color based on progress
        if progress >= 0.8:  # Near completion
            self.progress_bar.configure(progress_color="#28a745")  # Green
        elif progress >= 0.4:  # Mid-way
            self.progress_bar.configure(progress_color="#ffc107")  # Yellow
        else:  # Starting
            self.progress_bar.configure(progress_color="#007bff")  # Blue 
