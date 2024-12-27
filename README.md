# Stream Deck Python Controller - Windows Setup Guide

This guide will help you set up a Python environment and run the Stream Deck controller script on Windows, even if you're new to Python.

## Prerequisites

You'll need administrative rights on your computer to install Python and the required packages.

## Step-by-Step Installation

### 1. Install Python

1. Visit the official Python website: https://www.python.org/downloads/
2. Click the big yellow "Download Python" button (get the latest version)
3. Run the downloaded installer
4. **IMPORTANT**: Check the box that says "Add Python to PATH" during installation
5. Click "Install Now"

To verify Python is installed:
1. Open Command Prompt (press Win + R, type `cmd`, press Enter)
2. Type `python --version`
3. You should see something like `Python 3.x.x`

### 2. Install Required Packages

1. Open Command Prompt as Administrator:
   - Press Win + X
   - Click "Windows Terminal (Admin)" or "Command Prompt (Admin)"
   
2. Install the required packages by typing:
```bash
pip install hidapi pillow
```

### 3. Set Up the Script

1. Create a new folder somewhere easy to find (e.g., on your Desktop) called `streamdeck-controller`

2. Save the Python script (the code from the previous message) as `streamdeck.py` in this folder

3. To run the script:
   - Open Command Prompt
   - Navigate to your folder (replace PATH with your actual path):
     ```bash
     cd PATH\streamdeck-controller
     ```
   - Run the script:
     ```bash
     python streamdeck.py
     ```

## Troubleshooting

### "Python is not recognized as an internal or external command"
- Solution: Restart your computer after installing Python
- If still not working: Manually add Python to PATH
  1. Search for "Environment Variables" in Windows
  2. Click "Environment Variables"
  3. Under "System Variables", find "Path"
  4. Click "Edit" → "New"
  5. Add the Python installation path (typically `C:\Users\YourUsername\AppData\Local\Programs\Python\Python3x\`)

### "No module named 'hid'"
- Try running:
  ```bash
  pip uninstall hidapi
  pip install hidapi
  ```

### "Unable to connect to Stream Deck"
1. Ensure no other Stream Deck software is running
2. Try unplugging and replugging your Stream Deck
3. If still not working, we may need to find your specific device ID:
   ```python
   import hid
   for device in hid.enumerate():
       print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")
   ```
   Run this code and look for your Stream Deck in the list

## Next Steps

Once everything is working:
1. Press the first key on your Stream Deck
2. You should see "Hello World!" printed in the Command Prompt
3. To exit the program, press Ctrl+C in the Command Prompt

## Additional Notes

- Keep the Command Prompt window open while the script is running
- The script needs to be run each time you want to use your custom Stream Deck controls
- You can modify the script to change what each key does
- Consider creating a batch file (.bat) to make running the script easier

Need help? Feel free to ask for clarification on any step!
