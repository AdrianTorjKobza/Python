# Import the GUI widgets from guizero
from guizero import App, TextBox, PushButton, Box

# Create the app for the program
app = App(title="Text Editor")

# Open the text file and upload the content into text editor
def open_file():
    with open(file_name.value, "r") as f:
        editor.value = f.read()

# Save the edited text into the text file
def save_file():
    with open(file_name.value, "w") as f:
        f.write(editor.value)

# Create a box / container for the controls
file_controls = Box(app, align="top", width="fill")

# Create a text box for the file name
file_name = TextBox(file_controls, text = "text_file.txt", width=50, align="left")

# Create a save button to save the text file
save_button = PushButton(file_controls, text="Save", command=save_file, align="right")

# Create an open button to open the text file
open_button = PushButton(file_controls, text="Open", command=open_file, align="right")

# Create a separate text box / container for the editor
editor = TextBox(app, multiline=True, height="fill", width="fill")

# Display the GUI
app.display()
