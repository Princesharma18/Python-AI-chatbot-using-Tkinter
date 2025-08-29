import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
from datetime import datetime

class SimpleChatApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Chat Application")
        self.root.geometry("600x500")
        self.root.configure(bg="#2c3e50")
        
        self.username = ""
        self.is_connected = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="💬 Simple Chat App", 
            font=("Arial", 20, "bold"),
            fg="#ecf0f1",
            bg="#2c3e50"
        )
        title_label.pack(pady=(0, 20))
        
        # Username section
        username_frame = tk.Frame(main_frame, bg="#2c3e50")
        username_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            username_frame, 
            text="Username:", 
            font=("Arial", 12),
            fg="#ecf0f1",
            bg="#2c3e50"
        ).pack(side=tk.LEFT)
        
        self.username_entry = tk.Entry(
            username_frame, 
            font=("Arial", 12),
            bg="#34495e",
            fg="#ecf0f1",
            insertbackground="#ecf0f1"
        )
        self.username_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 10))
        self.username_entry.bind("<Return>", self.connect_chat)
        
        self.connect_btn = tk.Button(
            username_frame,
            text="Connect",
            font=("Arial", 10, "bold"),
            bg="#3498db",
            fg="white",
            command=self.connect_chat
        )
        self.connect_btn.pack(side=tk.RIGHT)
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(
            main_frame,
            font=("Arial", 11),
            bg="#34495e",
            fg="#ecf0f1",
            state=tk.DISABLED,
            wrap=tk.WORD,
            height=15
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Message input section
        input_frame = tk.Frame(main_frame, bg="#2c3e50")
        input_frame.pack(fill=tk.X)
        
        self.message_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            bg="#34495e",
            fg="#ecf0f1",
            insertbackground="#ecf0f1"
        )
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.message_entry.bind("<Return>", self.send_message)
        
        self.send_btn = tk.Button(
            input_frame,
            text="Send",
            font=("Arial", 10, "bold"),
            bg="#27ae60",
            fg="white",
            command=self.send_message
        )
        self.send_btn.pack(side=tk.RIGHT)
        
        # Status
        self.status_label = tk.Label(
            main_frame,
            text="Status: Enter username and click Connect",
            font=("Arial", 10),
            fg="#95a5a6",
            bg="#2c3e50"
        )
        self.status_label.pack(fill=tk.X, pady=(10, 0))
    
    def connect_chat(self, event=None):
        username = self.username_entry.get().strip()
        if not username:
            messagebox.showerror("Error", "Please enter a username!")
            return
        
        if not self.is_connected:
            self.username = username
            self.is_connected = True
            
            # Update UI
            self.connect_btn.config(text="Disconnect", bg="#e74c3c")
            self.status_label.config(
                text=f"Status: Connected as {self.username}", 
                fg="#27ae60"
            )
            
            # Add welcome message
            self.add_message("System", f"Welcome to the chat, {self.username}!")
            self.add_message("System", "Type a message and press Enter to chat!")
            
            # Focus on message input
            self.message_entry.focus_set()
            
        else:
            self.disconnect_chat()
    
    def disconnect_chat(self):
        self.is_connected = False
        self.connect_btn.config(text="Connect", bg="#3498db")
        self.status_label.config(text="Status: Disconnected", fg="#95a5a6")
        self.add_message("System", f"{self.username} has left the chat.")
        self.message_entry.delete(0, tk.END)
    
    def send_message(self, event=None):
        if not self.is_connected:
            messagebox.showwarning("Warning", "Please connect first!")
            return
        
        message = self.message_entry.get().strip()
        if not message:
            return
        
        # Add user message
        self.add_message(self.username, message)
        self.message_entry.delete(0, tk.END)
        
        # Bot response after 1 second
        threading.Timer(1.0, lambda: self.bot_response(message)).start()
    
    def bot_response(self, user_message):
        if not self.is_connected:
            return
            
        message_lower = user_message.lower()
        
        if any(word in message_lower for word in ["hello", "hi", "hey"]):
            response = "Hello there! 👋"
        elif "how are you" in message_lower:
            response = "I'm doing great! Thanks for asking! 😊"
        elif any(word in message_lower for word in ["bye", "goodbye"]):
            response = "Goodbye! Have a great day! 👋"
        elif "weather" in message_lower:
            response = "It's a beautiful day for chatting! ☀️"
        elif "time" in message_lower:
            response = f"Current time is {datetime.now().strftime('%H:%M:%S')}"
        else:
            import random
            responses = [
                "That's interesting! Tell me more.",
                "I see what you mean!",
                "Thanks for sharing!",
                "That's a good point!",
                "Interesting perspective!"
            ]
            response = random.choice(responses)
        
        self.add_message("ChatBot", response)
    
    def add_message(self, username, message):
        timestamp = datetime.now().strftime("%H:%M")
        
        self.chat_display.config(state=tk.NORMAL)
        
        if username == "System":
            self.chat_display.insert(tk.END, f"[{timestamp}] {message}\n")
        else:
            self.chat_display.insert(tk.END, f"[{timestamp}] {username}: {message}\n")
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def run(self):
        # Focus on username entry at start
        self.username_entry.focus_set()
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleChatApp()
    app.run()