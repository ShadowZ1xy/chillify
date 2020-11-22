# PyInstaller commands


### Chillify
```shell
$ pyinstaller --noconfirm --onedir --windowed
    --icon "path/to/chillify/icon.ico"
    --name "chillify"
    --add-data "path/to/chillify/hints.json;."
    --add-data "path/to/chillify/icon.ico;." 
    "path/to/chillify/chillify_main.py"
```

### Settings
```shell
$ pyinstaller --noconfirm --onedir --windowed
    --icon "path/to/settings/icon.ico"
    --name "settings"
    --add-data "path/to/settings/icon.ico;." 
    "path/to/settings/settings_main.py"
```
