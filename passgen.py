import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            password_result.config(text="Invalid length. Please enter a positive number.")
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            password_result.config(text=f"Generated Password: {password}")
    except ValueError:
        password_result.config(text="Invalid input. Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Random Password Generator")

# Set window dimensions to fill the entire screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry(f"{window_width}x{window_height}")

# Labels and entry fields
label_length = tk.Label(root, text="Enter Password Length:", font=("Arial", 20))
label_length.pack(pady=20)
entry_length = tk.Entry(root, font=("Arial", 18))
entry_length.pack(pady=20)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 18))
generate_button.pack(pady=40)

# Result label
password_result = tk.Label(root, text="", font=("Arial", 22))
password_result.pack()

# Run the application
root.mainloop()
