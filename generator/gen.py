import jinja2
import typing
import json
import os
import marko


class Page:
    def __init__(self, html, path):
        self.html = html
        self.path = path

def build_page(filepath: str):
    """
    Primary function for turning my markup into the html I want
    :param filepath:
    :return:
    """
    with open(filepath) as text:
        header, body = parse(text)
    page = render(header, body)
    root = os.path.dirname(os.path.dirname(__file__))
    with open(os.path.join(root, page.path), 'w') as dest:
        dest.write(page.html)


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


def render(header, body):
    env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    )
    template = env.get_template(header['template'])
    txt = template.render(stylesheets=header['stylesheets'], header=header['header'],
                          body=marko.convert(body))
    return Page(txt, header['path'])

