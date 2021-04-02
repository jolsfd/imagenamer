# ImageNamer

## Requirements

Python 3.7 or higher installed.

## Setup

Extract folder from .zip file into your favorite directory.
Run this options for installing the required libaries.

Your structure should look like this:

```bash
.
├── imagenamer.ps1
├── imagenamer.sh
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
├── settings
│   └── git_dummy
├── setup
│   ├── setup.ps1
│   └── setup.sh
└── src
    ├── menu.py
    ├── rename.py
    └── settings.py
```

### Windows

Open Powershell and navigate to the imagenamer folder and execute the **setup.ps1** file.

Or run followed command:

```
py.exe -m pip install -r requirements.txt
```

### Linux

Navigate into the imagenamer folder and execute the **setup.sh** file in the setup folder.

Or run followed command:

```
python3 -m pip install -r requirements.txt
```

## Run

### Windows

Navigate into the imagenamer folder and execute main.py or run **imagenamer.ps1** (double click).

Command (POWERSHELL):

> ```
> py.exe ./main.py
> ```

### Linux

Navigate Info the imagenamer folder and execute main.py or run **imagenamer.sh** (double click).

Command (BASH):

> ```
> python3 ./main.py
> ```

## Usage

This program renames all images in a directory into a specific format.

### Safe Rename

When this feature is enabled, the program will only rename images without the safe string.

### Raw Rename

When this feature is enabled, the program names the raw image that belongs to the respective image.
Works only if the raw image and the image had the same name before they are renamed.

## Troubleshooting

If you get an error message when starting the program, delete the **settings.json** file in the settings folder.  
Else open an issue [here](https://github.com/jolsfd/imagenamer/issues).

## Format

Safe string:

> IMG

Date:

> 20201203

Time:

> 101036

Camera model:

> Pixel3a

Space letter:

> \_

The program also renames raw images. The requirement for that is the same filename before renaming.

## License

MIT License by jolsfd

---
