# Website Blocker

## Overview
This is a Python-based application that allows users to block and unblock websites on their local machine. It modifies the `hosts` file to redirect the specified websites to `127.0.0.1`, effectively blocking access to those websites.

The application features a graphical user interface (GUI) built using the `tkinter` library, making it easy for users to input websites and manage their blocked list.

## Features
- Block websites by adding them to the `hosts` file.
- Unblock websites by removing their entries from the `hosts` file.
- Simple GUI for easy interaction.
- Requires administrator permissions to modify the `hosts` file.

## Requirements
- Python 3.x
- `tkinter` (included with Python standard library)
- Administrator permissions

## How to Run
1. Ensure you have Python installed on your system.
2. Download or clone this repository to your local machine.
3. Run the script with administrator privileges:
   ```bash
   python path_to_script.py
   ```

## Usage
1. **Block Websites**: Enter the URLs of the websites you want to block in the input field, separated by commas, and click the "Block Website" button.
2. **Unblock Websites**: Enter the URLs of the websites you want to unblock in the input field, separated by commas, and click the "Unblock Website" button.
3. **Exit**: Click the "Exit" button to close the application.

## Note
- Make sure to close your web browser before blocking or unblocking websites for the changes to take effect.
- The application modifies the `hosts` file located at `C:\Windows\System32\drivers\etc\hosts`. Any changes made to the file can affect your network behavior. Use this application responsibly.

## Known Issues
- The script may not work on non-Windows systems as the path to the `hosts` file is specific to Windows.
- Administrator permissions are required to modify the `hosts` file. If the application is not run as an administrator, it will automatically attempt to restart itself with elevated privileges.

## Contributing
Feel free to fork this repository, open issues, and submit pull requests to contribute to the project.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
