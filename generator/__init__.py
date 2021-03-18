from generator import gen
import glob
import os.path as osp

if __name__ == '__main__':
    page_dir = osp.join(osp.dirname(__file__), 'pages', '*.md')
    pages = glob.glob(page_dir)
    for p in pages:
        gen.build_page(p)