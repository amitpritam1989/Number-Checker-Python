import tkinter as tk  # Import Tkinter library for GUI
from tkinter import messagebox  # Import messagebox for error popups

# Function to check number properties
def check_number():
    num = entry.get().strip()  # Get user input and remove extra spaces
    
    if not num.lstrip('-').isdigit():  # Check if input is a valid number (handles negative input)
        messagebox.showerror("Invalid Input", "Please enter a valid integer!")  # Show error for invalid input
        return  # Exit function if input is invalid

    dup = int(num)  # Convert string input to integer

    # --- Basic Number Properties ---
    if dup > 0:
        num_type = "Positive"
    elif dup < 0:
        num_type = "Negative"
    else:
        num_type = "Zero"

    # --- Even or Odd Check ---
    even_odd = "Even" if dup % 2 == 0 else "Odd"

    # --- Prime or Composite Check ---
    if dup > 1:
        is_prime = all(dup % i != 0 for i in range(2, int(dup ** 0.5) + 1))
        prime_comp = "Prime" if is_prime else "Composite"
    elif dup == 1:
        prime_comp = "Neither Prime nor Composite"
    else:
        prime_comp = "Not applicable for negative numbers"

    # --- Perfect Number Check ---
    if dup > 0:
        sum_of_divisors = sum(i for i in range(1, dup) if dup % i == 0)
        perfect = "Perfect Number" if sum_of_divisors == dup else "Not a Perfect Number"
    else:
        perfect = "Perfect Number check is only for positive numbers"

    # --- Special Number Properties ---
    num_str = str(abs(dup))  # Convert to string (absolute value for negative numbers)
    total = sum(int(digit) for digit in num_str)  # Sum of digits
    spy = 1  # Initialize spy number product as 1
    armstg = sum(int(digit) ** len(num_str) for digit in num_str)  # Armstrong number calculation
    disarum = sum(int(num_str[i]) ** (i + 1) for i in range(len(num_str)))  # Disarium number calculation

    # Calculate product of digits for Spy number check
    for digit in num_str:
        spy *= int(digit)

    # Prepare the result string to display
    results = f"Entered Number: {dup}\n\n"
    results += f"Type: {num_type}\n"
    results += f"Even or Odd: {even_odd}\n"
    results += f"Prime or Composite: {prime_comp}\n"
    results += f"Perfect Number: {perfect}\n\n"

    results += f"Sum of digits: {total}\n"

    # Niven Number Check
    results += f"{dup} is a Niven Number\n" if dup != 0 and dup % total == 0 else f"{dup} is NOT a Niven Number\n"

    # Armstrong Number Check
    results += f"{dup} is an Armstrong Number\n" if abs(dup) == armstg else f"{dup} is NOT an Armstrong Number\n"

    # Disarium Number Check
    results += f"{dup} is a Disarium Number\n" if abs(dup) == disarum else f"{dup} is NOT a Disarium Number\n"

    # Spy Number Check
    results += f"{dup} is a Spy Number\n" if total == spy else f"{dup} is NOT a Spy Number\n"

    # Clear the previous result and insert new results in the text widget
    result_text.delete("1.0", tk.END)  # Clear previous text from the text box
    result_text.insert(tk.END, results)  # Insert the new results into the text box


# Create the main window (root)
root = tk.Tk()  # Initialize the main Tkinter window
root.title("Number Checker")  # Set the title of the window
root.geometry("500x500")  # Set the size of the window (width x height)
root.configure(bg="lightgray")  # Set the background color of the window

# Create and place widgets

# Label to ask user for input
tk.Label(root, text="Enter a Number:", font=("Arial", 12), bg="lightgray").pack(pady=10)

# Entry widget for user to type a number
entry = tk.Entry(root, font=("Arial", 14))  # Create an entry box for user input
entry.pack(pady=5)  # Add some space below the entry box

# Button to trigger number checker
tk.Button(root, text="Check", command=check_number, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

# Text widget to display results
result_text = tk.Text(root, height=15, width=50, font=("Arial", 12))  # Create a text box to show results
result_text.pack(pady=10)  # Add some space below the result box

# Run the main event loop to display the window
root.mainloop()  # This keeps the window running and waits for user interaction
