# Resume
An overly complicated way to write your resume

You can find [my resume here](https://github.com/nateraw/Resume/blob/master/renderings/Nathan_Raw_Resume.pdf).

## How it works
[editor.py](https://github.com/nateraw/Resume/blob/master/editor.py) grabs filenames from [config.yml](https://github.com/nateraw/Resume/blob/master/config.yml) and launches a Flask app in debug mode to let you play with content in [resume.md](https://github.com/nateraw/Resume/blob/master/templates/resume.md) and [resume_template.html](https://github.com/nateraw/Resume/blob/master/templates/resume_template.html) to create your resume.

## Requirements
 - Python 3.5
 - [pdfkit](https://github.com/JazzCore/python-pdfkit)
 - flask=1.0.2
 - markdown=2.6.11
 - yaml=0.1.7
 - werkzeug=0.15.1
