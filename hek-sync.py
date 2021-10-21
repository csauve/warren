#!/bin/env python
import shutil
import glob
from os import path, stat
from pathlib import Path
import sys

if len(sys.argv) != 2:
    print("Usage: hek-sync.py <hek-root>")
    sys.exit(1)

dev_root = "."
hek_root = sys.argv[1]

def do_copy(src_file, dst_file):
    Path(dst_file).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_file, dst_file)

def sync(pattern):
    dev_files = {path.relpath(f, dev_root): stat(f).st_mtime for f in glob.glob(path.join(dev_root, path.normpath(pattern)), recursive=True)}
    hek_files = {path.relpath(f, hek_root): stat(f).st_mtime for f in glob.glob(path.join(hek_root, path.normpath(pattern)), recursive=True)}
    for f in {*dev_files.keys(), *hek_files.keys()}:
        if f in dev_files and (f not in hek_files or dev_files[f] > hek_files[f]):
            print("Copying to HEK: " + f)
            do_copy(path.join(dev_root, f), path.join(hek_root, f))
        elif f in hek_files and (f not in dev_files or hek_files[f] > dev_files[f]):
            print("Copying to local: " + f)
            do_copy(path.join(hek_root, f), path.join(dev_root, f))

sync("data/levels/warren/**/warren_*.tif")
sync("data/levels/warren/**/**.JMS")
sync("tags/levels/warren/**/**.*")
sync("maps/warren.map")
