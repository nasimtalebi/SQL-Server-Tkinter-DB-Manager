Create Shortcut on Desktop:

Reinstall PyInstaller:
1.	Open a command prompt.
2.	Install PyInstaller using pip:
pip install  pyinstaller

Add PyInstaller to PATH:
1.	Find the directory where PyInstaller is installed. It's usually located in the Scripts directory of your Python installation.
2.	Open Control Panel -> System and Security -> System -> Advanced system settings -> Environment Variables.
3.	Under System Variables, find the PATH variable and click Edit.
4.	Add the directory containing PyInstaller to the list of paths. If PyInstaller is installed in the Scripts directory of your Python installation, the path to add would be something like


Run PyInstaller Command :
pyinstaller --onefile "C:\Users\admin.nasim\Desktop\Auto Creat & insert indexbase.ipynb"


C:\Users\admin.nasim\dist
----------------------------------------------------

1. Locate the Executable:
   •	After running PyInstaller, it creates a standalone executable file for your Jupyter Notebook. This file is typically located in a directory named dist within your project folder.
•	Open File Explorer (Windows) or Finder (macOS) and navigate to the directory where your Jupyter Notebook project is located.
•	Look for a folder named dist. Inside this folder, you should find your standalone executable file. It will have the same name as your Jupyter Notebook file but without the .ipynb extension.

2. Create Shortcut on Desktop:
For Windows:
•	Once you've located the executable file:
•	Right-click on the executable file.
•	In the context menu, hover over the "Send to" option.
•	In the submenu that appears, select "Desktop (create shortcut)".

For macOS:
•	Once you've located the executable file:
•	Hold down the Option key on your keyboard.
•	Drag the executable file to your desktop while holding down the Option key. This will create an alias (shortcut) on your desktop.

For Linux:
•	The method for creating shortcuts on Linux desktop environments may vary depending on your desktop environment (e.g., GNOME, KDE, etc.).
•	Typically, you can right-click on the desktop and select an option to create a new shortcut or launcher. The exact steps may vary depending on your Linux distribution and desktop environment.

3. Customize Shortcut Icon (Optional):
   •	Once the shortcut is created on your desktop:
•	Right-click on the shortcut icon.
•	Select "Properties" from the context menu. This will open the Properties window for the shortcut.
•	In the Properties window, navigate to the "Shortcut" tab (or similar).
•	Look for an option labeled "Change Icon" or "Icon". Click on it.
•	Choose an icon for your shortcut from the available options, or browse for an icon file (.ico on Windows, .icns on macOS, .png on Linux) on your system.
•	After selecting the icon, click OK to save the changes.

By following these steps, you'll be able to create a shortcut for your standalone executable on your desktop and customize its icon if desired. Let me know if you need further clarification on any step!









pip install pyodbc
pip install pyxlsb
pip install  pyinstaller
pyinstaller --onefile "C:\Users\admin.nasim\Desktop\Auto Creat&insert indexbase.ipynb
