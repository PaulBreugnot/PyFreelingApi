from pyFreelingApi import LINUX_API_PATH
import os
if "LD_LIBRARY_PATH" not in os.environ.keys:
    os.environ["LD_LIBRARY_PATH"] = "/usr/local/share/freeling/APIs/python3/"
else:
    os.environ["LD_LIBRARY_PATH"] += "/usr/local/share/freeling/APIs/python3/"

os.putenv("LD_LIBRARY_PATH", os.environ["LD_LIBRARY_PATH"])
# _pyfreeling_source = open("/usr/local/share/freeling/APIs/python3/_pyfreeling.so", mode="rb")
# _pyfreeling_target = open(LINUX_API_PATH, mode="w+b")
# _pyfreeling_target.write(_pyfreeling_source.read())

