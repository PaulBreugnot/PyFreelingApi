import importlib
import platform

if platform.system() == "Windows":
    freeling_api = importlib.import_module("windows_api.pyfreeling")

elif platform.system() == "Linux":
    freeling_api = importlib.import_module("windows_api.pyfreeling")
