import time
import numpy as np
import pandas as pd


def processor(app):    
    for file_path in app.file_paths_to_process:
        # read in data from .txt file
        with open(file_path, 'r') as f:
            data = f.read()

            # transform text - turn ever other character upper case
            data = ''.join([data[i].upper() if i % 2 == 0 else data[i].lower()
                            for i in range(len(data))])
            print(data)

            # save to output file
            print('save path', app.path_to_output + '/' + file_path.split('/')[-1],flush=True)
            with open(app.path_to_output + '/' +
                      file_path.split('/')[-1], 'w') as f:
                f.write(data)
                print(data, flush=True)

