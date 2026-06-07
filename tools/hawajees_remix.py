#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Hawajees Remix: يحذف الشاعر فقط من الأوقات المحددة ويحافظ على الأغنية خارجها.
import argparse, shutil, subprocess
from pathlib import Path

def need(c):
    if shutil.which(c) is None: raise SystemExit(f"Missing command: {c}")

def run(cmd):
    print('>>> ' + ' '.join(map(str, cmd)))
    subprocess.run(cmd, check=True)

def sec(x):
    p=[float(i