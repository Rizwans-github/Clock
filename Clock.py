import tkinter as tk
from time import strftime, strptime
import inflect

def time_to_words(hour, minute, second, am_pm):
    p = inflect.engine()
    hour_words = p.number_to_words(hour % 12) if hour % 12 != 0 else p.number_to_words(12)
    minute_words = p.number_to_words(minute)
    second_words = p.number_to_words(second)
    am_pm_str = 'AM' if am_pm == 0 else 'PM'
    am_pm_words = p.unit("o'clock", am_pm_str.lower()) if minute == 0 and second == 0 else am_pm_str.lower()

    return f"{hour_words} {minute_words} {second_words} {am_pm_words}"

def update_time():
    current_time = strftime('%I:%M:%S %p')  # Using %I for 12-hour format
    # Split the time into components (hour, minute, second, am_pm)
    time_components = time_to_words(*strptime(current_time, '%I:%M:%S %p')[3:7])

    # Set colors for hour, minute, second
    hour_color = '#df5242'
    minute_color = '#329ddb'
    second_color = 'blue'
    am_color = 'purple'

    label.config(state="normal")  # Enable text widget for editing
    label.delete("1.0", "end")  # Clear the existing text

    # Add heading for the hour hand
    label.insert("1.0", "For i in hour hand: ")

    # Insert new text
    label.insert("end", time_components)

    # Apply colors to different parts of the text
    label.tag_configure('hour', foreground=hour_color)
    label.tag_configure('minute', foreground=minute_color)
    label.tag_configure('second', foreground=second_color)
    label.tag_configure('am', foreground=am_color)

    label.tag_add('hour', '1.18', '1.end')  # Apply color to the hour component
    label.tag_add('minute', '1.end+1c', '1.end+3c')
    label.tag_add('second', '1.end+4c', '1.end+6c')
    label.tag_add('am', '1.end+7c', '1.end+9c')

    label.config(state="disabled")  # Disable text widget for readonly

    label.after(1000, update_time)

# Create the main application window
app = tk.Tk()
app.title("Improved Clock Widget")
app.geometry("7  00x80")  # Set the initial size of the window

# Create and configure the text widget for displaying the time
label = tk.Text(app, font=('Helvetica', 20, 'bold'), background=None, wrap="none", height=1, state="disabled")
label.pack(pady=20)  # Add padding

# Call the update_time function to initialize and start updating the time
update_time()

# Start the main event loop
app.mainloop()

