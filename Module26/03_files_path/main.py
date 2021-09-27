import os
from collections.abc import Iterable


def gen_files_path(folder=os.path.abspath(os.path.sep)) -> Iterable:
    for root, dirs, filenames in os.walk(folder):
        if dirs:
            for subdir in dirs:
                gen_files_path(subdir)
        path = root
        for filename in filenames:
            yield os.path.join(path, filename)


for item in gen_files_path(folder='/python_basic'):
    print(item, end='\n')
