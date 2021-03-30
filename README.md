# ImageNamer

## Requirements

Python 3.7 or higher installed.

## Setup

Extract folder from .zip file into your favorite directory.

### Windows

Open Powershell or cmd and navigate to in the imagenamer folder.
Run this command for installing the required libaries.

```
py.exe -m pip install -r requirements.txt
```

### Linux

Navigate into the imagenamer folder and run the build.sh file in the setup folder.
The script installs the required libaries into your python enviroment.

```bash
./setup/build.sh
```

## Run

### Windows

Navigate into the imagenamer folder and execute main.py.

Command:

> ```
> py.exe ./main.py
> ```

### Linux

Navigate Info the imagenamer folder and execute main.py or run the bash script.

Command (python file):

> ```
> python3 ./main.py
> ```

Command (bash script):

> ```
> ./imagenamer.sh
> ```

## Usage

This program renames all images in a directory into a specific format.
Example: IMG_20201203_101036_Pixel3a.jpg

### Format:

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
