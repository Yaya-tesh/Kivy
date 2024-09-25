[app]

# (str) Title of your application
title = BingoApp

# (str) Package name
package.name = bingoapp

# (str) Package domain (you can use your own domain or a placeholder)
package.domain = org.yourdomain.bingoapp

# (str) Source code file to run
source.main = main.py

# (list) Source files to include (e.g., .py, .kv, audio files)
source.include_exts = py,png,jpg,kv,mp3

# (list) Patterns to include from the source directory
source.include_patterns = sounds/*

# (str) Application version
version = 0.1

# (str) Icon of the application (should be a square image)
icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash image (displayed while app loads, optional)
presplash.filename = %(source.dir)s/data/presplash.png

# (list) Application requirements (these are required libraries for your app)
# Python 3, Kivy for GUI, Pygame for sound
requirements = python3, kivy, pygame

# (str) Supported orientation (portrait, landscape, sensorLandscape, etc.)
orientation = portrait

# (list) Permissions required for the app
# INTERNET - In case the app uses network features
# READ_EXTERNAL_STORAGE - To access audio files if stored on device
# WRITE_EXTERNAL_STORAGE - If you save data on device
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Minimum API level supported by your application (21 for Android 5.0 and higher)
android.minapi = 21

# (int) Target API level (latest Android API supported by Buildozer)
android.api = 33

# (int) Android NDK version
android.ndk = 23b

# (bool) Indicate whether the app should be full-screen
fullscreen = 1

# (str) Language code of the default locale (optional)
#locale = en_US

# (str) Supported Android version numbers separated by a comma
# Uncomment below to specify supported Android versions (API levels)
# android.sdk = 21,22,23,24,25,26,27,28,29,30,31

# (str) The package format to use for distribution
# p4a is recommended for compatibility with most devices
android.dist_name = p4a

# (str) Keystore for signing the APK (for release builds)
# Uncomment and configure below for custom signing (optional)
# android.release_keystore = /path/to/your/keystore
# android.release_keyalias = keyalias
# android.release_keystore_passwd = your_password
# android.release_keyalias_passwd = your_password

# (bool) Indicate whether the app should use the APK expansion files (OBB)
# OBB is required when the APK exceeds 100 MB (Google Play Store limit)
# android.use_expansion = False

# (list) Android features that the application needs.
# Enable multitouch for the app
# android.features = android.hardware.touchscreen.multitouch

# (bool) Indicate whether to include the debug symbols in the APK (debug builds only)
# Useful for debugging C/C++ code
# android.debug_symbols = 1

# (bool) Indicate if your app is a service (background process)
# android.service = False

# (str) The URL for Play Store listing
# Uncomment below if you're publishing to the Google Play Store
# android.play_store_url = https://play.google.com/store/apps/details?id=your.package.name

# (list) Screen densities supported by the app
# Add screen densities for supporting different device resolutions
# android.densities = ldpi, mdpi, hdpi, xhdpi

# (bool) If True, ensures compatibility with older devices (Android 4.4 and below)
# android.compatibility_mode = True

# (bool) Indicate whether to allow debugging (True = APK is debuggable)
# android.debug = False

# (bool) Enable hardware acceleration (True by default)
# android.hardware_accelerated = True

# (str) Android entry point for the app (for Kivy apps, leave it as default)
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android log level (can be debug, info, warning, error)
android.log_level = info

# (int) Python version to use (3 for Python 3)
python_version = 3

# (bool) Set to True to build the app as an APK (Android Package)
# Set to False if you only want to build for testing (running on an emulator)
android.release = False

# (str) File format for the output (can be APK or AAB - for Google Play Store)
android.package_format = apk

# (bool) Indicate whether to build a bundle for Google Play Store (True for AAB)
# android.bundle = True

# (bool) Indicate whether to create a debugging key if one doesn't exist
# android.debug_create_keys = False

# (list) Directories to include in the distribution (optional)
# paths = /path/to/your/directory1,/path/to/your/directory2

# (str) Custom JVM arguments (optional)
# android.jvm_args = -Xmx4096m

# (list) Modules to exclude from the build
# Uncomment below if you want to exclude specific libraries/modules from the APK
# android.exclude_modules = library1,library2

# (str) Language pack to include in the APK
# Uncomment below if you want to include specific language packs
# android.include_languages = en,es

# (list) Architectures to support
# p4a supports 'armeabi-v7a' and 'arm64-v8a' by default
# Uncomment below to support other architectures
# android.archs = armeabi-v7a,arm64-v8a,x86

# (list) Libraries to include in the APK
# Uncomment below to include third-party libraries or native C/C++ code
# android.include_libraries = lib1.so,lib2.so

# (bool) Enable OpenGL ES 2.0 (True by default for Kivy apps)
# Uncomment if your app doesn't use OpenGL ES 2.0 features
# android.opengles = 2.0

# (bool) Add your license if required
# license = your_license.txt