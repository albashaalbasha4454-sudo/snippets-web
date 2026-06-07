import argparse
import shutil
import subprocess
from pathlib import Path


def run(cmd):
    print("\n>>>", " ".join(str(x) for x in cmd))
    subprocess.run(cmd, check=True)


def require_cmd(name):
    if shutil.which(name) is None:
        raise SystemExit(f"ERROR: لم أجد البرنامج المطلوب: {name}")


def parse_time(value: str) -> float:
    value = value.strip()
    if ":" not in value:
        return float(value)
    parts = [float(p) for p in value