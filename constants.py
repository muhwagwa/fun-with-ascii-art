"""Constants
List of constants used in this app.

This file can also be imported as a module and contains the following constants:

    * IMG_EXTENSION : Permitted img extensions
    * VIDEO_EXTENSION : Permitted video extensions
    * HEADER : HTML header
    * FOOTER : HTML footer
"""


IMG_EXTENSION = ["png", "jpg", "jpeg"]
VIDEO_EXTENSION = ["mov", "mp3", "avi"]
HEADER = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body{
                line-height: 6.5px;
                letter-spacing: 3px;
                font-family: 'Courier', sans-serif;
                font-size: 7px;
                white-space: nowrap;
                background-color: lightgray;
            }
        </style>
        <title>Page Title</title>
        </head>
        <body>

        <h1>ASCII Art</h1>
    """
FOOTER = """
        </body>
        </html>
    """
