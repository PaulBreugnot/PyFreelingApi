import importlib
import platform
import pyFreelingApi.windows_api as win_api
import pyFreelingApi.linux_api as lin_api

if platform.system() == "Windows":
    freeling_api = win_api

elif platform.system() == "Linux":
    freeling_api = lin_api
