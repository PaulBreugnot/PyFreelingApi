import importlib
import platform
import os
LINUX_API_PATH = os.path.abspath(os.path.join(".", "linux_api", "_pyfreeling.so"))

if platform.system() == "Windows":
    freeling_api = importlib.import_module("pyFreelingApi.windows_api.pyfreeling")

elif platform.system() == "Linux":
    freeling_api = importlib.import_module("pyFreelingApi.linux_api.pyfreeling")
