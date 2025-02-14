# python3 -m venv my_env
# source my_env/bin/activate
# deactivate

import os


def get_venv():
    virtual_env = os.getenv('VIRTUAL_ENV')
    if virtual_env:
        print(f'Your current virtual env is {virtual_env}')
    else:
        print('No virtual env')

if __name__ == '__main__':
    get_venv()