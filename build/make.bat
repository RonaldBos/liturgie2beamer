@rem http://irwinkwan.com/2013/04/29/python-executables-pyinstaller-and-a-48-hour-game-design-compo/

@rem python PyInstaller-2.1\pyinstaller.py --onefile ..\python\gui.py
python PyInstaller-2.1\pyinstaller.py liturgie2beamer.spec
copy dist\liturgie2beamer.exe ..\windows\

pause
