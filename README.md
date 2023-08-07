# fun-with-ascii-art
Convert images and videos to ascii art!

You can either print the result to terminal or to an html file.
<br />
<br />

## **How to Start**
---
### 1. Install Dependencies
Run the below code and poetry will install all the necessary dependencies.
```
poetry install
```
<br />

### 2. Add Files
Create a folder (ex. `img/`) at the root of this repository and add files you want to convert.
<br /> <br />

### 3. Run the Script
Run `my_ascii.py` file.
Here is an example of running the script file at the root of this repository.
```
poetry run python3 fun_with_ascii_art/my_ascii.py --file img/ --width 20 --style color
```

You need to pass all of the 3 arguments below.
- file : Either put in a path to a folder that holds files, or a path to a img/video file you want to convert. This package supports `png`, `jpg`, `jpeg`, `mov`, `mp3` and `avi`.
- width : Desired width (int) of the ascii result. Height will automatically be set according to the original ratio of the img/video.
- style : Choose the style of ascii you want to convert to. Options are `bw`, `color`, `emoji`, `line` and `terminal`. All except `terminal` will create an html file result if input is an image, and a video result if input is a video. Option `terminal` will print the result to the terminal directly.

<br /> <br />
## **Result Examples**
---
Below are the results of this sample image. Width set to 30.

<img src="src/monalisa.jpeg" alt="sample image (monalisa.jpeg)" width="200"/>


**Terminal**

<img src="src/monalisa_terminal.png" alt="monalisa terminal" width="200"/>

<br /> <br />

**BW (Black and White)**

<img src="src/monalisa_bw.png" alt="monalisa bw" width="200"/>

<br /> <br />

**Color**

<img src="src/monalisa_color.png" alt="monalisa color" width="200"/>

<br /> <br />

**Line**

<img src="src/monalisa_line.png" alt="monalisa line" width="200"/>

<br /> <br />

**Emoji**

<img src="src/monalisa_emoji.png" alt="monalisa emoji" width="200"/>


*You can change the font, line height and so many stuff of the result HTML file to make it more interesting!*