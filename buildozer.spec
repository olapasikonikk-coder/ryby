[app]

# (str) Title of your application
title = OCR App

# (str) Package name
package.name = ocrapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.1.0,pytesseract==0.3.10,Pillow==9.5.0,requests==2.28.1

# (list) Icon files
icon.filename = assets/icon.png

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True

# (str) The Android arch to build for
android.arch = arm64-v8a

# (int) Android NDK version to use - używamy najnowszej stabilnej wersji
android.ndk = 25b

# (int) Android API to use
android.api = 30

# (int) Minimum Android API
android.minapi = 21

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
