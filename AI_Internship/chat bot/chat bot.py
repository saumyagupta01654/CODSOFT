import tkinter as tk

# ---------- Chatbot Logic ----------
def get_response(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! How can I help you?"

    elif "how are you" in user_input:
        return "I'm doing great! 😊"

    elif any(word in user_input for word in ["your name", "who are you"]):
        return "I am a rule-based AI chatbot."

    elif "help" in user_input:
        return "I can answer basic questions using pattern matching."

    elif any(word in user_input for word in ["bye", "exit", "quit"]):
        return "Goodbye! Have a nice day 👋"

    else:
        return "Sorry, I didn't understand that."


# ---------- Send Message ----------
def send_message():
    user_message = entry.get()
    if user_message.strip() == "":
        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(tk.END, "You: " + user_message + "\n", "user")
    bot_reply = get_response(user_message)
    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n", "bot")

    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)
    entry.delete(0, tk.END)


# ---------- GUI Window ----------
window = tk.Tk()
window.title("AI Rule-Based Chatbot")
window.geometry("450x550")
window.config(bg="#0f172a")  # dark blue background

# ---------- Title ----------
title = tk.Label(
    window,
    text="🤖 AI Rule-Based Chatbot",
    font=("Segoe UI", 16, "bold"),
    fg="#38bdf8",
    bg="#0f172a"
)
title.pack(pady=10)

# ---------- Chat Area ----------
chat_area = tk.Text(
    window,
    height=20,
    width=50,
    bg="#020617",
    fg="white",
    font=("Consolas", 11),
    wrap=tk.WORD,
    bd=0
)
chat_area.pack(padx=10, pady=10)
chat_area.insert(tk.END, "Bot: Hello! I am your AI-style chatbot.\n\n")
chat_area.config(state=tk.DISABLED)

# Text styles
chat_area.tag_config("user", foreground="#22c55e")   # green
chat_area.tag_config("bot", foreground="#38bdf8")    # blue

# ---------- Input Area ----------
input_frame = tk.Frame(window, bg="#0f172a")
input_frame.pack(pady=10)

entry = tk.Entry(
    input_frame,
    width=30,
    font=("Segoe UI", 11),
    bg="#020617",
    fg="white",
    insertbackground="white",
    bd=0
)
entry.pack(side=tk.LEFT, padx=10, ipady=6)

send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Segoe UI", 10, "bold"),
    bg="#38bdf8",
    fg="black",
    padx=15,
    pady=6,
    bd=0,
    command=send_message
)
send_button.pack(side=tk.LEFT)

window.mainloop()
