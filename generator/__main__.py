from generator import gen
import glob
import os.path as osp

page_dir = osp.join(osp.dirname(__file__), 'pages', '*.md')
pages = [gen.build_page(p) for p in  glob.glob(page_dir)]
for p in pages:
    p.write()
gen.build_index(p for p in pages if p.header.get('index'))

