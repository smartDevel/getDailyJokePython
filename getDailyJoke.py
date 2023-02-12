import tkinter as tk
import requests
import tkinter.messagebox

# Function to get a joke from the jokeAPI
def get_joke(joke_type):
    # Make a GET request to the jokeAPI to get a joke
    response = requests.get(f"https://sv443.net/jokeapi/v2/joke/{joke_type}")
    # Convert the response to a dictionary
    response_dict = response.json()
    # Check if the joke is present in the dictionary
    if 'joke' in response_dict:
        joke = response_dict['joke']
    else:
        # If joke is not present, combine the setup and delivery to form a joke
        joke = response_dict['setup'] + '\n' + response_dict['delivery']
    return joke

# Function to show the joke in the GUI
def show_joke():
    # Get the selected joke type from the dropdown
    joke_type = var.get()
    # Get the joke from the API
    joke = get_joke(joke_type)
    # Update the label text with the joke
    label.config(text=joke, font=("Helvetica", 16), fg="darkgreen")

# Function to show the about message
def about_program():
    # Show an info message box with information about the program
    tkinter.messagebox.showinfo("About", "Author: Herbert Sablotny\nVersion: 1.0")

# Create the main window
root = tk.Tk()
# Set the window title
root.title("Joke of the day")

# Create a variable to store the selected joke type
var = tk.StringVar(value="Any")
# Define the options for the dropdown
options = ["Any", "Miscellaneous", "Programming", "Dark"]
# Create a dropdown menu
dropdown = tk.OptionMenu(root, var, *options)
# Pack the dropdown to the window
dropdown.pack()

# Create a button to show the joke
button = tk.Button(root, text="Show joke", command=show_joke)
# Pack the button to the window
button.pack()

# Create a label to display the joke
label = tk.Label(root, text="")
# Pack the label to the window
label.pack(pady=20)

# Create a menu bar
menu = tk.Menu(root)
# Set the menu bar for the window
root.config(menu=menu)

# Create a File menu
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
# Add an Exit option to the File menu
file_menu.add_command(label="Exit", command=root.quit)

# Create a Help menu
help_menu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
# Add an About option to the Help menu
help_menu.add_command(label="About", command=about_program)

# Start the GUI event loop
root.mainloop()
