# ImageNamer

## Requirements

Python 3.7 or higher installed.

## Setup

Extract folder from .zip file into your favorite directory.

### Linux

Navigate into the imagenamer folder and run the build.sh file in the setup folder.
The script installs the required libaries into your python enviroment.

```bash
./setup/build.sh
```

### Windows

Open Powershell or cmd and navigate to in the imagenamer folder.
Run this command for installing the required libaries.

```
py.exe -m pip install requirements.txt
```

## Run

Execute the main.py.

Windows

> ```
> py.exe ./imagenamer/main.py
> ```

````

Linux

> ```
> ./imagenamer/imagenamer
> ```

````

## Usage

This program renames all images in a directory into a specific format.

> Format: SAFESTRING_DATETIME_CAMERA_MODEL.jpg

The program also renames raw images. The requirement for that is the same filename before renaming.

## License

MIT License by jolsfd

---
