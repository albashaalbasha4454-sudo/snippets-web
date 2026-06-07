#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse, shutil, subprocess
from pathlib import Path

# يحذف صوت الشاعر فقط من المقاطع المحددة، ويحافظ على الأغنية خارجها.

def need(cmd):
    if shutil.which(cmd) is None:
        raise SystemExit(f"Missing command: {cmd}")

def run(cmd):
    print('>>> ' + ' '.join(map(str, cmd)))
    subprocess.run(cmd, check=True)

def tsec(s):
    p=[float(x) for x in s.strip().split(':')]
    if len(p)==1: return p[0]
    if len(p)==2: return p[0]*60