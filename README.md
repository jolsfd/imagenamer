# ImageNamer

## Requirements

Python 3.7 or higher installed.

## Setup

Extract folder from .zip file into your favorite directory.
Run this options for installing the required libaries.

### Windows

Open Powershell and navigate to in the imagenamer folder.

```
.\setup\setup.ps1
```

or run followed command:

```
py.exe -m pip install -r requirements.txt
```

### Linux

Navigate into the imagenamer folder and run the build.sh file in the setup folder.

```
./setup/setup.sh
```

or run followed command:

```
python3 -m pip install -r requirements.txt
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

### Format

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
