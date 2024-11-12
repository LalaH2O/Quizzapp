import tkinter as tk
import threading
import settings

# Global variable to coordinate input
waitforinput = threading.Event()
input_value = None

# Color variables
bg_color = settings.gui_bg_color
text_color = settings.gui_text_color
button_bg_color = settings.button_bg_color
button_text_color = settings.button_text_color

def exit_and_help_button_add(window, help=0):
    button = tk.Button(window, text='Exit', command=exit, bg=button_bg_color, fg=button_text_color)
    button.pack()

    if help == 0:
        button2 = tk.Button(window, text='Help', command=show_help, bg=button_bg_color, fg=button_text_color)
        button2.pack()

def show_help():
    popup_main(settings.proces_name, settings.help, help=1)

def popup_main(name, text, time=0, help=0):
    print(text)
    amauntofbsn = 5
    amountofchars = len(str(text))
    x = amountofchars * 10
    if x < 200:
        x = 200
    y = amauntofbsn * 5
    if y < 100:
        y = 100
    open_window(x, y, text, name, time, help)

def input_question(name, question):
    create_input_field(name, question)  # Call function directly in the main thread
    waitforinput.wait()  # Wait until input is received
    waitforinput.clear()  # Reset the event
    return input_value  # Return the input value after it's received

def open_window_backend_threading(x, y, text, name, t, help):
    root = tk.Tk()  # Create the root window
    root.title(name)
    root.configure(background=bg_color)
    label = tk.Label(root, text=text, font=text_color)
    label.pack()
    root.geometry(str(x) + 'x' + str(y) + '+' + str(settings.window_position_x) + '+' + str(settings.window_position_y))
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    w = 200
    h = 100
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry('+%d+%d'%(x,y))
    root.minsize(200, 100)
    if t != 0:
        root.after(t)

    exit_and_help_button_add(root, help)

    def close_win():
        root.destroy()

    conb = tk.Button(root, text='Continue', command=close_win, bg=button_bg_color, fg=button_text_color)
    conb.pack()

    root.mainloop()                             

def open_window(x, y, text, name, t, help):
    open_window_backend_threading(x, y, text, name, t, help)

def create_input_field(name, question):
    global waitforinput
    global input_value

    def get_input():
        global input_value
        input_value = entry.get()
        print(input_value)
        waitforinput.set()  # Set the event to signal input received

    def close_win():
        window.destroy()

    # Create a Tkinter window
    window = tk.Tk()
    window.title(name)
    window.configure(background=bg_color)
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    w = 200
    h = 100
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    window.geometry('+%d+%d'%(x,y))
    window.minsize(200, 100)

    # Create a label
    label = tk.Label(window, text=question, font=text_color)
    label.pack()

    # Create an entry widget
    entry = tk.Entry(window, bg=bg_color)
    entry.pack()

    # Create a button to get the input value
    button_bg_color = bg_color
    button_text_color = text_color
    button = tk.Button(window, text='Submit', command=lambda: [get_input(), close_win()], bg=button_bg_color, fg=button_text_color)
    button.pack()

    exit_and_help_button_add(window)

    # Run the Tkinter event loop
    window.mainloop()

    return input_value

def multiple_choice_3(q, _1, _2, _3):
    window = tk.Tk()
    window.configure(background=bg_color)
    window.title("Multiple Choice")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    w = 200
    h = 150
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('+%d+%d' % (x, y))
    window.minsize(200, 150)

    # Create a label
    label = tk.Label(window, text=q, bg=bg_color, fg=text_color)
    label.pack()

    # Define a variable to hold the selected choice
    v = tk.IntVar()

    # Function to handle submission
    def submit():
        window.destroy()

    # Create Radiobuttons
    tk.Radiobutton(window, text=_1, padx=20, variable=v, value=1, bg=bg_color, fg=text_color).pack(anchor=tk.W)
    tk.Radiobutton(window, text=_2, padx=20, variable=v, value=2, bg=bg_color, fg=text_color).pack(anchor=tk.W)
    tk.Radiobutton(window, text=_3, padx=20, variable=v, value=3, bg=bg_color, fg=text_color).pack(anchor=tk.W)

    # Submit button
    button_bg_color = bg_color
    button_text_color = text_color
    submit_button = tk.Button(window, text="Submit", command=submit, bg=button_bg_color, fg=button_text_color)
    submit_button.pack()

    exit_and_help_button_add(window)

    window.mainloop()

    # Return the selected value after window is destroyed
    return v.get()

def multiple_choice_2(q, _1, _2):
    window = tk.Tk()
    window.configure(background=bg_color)
    window.title(settings.proces_name)
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    w = 200
    h = 150
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('+%d+%d' % (x, y))
    window.minsize(200, 150)

    # Create a label
    label = tk.Label(window, text=q, bg=bg_color, fg=text_color)
    label.pack()

    # Define a variable to hold the selected choice
    v = tk.IntVar()

    # Function to handle submission
    def submit():
        window.destroy()

    # Create Radiobuttons
    tk.Radiobutton(window, text=_1, padx=20, variable=v, value=1, bg=bg_color, fg=text_color).pack(anchor=tk.W)
    tk.Radiobutton(window, text=_2, padx=20, variable=v, value=2, bg=bg_color, fg=text_color).pack(anchor=tk.W)

    # Submit button
    button_bg_color = bg_color
    button_text_color = text_color
    submit_button = tk.Button(window, text="Submit", command=submit, bg=button_bg_color, fg=button_text_color)
    submit_button.pack()

    exit_and_help_button_add(window)

    window.mainloop()

    # Return the selected value after window is destroyed
    return v.get()

def multiple_choice(q, arr): #Nur noch die verwenden!
    window = tk.Tk()
    window.configure(background=bg_color)
    window.title("Multiple Choice")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    w = 200
    h = 150
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('+%d+%d' % (x, y))
    window.minsize(200, 150)

    # Create a label
    label = tk.Label(window, text=q, bg=bg_color, fg=text_color)
    label.pack()

    # Define a variable to hold the selected choice
    v = tk.IntVar()

    # Function to handle submission
    def submit():
        window.destroy()

    # Create Radiobuttons
    for i in range(len(arr)):
        tk.Radiobutton(window, text=arr[i], padx=20, variable=v, value=i, bg=bg_color, fg=text_color).pack(anchor=tk.W)

    # Submit button
    button_bg_color = bg_color
    button_text_color = text_color
    submit_button = tk.Button(window, text="Submit", command=submit, bg=button_bg_color, fg=button_text_color)
    submit_button.pack()

    exit_and_help_button_add(window)

    window.mainloop()

    # Return the selected value after window is destroyed
    return v.get()

def indexcards_ui(arr):
    global indexcards_temp
    window = tk.Tk()
    window.configure(background=bg_color)
    window.title("Index Cards")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    w = 200
    h = 150
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('+%d+%d' % (x, y))
    window.minsize(200, 150)
    indexcards_temp = 0

    def flip():
        global indexcards_temp

        if indexcards_temp == 0:
            indexcards_temp += 1
        else:
            indexcards_temp -= 1
        label.configure(text=arr[indexcards_temp])
        window.update()

    def continue_func():
        window.destroy()

    # Create a label
    label = tk.Label(window, text=arr, bg=bg_color, fg=text_color)
    label.pack()

    flip = tk.Button(window, text="Flip", command=flip, bg=bg_color, fg=text_color)
    flip.pack()

    continue_button = tk.Button(window, text="Continue", command=continue_func, bg=bg_color, fg=text_color)
    continue_button.pack()

    exit_and_help_button_add(window)

    window.mainloop()