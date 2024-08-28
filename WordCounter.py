import tkinter as tk

def update_word_count(event=None):
    text = text_box.get("1.0", "end-1c")
    words = text.split()
    word_count = len(words)
    word_count_label.config(text=f"Word Count: {word_count}")

def clear_text():
    text_box.delete("1.0", "end")
    update_word_count()

# Create the main window
root = tk.Tk()
root.title("Word Count Tool")
root.geometry("400x300")

# Create a Text widget for text input
text_box = tk.Text(root, wrap="word", width=50, height=10)
text_box.pack(pady=10)

# Bind the Text widget to update the word count as the user types
text_box.bind("<KeyRelease>", update_word_count)

# Create a label to display the word count
word_count_label = tk.Label(root, text="Word Count: 0", font=("Arial", 12))
word_count_label.pack(pady=5)

# Create a Button to clear the text box
clear_button = tk.Button(root, text="Clear Text", command=clear_text)
clear_button.pack(pady=10)

# Run the application
root.mainloop()
