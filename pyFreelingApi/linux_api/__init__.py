from pyFreelingApi import LINUX_API_PATH

_pyfreeling_source = open("/usr/local/share/freeling/APIs/python3/_pyfreeling.so", mode="rb")
_pyfreeling_target = open(LINUX_API_PATH, mode="w+b")
_pyfreeling_target.write(_pyfreeling_source.read())

