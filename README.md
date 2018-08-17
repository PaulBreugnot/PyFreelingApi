# PyFreeling
Freeling Python APIs

http://nlp.lsi.upc.edu/freeling/index.php/node/1

Only this package **won't make you able to use Freeling!**

## Install Freeling Python API for Windows x64

- Install Python Package :
```
pip install git+https://github.com/PaulBreugnot/PyFreelingApi
```
- Install pre-compiled Freeling binary from https://sourceforge.net/projects/loacore/files/Freeling/ *(for now, only Windows x64)*
Once downloaded, unzip the file, and run the `install.bat` file. By default, this will install Freeling in the folder `C:\Freeling\`.
If you want to install Freeling in an other directory, you can run `install.bat` from `cmd.exe`. After running `cmd.exe`, `cd` to the folder where you unzipped the files, and specify your installation folder as follow :
```
install "C:\your\installation\folder\"
```
Then, Freeling will be installed in `C:\your\installation\folder\Freeling\`.
<Warning>
  During the process, an hard link linking `C:\Freeling\` to `C:\your\installation\folder\Freeling\` will be created. **Notice that without it, your Freeling API won't work.**
</Warning>
