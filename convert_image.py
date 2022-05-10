import os, sys
from PIL import Image

source_dir = sys.argv[1]
dest_dir = sys.argv[2]

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for infile in os.listdir(source_dir):
    f, e = os.path.splitext(infile)
    outfile = f + ".png"
    print(outfile)
    if infile != outfile:
        try:
            with Image.open(f'{source_dir}/{infile}') as im:
                im.save(f'{dest_dir}/{outfile}', format='PNG')
        except OSError as err:
            print("cannot convert", infile)
            print(err)