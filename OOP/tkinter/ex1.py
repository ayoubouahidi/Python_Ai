# import tkinter
# r = tkinter.Tk ()
# but = tkinter.Button (text = "changement légende")
# but.pack ()
# def change_legende () :
#  global but
# but.config (text = "nouvelle légende")
# but.config (command = change_legende)
# r.mainloop ()
# #############
# import tkinter as tk
# app = tk.Tk()
# message = tk.Label(app, text="Bonjour le monde")
# message.pack()
# app.mainloop()
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
     [
        r"what is your name ?",
        ["I am a simple chatbot created by Julius AI.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How can I assist you today?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright, no need to apologize. How can I assist you today?",]
    ],
    [
        r"I am fine",
        ["Great to hear that! How can I assist you today?",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am based on the internet, I do not have a physical location.',]
    ],
    [
        r"how is the weather in (.*)?",
        ["I'm not sure about the weather in %1, but I can find out for you if you'd like.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :)",]
    ],
]

def chatbot():
    print("Hi, I'm the chatbot you created! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Uncomment the following line to run the chatbot
chatbot()