[app]
# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (com.example, org.test, etc.)
package.domain = com.example

# (str) Source code directory, where the main.py is located
source.dir = .

# (str) Main script name
source.main = main.py

# (list) List of application requirements (comma separated)
# Add any other dependencies if needed
requirements = python3,kivy,plyer

# (str) Supported orientations (one of landscape, portrait or all)
orientation = portrait

# (str) Application version
version = 1.0.0

# (list) Presplash background (Optional)
presplash.filename = %(source.dir)s/data/presplash.png

# (list) Supported platforms
# Available options: android, ios, windows, macos, linux, html
supported_platforms = android

# (bool) Indicate if the application needs internet access
android.permissions = INTERNET

# (str) The format used to package the app for the play store (e.g., release)
android.api = 33
android.minapi = 21

# (str) Android NDK version
android.ndk = 23b

# (list) Additional Java .jar or .aar libraries to include (if needed)
android.add_jars = libs/some-library.jar

# (str) Presplash background color (default #FFFFFF)
presplash_color = #FFFFFF

# (bool) Whether to include the debug version
debug = True
android.sdk = 33
