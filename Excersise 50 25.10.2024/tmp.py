# /media/nemsys/data/projects/courses/netIT/PythonCourseNetIT/Labs_28.02.2024/Lab50/tmp.py
import os

SCRIPT_PATH = __file__
print(f'CWD: {os.getcwd()}')

new_cwd = os.path.dirname(SCRIPT_PATH)
os.chdir(new_cwd)

with open('./simple_HTTP_server/front-end/index.html','r') as f:
    content = f.read()

print(content)