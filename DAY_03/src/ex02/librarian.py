import subprocess
import os
import sys

def librarian():
    env = os.environ.get('VIRTUAL_ENV')
    if env and 'my_env' in env:
        try:
            with open('requirements.txt', 'w') as f:
                f.write("beautifulsoup4\npytest\n")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

            installed = subprocess.check_output([sys.executable, "-m", "pip", "freeze"]).decode()
            print(installed)

            with open('requirements.txt', 'w') as f:
                f.write(installed)
        except subprocess.CalledProcessError as e:
            print(f"Error during installation or pip freeze: {e}")
    else:
        raise EnvironmentError("This script must be run inside the correct virtual environment.")

if __name__ == '__main__':
    try:
        librarian()
    except EnvironmentError as e:
        print(e)