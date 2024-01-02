import jinja2
import typing
import json
import os
import os.path as osp
import marko

class Page:

    ENV = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                os.path.join(os.path.dirname(__file__), 'templates')),
    )

    def __init__(self, header, body):
        self.header = header
        self.body = body
        self.path = header.get('path')
        self.name = header.get('name') or osp.splitext(
                                               osp.basename(self.path))[0]
        self._render()

    def _render(self):
        template = Page.ENV.get_template(self.header['template'])
        self.txt = template.render(stylesheets=self.header['stylesheets'], 
            header=self.header['header'],
                            body=marko.convert(self.body),name=self.name)

    def write(self): 
        with open(os.path.join(root(), self.path), 'w') as dest:
            dest.write(self.txt)

def root():
    return os.path.dirname(os.path.dirname(__file__))

def build_page(filepath: str) -> Page:
    """
    Primary function for turning my markup into the html I want
    :param filepath:
    :return:
    """
    with open(filepath) as text:
        return Page(*parse(text))
    
def parse(txt: typing.TextIO):
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
    header = json.loads('{' + ','.join(header_lines) + '}')
    body = '\n'.join(body_lines)
    return header, body


def build_index(pages: list):
    env = Page.ENV
    index_template = env.get_template('index.htm.tpl')
    txt = index_template.render(pages=pages, stylesheets=['css/style.css'], title="Ariel Davis")
    with open(osp.join(root(), 'index.html'), 'w') as dest:
        dest.write(txt)