import datetime as dt
import os
import pandas as pd

print('logs started')

now = dt.datetime.now()
date = dt.datetime.now().date()
log_file_path = r'log_files/'+str(date)+'.xlsx'
log_file = None

def df(**kwargs):
    return pd.DataFrame(kwargs)

def check_and_build():
    global log_file
    if os.path.isfile(log_file_path):
        log_file = pd.read_excel(log_file_path)
        return False
    else:
        pd.DataFrame([[1, now, 'Log file created']],columns=['row','datetime','operation']).to_excel(log_file_path,index=False)
        log_file = pd.read_excel(log_file_path)
        return False

check_and_build()

def write(operation):
    global log_file
    global now
    log_file = pd.DataFrame(log_file)
    pd.DataFrame(log_file).append(
        pd.DataFrame([[log_file.shape[0]+1, now, operation]],
                     columns=['row','datetime','operation'])).to_excel(log_file_path,index=False)