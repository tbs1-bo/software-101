import os
import subprocess

IGNORE = [
    'bottle',
    'datenbank',
    'decorator',
    'guizero',
    'netzwerk',
    'pyqt',
    'pygame',
    'tkinter',
    'typen',
    'testing',
    'mqtt',
    'python',
    'python_intro',
    'pysimplegui',
    'pygame-zero',
    'venv'
]


for d in os.listdir():
    if not os.path.isdir(d) or d.startswith('.') or d in IGNORE:
        print('  ignoring', d)
        continue

    print('testing', d)
    r = subprocess.run(['pytest', '--nbval', d])
    if r.returncode != 0:
        print('ERROR')
        exit(1)
