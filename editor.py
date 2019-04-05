#!/home/dlmachine/.conda/envs/resume_env/bin/python
from flask import Flask
import jinja2
import markdown
import yaml
import os
import pdfkit

app = Flask(__name__)

@app.route('/')
def main():
    config = yaml.safe_load(open("config.yml"))
    
    # Read in Markdown Content
    md = open(config["md_template"]).read()
    extensions = ['extra', 'smarty']
    md_content = markdown.markdown(md, extensions=extensions, output_format='html5')

    # Read in and populate html template with markdown content
    html_template_str = open(os.path.join("templates/",config["html_template"])).read()
    html_page = jinja2.Template(html_template_str).render(content=md_content)

    # Save resume as pdf
    pdfkit.from_string(html_page, config["pdf_out"])
    
    return html_page

if __name__ == '__main__':
    app.run(debug=True)
