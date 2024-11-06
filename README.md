
# HEIC Converter

This tool is especially useful if you use an iPhone with Windows, as all iPhone photos are imported as `.heic` files. 
I created this to make it easier and faster to transfer photos from my phone to Windows for platforms like eBay or Facebook Marketplace.

This is a simple Python GUI app I built to make converting HEIC images easier. With this tool, you can batch-convert HEIC files in a selected folder to either JPEG or PNG, plus have the option to delete the original HEIC files once they’re converted. It’s a quick way to manage image conversions without needing extra software.

**HEIC Conversion Tool Interface**  
![HEIC Conversion Tool Screenshot](screenshots/HEIC%20Conversion%20Tool%20Screenshot.png)

## Features
- **Batch Conversion**: Choose an entire folder to convert all `.heic` files to JPEG or PNG at once.
- **File Management**: Optionally delete original `.heic` files automatically after conversion.
- **User-Friendly GUI**: Includes a format selection dropdown, start button, and live log showing each file’s status as it converts.

## Setup and Usage

### Step-by-Step Instructions
1. **Clone the repository** to your local machine and navigate into the project folder:
   ```bash
   git clone https://github.com/CameronTomczyk/HEIC-to-JPEG-or-PNG-Converter.git
   cd HEIC-to-JPEG-or-PNG-Converter
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the program**:
   ```bash
   python heic_converter.py
   ```

### Quick Start: All-in-One Script
To clone the repository, install dependencies, and run the program in one go, you can use this single script:
```bash
git clone https://github.com/CameronTomczyk/HEIC-to-JPEG-or-PNG-Converter.git
cd HEIC-to-JPEG-or-PNG-Converter
pip install -r requirements.txt
python heic_converter.py
```

### Tech Details
- **Python**
- **tkinter** for the GUI
- **Pillow and pillow-heif** for handling HEIC to JPEG/PNG conversion

---

Let me know what you think, or feel free to fork it and add more functionality! Working on an EXE.
