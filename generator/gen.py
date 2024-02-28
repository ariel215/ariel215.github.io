import jinja2
import typing
import json
import os
import os.path as osp
import marko
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

def root():
    return os.path.dirname(os.path.dirname(__file__))

ENV = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            os.path.join(os.path.dirname(__file__), 'templates')),
)

@dataclass
class Header:
    """
    Post header to describe how a markdown post should 
    be translated to a webpage
    """
    stylesheets: typing.List[str] # list of paths to stylesheets for the post
    template: str # base template for the post to use
    path: str # destination for 
    index: bool
    name: typing.Optional[str] = None #post name; used on home page
    category: str  = "post"

class Post:
    def __init__(self, filename: str):
        with open(filename) as txt:
            header_lines = []
            body_lines = []
            reading_header = True
            for line in txt:
                if line.strip().startswith("==="):
                    reading_header = False
                    continue
                if reading_header:
                    header_lines.append(line.strip())
                else:
                    body_lines.append(line.strip())
            # Header is json literals but:
            #   * no outer braces
            #   * newlines in place of commas
        self.header = Header(**json.loads('{' + ','.join(header_lines) + '}'))
        self.body = '\n'.join(body_lines)
        self.path = self.header.path
        self.name = self.header.name or osp.splitext(
                                               osp.basename(self.header.path))[0]
        self.created = datetime.fromtimestamp(os.path.getctime(filename))
        self.modified = datetime.fromtimestamp(os.path.getmtime(filename))

    def render(self)->str:
        template = ENV.get_template(self.header.template)
        return template.render(
            stylesheets=self.header.stylesheets, 
            body=marko.convert(self.body),name=self.name,
            created=self.created,
            modified=self.modified
        )

    def write(self): 
        with open(os.path.join(root(), self.header.path), 'w') as dest:
            dest.write(self.render())


def build_index(pages: list):
    index_template = ENV.get_template('index.htm.tpl')
    txt = index_template.render(pages=pages, stylesheets=['css/style.css'], title="Ariel Davis")
    with open(osp.join(root(), 'index.html'), 'w') as dest:
        dest.write(txt)