# PyFreelingApi
Freeling 4.1 Python APIs

For more information about Freeling, see :
http://nlp.lsi.upc.edu/freeling/index.php/node/1

## Content
This repository contains built Python APIs for Freeling, built following this procedure : https://talp-upc.gitbooks.io/freeling-4-1-user-manual/content/installation/apis-windows.html

Notice that this project is not an official Freeling project.

The Python package contains APIs for Linux systems and Windows *(for now, still in development...)*.

## Use

Once installed, you can use the Freeling Python API from your Python programs ([official Freeling examples] (https://talp-upc.gitbooks.io/freeling-tutorial/content/)) replacing `import freeling` by the following import :
```
from pyFreelingAPI import freeling_api as freeling
```
The script determines by itself what is the good API to use according to your plateform.

## Install Freeling and its Python API for Windows x64

- Install Python Package (this repository):
```
pip install git+https://github.com/PaulBreugnot/PyFreelingApi
```

**Notice that only install this won't make you able to use Freeling, even if you can now import the module from your Python programs!**

- Install pre-compiled Freeling binary from https://sourceforge.net/projects/loacore/files/Freeling/ *(for now, only Windows x64)*

Once downloaded, unzip the file, and run the `install.bat` file. By default, this will install Freeling in the folder `C:\Freeling\`.

If you want to install Freeling in an other directory, you can run `install.bat` from `cmd.exe`. After running `cmd.exe`, `cd` to the folder where you unzipped the files, and specify your installation folder as follow :
```
install "C:\your\installation\folder\"
```
Then, Freeling will be installed in `C:\your\installation\folder\Freeling\`.

**During the process, an hard link linking `C:\Freeling\` to `C:\your\installation\folder\Freeling\` will be created. Notice that without it, your Freeling API won't work.**

If prefer you can perform this process manually, following instructions in the `README.txt` in the downloaded zip.
