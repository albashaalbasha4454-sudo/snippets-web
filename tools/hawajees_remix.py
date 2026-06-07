#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hawajees Remix Tool

وظيفة السكربت:
1) حذف صوت الشاعر فقط من المقاطع التي تحددها أنت.
2) الحفاظ على الأغنية/الريمكس إذا بدأ بعد سكوت الشاعر.
3) إضافة تسجيلك أنت فوق النغمة مع خفض الموسيقى تلقائياً أثناء الإلقاء.

القاعدة الذهبية:
لا تضع وقت الأغنية داخل --poet-ranges إذا تريد الحفاظ عليها.
"""

import argparse
import shutil
import subprocess
from pathlib import Path


# تشغيل