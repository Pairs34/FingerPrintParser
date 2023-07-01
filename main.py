import json
import os.path
import shutil
import glob
import traceback
from pathlib import Path

finger_folder = input("Fingerprint Klasörünün yolunu giriniz :")
desktop_fp_folders = os.path.join(os.getcwd(), "desktop")
mobile_fp_folders = os.path.join(os.getcwd(), "mobile")

if not os.path.exists(desktop_fp_folders):
    os.makedirs(desktop_fp_folders)

if not os.path.exists(mobile_fp_folders):
    os.makedirs(mobile_fp_folders)


if os.path.isdir(finger_folder):

    for file in glob.iglob(f"{finger_folder}\\*.json", recursive=False):
        try:
            finger_file = open(file, "r", encoding="utf8")
            finger_print = json.load(finger_file)
            finger_file.close()

            if "Desktop" in finger_print["tags"]:
                shutil.copyfile(file, os.path.join(desktop_fp_folders, Path(file).name))

            if "Mobile" in finger_print["tags"]:
                shutil.copyfile(file, os.path.join(mobile_fp_folders, Path(file).name))
        except:
            traceback.print_exc()

    input("Finger print taşıma işlemi tamamlandı")
else:
    print("Lütfen finger print dizini seçiniz.")