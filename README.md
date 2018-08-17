# PyFreelingApi
Freeling 4.1 Python 3 APIs

## Presentation
If you want to use Freeling 4.1 with Python API, you currently need to build it from source as described in the [Freeling Documentation](https://talp-upc.gitbooks.io/freeling-4-1-user-manual/).
However, this procedure can be quite complex and reserved for advanced users. The global objective of this project is to provide already built Freeling binaries with Python 3 APIs to quickly get Freeling Python 3 APIs to work thanks to a platform independent interface.

This repository **only contains Python 3 APIs** for Freeling 4.1 built following the procedures described in the [Freeling Documentation](https://talp-upc.gitbooks.io/freeling-4-1-user-manual/).
Freeling 4.1 binaries can then be found there : https://sourceforge.net/projects/loacore/files/
The reason for that are :
  - Using GitHub allows to install all needed Python modules using [pip](https://pip.pypa.io/en/stable/)
  - Freeling binaries are too heavy for GitHub repositories.
  - This package can be cross-platform thanks to Python tricks, however Freeling is highly platfrom dependent, and so the Freeling installation, even from pre-compiled binaries, needs to be an external process (that we also try to make as simple as possible).

**Notice that this project is not an official Freeling project.**

*For now, the installed Python package contains APIs for Linux and Windows systems. Still in test/development...*.

For more information about Freeling, see :
http://nlp.lsi.upc.edu/freeling/index.php/node/1

## Use

Once installed, you can use the Freeling Python API from your Python programs ([official Freeling examples] (https://talp-upc.gitbooks.io/freeling-tutorial/content/)) replacing `import freeling` by the following import :
```python
from pyFreelingAPI import freeling_api as freeling
```
The script determines by itself what is the good API to use according to your platform.

## Install Freeling and its Python API for Windows x64

- Install Python Package (this repository):
```
pip install git+https://github.com/PaulBreugnot/PyFreelingApi
```

**Notice that only install this won't make you able to use Freeling, even if you can now import the module from your Python programs!**

- Download pre-compiled Freeling binary from https://sourceforge.net/projects/loacore/files/Freeling/ *(for now, only Windows x64)*

Once downloaded, unzip the file, and run the `install.bat` file. By default, this will install Freeling in the folder `C:\Freeling\`.

If you want to install Freeling in an other directory, you can run `install.bat` from `cmd.exe`. After running `cmd.exe`, `cd` to the folder where you unzipped the files, and specify your installation folder as follow :
```
install "C:\your\installation\folder\"
```
Then, Freeling will be installed in `C:\your\installation\folder\Freeling\`.

**During the process, an hard link linking `C:\Freeling\` to `C:\your\installation\folder\Freeling\` will be created. Notice that without it, your Freeling API won't work.**

If prefer you can perform this process manually, following instructions in the `README.txt` in the downloaded zip.
