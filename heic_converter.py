# Doing my best to explain what is going on here in the comments
#haven't made any code for public release and also am trying to get better with different libraries in Python. Thanks!

# Import necessary libraries
import os  # for handling file directories
from tkinter import Tk, Button, Label, filedialog, Checkbutton, IntVar, Text, Scrollbar, END, RIGHT, Y, Frame, StringVar, OptionMenu  # for GUI
from PIL import Image  # for image processing
import pillow_heif  # for handling HEIC format images

# Function to handle HEIC to JPEG/PNG conversion
def convert_heic(folder_path, delete_originals, format_choice):
    # Clear the log box at the start of each conversion for fresh logs
    log_box.delete(1.0, END)
    
    # If no folder is selected, log an error and exit function
    if not folder_path:
        log_box.insert(END, "Please select a folder.\n")
        return

    # Loop over each file in the selected folder
    for filename in os.listdir(folder_path):
        # Only proceed with files that have a .heic extension
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(folder_path, filename)  # Full path to each HEIC file
            
            try:
                # Read the HEIC image
                heif_image = pillow_heif.open_heif(heic_path)
                
                # Convert HEIC image to a Pillow Image object
                image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data)
                
                # Set the output path with the appropriate file extension based on format choice
                output_ext = "jpg" if format_choice.get() == "JPEG" else "png"
                output_path = os.path.join(folder_path, f"{filename.rsplit('.', 1)[0]}.{output_ext}")
                
                # Save the converted image in the selected format
                image.save(output_path, format_choice.get())
                log_box.insert(END, f"Converted {filename} to {format_choice.get()}.\n")
                
                # If delete_originals checkbox is selected, delete the original HEIC file after conversion
                if delete_originals.get() == 1:
                    os.remove(heic_path)
                    log_box.insert(END, f"Deleted original HEIC file: {filename}\n")
            except Exception as e:
                # Log any error that occurs during conversion for this file
                log_box.insert(END, f"Failed to convert {filename}: {e}\n")
    
    # Log completion message after all conversions are done
    log_box.insert(END, "Conversion complete!\n")

# Function to select a folder containing HEIC files
def select_folder():
    global folder_path  # Declare folder_path as global to access it across functions
    folder_path = filedialog.askdirectory()  # Open folder selection dialog
    if folder_path:
        status_label.config(text=f"Selected Folder: {folder_path}")  # Update status label with chosen path
        log_box.insert(END, f"Folder selected: {folder_path}\n")

# Function to start the conversion process
def start_conversion():
    if folder_path:
        log_box.insert(END, "Starting conversion...\n")  # Log starting message
        convert_heic(folder_path, delete_originals, format_choice)  # Call the conversion function
    else:
        log_box.insert(END, "Please select a folder first.\n")  # Log error if no folder is selected

# Set up the main window (Tkinter root)
root = Tk()
root.title("HEIC to JPEG/PNG Converter")  # Title for the GUI window
root.geometry("500x450")  # Window size

# Label and button for folder selection
Label(root, text="Select the folder containing HEIC files:").pack(pady=10)
Button(root, text="Select Folder", command=select_folder).pack(pady=5)

# Dropdown menu to select output format (JPEG or PNG)
format_choice = StringVar(value="JPEG")  # Default format is JPEG
Label(root, text="Choose output format:").pack(pady=5)
OptionMenu(root, format_choice, "JPEG", "PNG").pack(pady=5)

# Checkbox for choosing whether to delete original HEIC files after conversion
delete_originals = IntVar()  # 1 if checked, 0 if unchecked
Checkbutton(root, text="Delete original HEIC files after conversion", variable=delete_originals).pack(pady=5)

# Start button to initiate the conversion process
Button(root, text="Start Conversion", command=start_conversion).pack(pady=5)

# Status label to display the selected folder path
status_label = Label(root, text="No folder selected.")
status_label.pack(pady=5)

# Frame for the log box and scrollbar (for displaying conversion progress)
log_frame = Frame(root)
log_frame.pack(pady=10, fill="both", expand=True)

# Text box to show log messages during conversion
log_box = Text(log_frame, wrap="word", height=10)
log_box.pack(side="left", fill="both", expand=True)

# Scrollbar for the log box to manage longer logs
scrollbar = Scrollbar(log_frame, command=log_box.yview)
scrollbar.pack(side=RIGHT, fill=Y)
log_box.config(yscrollcommand=scrollbar.set)

# Run the GUI main loop
root.mainloop()
