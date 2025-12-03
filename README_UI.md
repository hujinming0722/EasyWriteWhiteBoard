# Qt UI Files for EasyWriteWhiteBoard

This project includes Qt UI files that can be edited with Qt Designer. 

## Files Description

1. `ui/mainui.ui` - Main UI layout file that can be opened with Qt Designer
2. `ui/resources.qrc` - Resource file containing icon definitions
3. `ui/resources_rc.py` - Compiled resource file for Python integration
4. `ui/Ui_mainui.py` - Generated Python class from the UI file
5. `test_ui.py` - Test script to validate the UI
6. `launch_designer.py` - Script to launch Qt Designer with the UI file

## Editing with Qt Designer

To edit the UI with Qt Designer:

1. Run the launch script:
   ```bash
   python launch_designer.py
   ```
   Or manually open Qt Designer and load the UI file.

2. Open `ui/mainui.ui` file in Qt Designer
3. Make your desired changes
4. Save the file
5. Regenerate the Python class:
   ```bash
   pyside6-uic ui/mainui.ui -o ui/Ui_mainui.py
   ```
6. If you modified resources, recompile them:
   ```bash
   pyside6-rcc ui/resources.qrc -o ui/resources_rc.py
   ```

## Icons Used

All icons are stored in the `ui/icons/` folder:
- pen.png: Pen tool
- arrow.png: Line tool
- correction.png: Rectangle tool
- settings.png: Circle tool
- save.png: Ellipse tool
- eraser.png: Eraser tool
- minimize.png: PPT navigation buttons
- exit.png: Exit button

## Testing Changes

To test any UI changes:

```bash
python test_ui.py
```

This will open a window showing the current UI layout.