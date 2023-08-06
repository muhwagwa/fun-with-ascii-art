# fun-with-ascii-art
Convert images and videos to ascii art!

You can either print the result to terminal or to a html file.
<br />
<br />

## **How to Start**
---
### Install Dependencies
Run the below code and poetry will install all the necessary dependencies.
```
poetry install
```
<br />

### Add Files
Create a folder (ex. img/) at the root of this repository and add files you want to convert.
<br /> <br />

### Run the Script
Run `my_ascii.py` file.
Here is an example of running the script file at the root of this repository.
```
poetry run python3 fun_with_ascii_art/my_ascii.py --file img/ --width 20 --style color
```

You need to pass all of the 3 arguments below.
- file : Either put in a path to a folder that holds files, or a path to a img/video file you want to convert. Supports `png`, `jpg`, `jpeg`, `mov`, `mp3` and `avi`.
- width : Desired width (int) of the ascii result. Height will automatically be set according to the original ratio of the img/video.
- style : Choose the style of ascii you want to convert to. Options are `bw`, `color`, `emoji`, `line` and `terminal`.

<br /> <br />
## **Result Examples**
---
Below are the results of this sample image. Width set to 30.

<img src="img/flower.jpeg" alt="drawing" width="400"/>


**Terminal**
```

```

**BW (Black and White)**

**Color**

**Emoji**

**Line**

