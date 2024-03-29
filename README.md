[![GitHub license](https://img.shields.io/github/license/jolsfd/imagenamer.svg)](https://github.com/jolsfd/imagenamer/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/jolsfd/imagenamer.svg)](https://GitHub.com/jolsfd/imagenamer/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/jolsfd/imagenamer.svg)](https://GitHub.com/jolsfd/imagenamer/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/jolsfd/imagenamer.svg)](https://GitHub.com/jolsfd/imagenamer/pull/)
![Size](https://img.shields.io/github/repo-size/jolsfd/imagenamer)
[![Download](https://img.shields.io/github/v/release/jolsfd/imagenamer)](https://github.com/jolsfd/imagenamer/releases)

# ImageNamer

## IMPORTANT

**THIS REPOSITORY IS OBSOLETE. PLEASE USE [ImageNamer-go](https://github.com/jolsfd/imagenamer-go) INSTEAD !**

## Requirements

Python 3.7 or higher installed. Get [Python](https://www.python.org/downloads/)!

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

Folder: _imagenamer/setup/_

Open Powershell and navigate to the imagenamer folder and execute the **setup.ps1** file.

Or run followed command:

```
py.exe -m pip install -r requirements.txt
```

### Linux

Folder: _imagenamer/setup_

Navigate into the imagenamer folder and execute the **setup.sh** file in the setup folder.

Or run followed command:

```
python3 -m pip install -r requirements.txt
```

## Run

### Windows

Folder: _imagenamer/_

Navigate into the imagenamer folder and execute main.py or run **imagenamer.ps1** (double click).

Command (POWERSHELL):

> ```
> py.exe ./main.py
> ```

### Linux

Folder: _imagenamer/_

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

### Exclude Folders

Exclude Folders when renaming images. Just give the folder name, not the path or anything else.

## Troubleshooting

If you get an error message when starting the program, delete the **settings.json** file in the settings folder.  
Else open an issue [here](https://github.com/jolsfd/imagenamer/issues).

## Format

**$Y**: Year; **$M**: Month; **$D**: Day; **$h**: Hour; **$m**: Minutes; **$s**: seconds; **MODEL**: Camera Model;

With that tags you can create your personal file format.
For Example the standard format:

```
IMG_$Y$M$D_$h$m$s_MODEL
```

The program automatically builds the safe string until the first *$*.
For Example the safe string for the standard format:

```
IMG_
```

## License

MIT License by jolsfd

---
