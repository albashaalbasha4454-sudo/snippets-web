import argparse
import shutil
import subprocess
from pathlib import Path


def run(cmd):
    print('\n>>>', ' '.join(str(x) for x in cmd))
    subprocess.run(cmd, check=True)


def require_cmd(cmd):
    if shutil.which(cmd) is None:
        raise SystemExit(f'ERROR: البرنامج غير موجود: {cmd}')


def parse_time(value):
    value = value.strip()
    if ':' not in value:
        return float(value)
    parts = [float(p) for p in value.split(':')]
    if len(parts) == 2