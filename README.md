# HEIC Converter

This is a simple Python GUI app I built to make converting HEIC images easier. With this tool, you can batch-convert HEIC files in a selected folder to either JPEG or PNG, plus have the option to delete the original HEIC files once they’re converted. It’s a quick way to manage image conversions without needing extra software.

## Features
- **Batch Conversion**: Choose an entire folder to convert all `.heic` files to JPEG or PNG at once.
- **File Management**: Optionally delete original `.heic` files automatically after conversion.
- **User-Friendly GUI**: Includes a format selection dropdown, start button, and live log showing each file’s status as it converts.

## How to Use
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/CameronTomczyk/HEIC-to-JPEG-or-PNG-Converter.git
   ```
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the program:
   ```
   python heic_converter.py
   ```

### Tech Details
- **Python**
- **tkinter** for the GUI
- **Pillow and pillow-heif** for handling HEIC to JPEG/PNG conversion

## Screenshots

**Main Interface**  
![Main Interface](screenshots/main_interface.png)

**Folder Selection**  
![Folder Selection](screenshots/folder_selection.png)


Let me know what you think, or feel free to fork it and add more functionality!
