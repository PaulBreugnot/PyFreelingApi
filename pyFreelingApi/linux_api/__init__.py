_pyfreeling_source = open("/usr/local/share/freeling/APIs/python3/_pyfreeling.so", mode="rb")
_pyfreeling_target = open("linux_api/_pyfreeling.so", mode="w+b")
_pyfreeling_target.write(_pyfreeling_source.read())

