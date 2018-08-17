import os
print("Set Windows environment variables...")
os.environ["PATH"] += \
    ";C:\\Freeling\\freeling\\bin;" \
    "C:\\Freeling\\dependencies\\boost\\lib;"\
    "C:\\Freeling\\dependencies\\zlib\\bin;"\
    "C:\\Freeling\\dependencies\\icu\\bin64"

os.putenv("PATH",
          os.environ["path"])
