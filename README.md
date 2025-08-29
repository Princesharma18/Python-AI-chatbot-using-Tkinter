✨ Features
GUI: A clean and simple user interface using Tkinter.

Username Handling: Enter a username to connect to the chat.

Interactive Bot: The app includes a basic bot that responds to specific keywords and provides generic responses for other inputs.

Event-Driven: The app uses both button clicks and the Enter key for a seamless user experience.

Automatic Scrolling: The chat display automatically scrolls to show the latest messages.

Status Updates: A status bar shows the current connection status.

Non-Blocking UI: The bot's response is handled in a separate thread to prevent the UI from freezing.

----

💻 Tech Stack
Python: The core programming language for the application's logic.

Tkinter: Python's standard GUI (Graphical User Interface) toolkit used to create the chat window, buttons, text areas, and other visual elements.

threading module: A built-in Python library used to handle the bot's response in a separate thread, preventing the main application from freezing while waiting for a response.

datetime module: A built-in Python library used to generate timestamps for each message.

scrolledtext widget: An extension of the standard Tkinter Text widget, providing a vertical scrollbar for the chat display.

messagebox module:
