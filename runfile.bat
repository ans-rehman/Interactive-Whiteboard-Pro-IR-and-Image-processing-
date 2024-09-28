@echo off
REM Replace "your_virtualenv_name" with the name of your virtual environment
call .\virtual-env\Scripts\activate

REM Replace "python_script.py" with the path to your Python script
python -u "IntractoVision\wi_prt.py"

REM Deactivate the virtual environment after running the script
deactivate

pause