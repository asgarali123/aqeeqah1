[app]

# (str) Title of your application
title = Aqeeqah Calculator

# (str) Package name
package.name = aqeeqahcalculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3crystax==3.6,kivy

# (str) Supported orientations
orientation = portrait

# Android Specific Settings
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.api = 31
android.minapi = 21
android.ndk_api = 21

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
