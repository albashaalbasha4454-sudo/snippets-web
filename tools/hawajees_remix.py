#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hawajees Remix Tool

الهدف:
1) حذف صوت الشاعر فقط من المقاطع التي تحددها أنت.
2) الحفاظ على الأغنية إذا بدأت بعد سكوت الشاعر.
3) إضافة تسجيلك أنت فوق النغمة مع خفض الموسيقى تلقائياً أثناء الإلقاء.

مهم جداً:
لا تضع وقت الأغنية داخل --poet-ranges إذا تريد الحفاظ عليها.
"""

import argparse
import shutil
import subprocess
from pathlib import Path


# تشغيل أو