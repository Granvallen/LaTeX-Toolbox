# drop some item of .bib extracted from zotero

import sys
import re

try:
    bibfile = sys.argv[1]
except:
    bibfile = "./bibcite.bib"

key = ['file', 'url', 'doi', 'urldate', 'issn', 'isbn']

with open(bibfile, 'r', encoding='UTF-8') as f:
    bib = f.read()
    print(f.read())

keypatten = '({})'.format('|'.join(key))
dropedbib = re.sub(r'\t' + keypatten + r' = {(.*?)}(,?\n)', '', bib)

with open(bibfile, 'w', encoding='UTF-8') as f:
    f.write(dropedbib)

print('Done!')