import customtkinter as ctk


class ChatMessage(ctk.CTkFrame):
    def __init__(self, master, sender, message, timestamp, message_type=None, **kwargs):
        super().__init__(master, **kwargs)

        # Configure frame appearance based on sender
        is_user = sender.lower() == "you"
        bg_color = (
            "#2B5278" if is_user else "#383838"
        )  # Blue for user, darker gray for others

        self.configure(fg_color=bg_color)

        # Message layout
        header_frame = ctk.CTkFrame(self, fg_color=bg_color)
        header_frame.pack(fill="x", padx=5, pady=(5, 0))

        # Sender name with bold font
        ctk.CTkLabel(
            header_frame,
            text=sender,
            font=("Helvetica", 12, "bold"),
            text_color="#E0E0E0",
        ).pack(side="left", padx=5)

        # Timestamp with smaller, muted font
        ctk.CTkLabel(
            header_frame, text=timestamp, font=("Helvetica", 10), text_color="#A0A0A0"
        ).pack(side="right", padx=5)

        # Message text with word wrap
        message_frame = ctk.CTkFrame(self, fg_color=bg_color)
        message_frame.pack(fill="both", expand=True, padx=5, pady=5)

        message_label = ctk.CTkLabel(
            message_frame,
            text=message,
            font=("Helvetica", 12),
            text_color="white",
            wraplength=550,  # Adjust based on your chat window width
            justify="left",
        )
        message_label.pack(fill="both", expand=True, padx=5, pady=5)

        # Message type at the bottom (if provided)
        if message_type:
            footer_frame = ctk.CTkFrame(self, fg_color=bg_color)
            footer_frame.pack(fill="x", padx=5, pady=(0, 5))
            
            ctk.CTkLabel(
                footer_frame,
                text=message_type,
                font=("Helvetica", 10),
                text_color="#808080",  # Gray color for message type
            ).pack(side="right", padx=5)


class ScrollableChatFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.messages = []

    def add_message(self, sender, message, timestamp, message_type=None):
        # Create message bubble
        msg_frame = ChatMessage(
            self, sender=sender, message=message, timestamp=timestamp, message_type=message_type
        )

        # Pack message with appropriate alignment
        is_user = sender.lower() == "you"
        msg_frame.pack(fill="x", padx=10, pady=5, anchor="e" if is_user else "w")

        # Store reference to prevent garbage collection
        self.messages.append(msg_frame)

        # Scroll to bottom
        self.after(100, self._scroll_to_bottom)

    def _scroll_to_bottom(self):
        try:
            self._parent_canvas.yview_moveto(1.0)
        except:
            pass

    def clear(self):
        try:
            for msg in self.messages:
                try:
                    if msg.winfo_exists():
                        msg.destroy()
                except:
                    pass
            self.messages.clear()
            
            self.update_idletasks()
        except Exception as e:
            print(f"Error clearing chat: {e}")
            self.messages.clear()
