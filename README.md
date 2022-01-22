# Upgrade All Python Packages
Script which upgrades `pip` and all other outdated python packages. Written for Python `3.x`.
<br><br>

### Usage
Run the following command in the console:
```
python upgrade_all_py_packages.py
```
If everything is working, the output should look like this:
```
>> Python version = 3.10.0.final.0
-----------------------------------------
>> Upgrading pip ... Requirement already satisfied: pip in lib\site-packages (21.2.1)
Collecting pip
  Using cached pip-21.3.1-py3-none-any.whl (1.7 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.1
    Uninstalling pip-21.2.1:
      Successfully uninstalled pip-21.2.1
Successfully installed pip-21.3.1
-----------------------------------------
>> Collecting outdated Python packages ... found 2
>> Upgrading 1/2: 'anyio'
- - - - - - - - - - - - - - - - - - - - -
Collecting anyio
  Using cached anyio-3.5.0-py3-none-any.whl (79 kB)
Installing collected packages: anyio
  Attempting uninstall: anyio
    Found existing installation: anyio 3.4.0
    Uninstalling anyio-3.4.0:
      Successfully uninstalled anyio-3.4.0
Successfully installed anyio-3.5.0
-----------------------------------------
>> Upgrading 2/2: 'terminado'
- - - - - - - - - - - - - - - - - - - - -
Collecting terminado
  Downloading terminado-0.12.1-py3-none-any.whl (15 kB)
Installing collected packages: terminado
  Attempting uninstall: terminado
    Found existing installation: terminado 0.12.0
    Uninstalling terminado-0.12.0:
      Successfully uninstalled terminado-0.12.0
Successfully installed terminado-0.12.1
```


