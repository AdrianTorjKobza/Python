# Import the GUI widgets from guizero
from guizero import App, TextBox, PushButton, Text, info

# Create the app for the program
app = App()

# Check if the user pass match, when the button is clicked
def btn_pass_clicked():
    # Check if pass was inserted
    if txt_pass1.value == "" or txt_pass2.value == "":
        info("NOK", "Please insert pass")
    else:
        if txt_pass1.value == txt_pass2.value:
            info("OK", "Pass match")
        else:
            info("NOK", "Pass do not match. Try again!")

# Display GUI widgets for the first text box and hide the pass
lbl_pass1 = Text(app, text="Insert pass")
txt_pass1 = TextBox(app, hide_text=True)

# Display GUI widgets for the second text box and hide the pass
lbl_pass2 = Text(app, text="Repeat pass")
txt_pass2 = TextBox(app, hide_text=True)

# Call the function 'btn_pass_clicked" when button is clicked
btn_pass = PushButton(app, command=btn_pass_clicked, text="Check")

# Show the GUI on the screen
app.display()
