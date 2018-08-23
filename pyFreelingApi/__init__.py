import importlib
import platform
import sys
import os

LINUX_INSTALLATION_PATH = "/usr/local/"
WINDOWS_INSTALLATION_PATH = "C:\\Freeling\\freeling\\"

if platform.system() == "Windows":
    INSTALLATION_PATH = WINDOWS_INSTALLATION_PATH

elif platform.system() == "Linux":
    INSTALLATION_PATH = LINUX_INSTALLATION_PATH

sys.path.append(os.path.join(INSTALLATION_PATH, "share", "freeling", "APIs", "python3"))

freeling_api = importlib.import_module("pyfreeling")
