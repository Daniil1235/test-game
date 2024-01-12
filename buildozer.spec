(python) daniil@ubuntu-vmware:~/Документы/PythonProgects/pygame$ buildozer android debug 
# Check configuration tokens
# Ensure build layout
# Check configuration tokens
# Preparing build
# Check requirements for android
# Search for Git (git)
#  -> found at /usr/bin/git
# Search for Cython (cython)
#  -> found at /home/daniil/Документы/PythonProgects/pygame/venv/python/bin/cython
# Search for Java compiler (javac)
#  -> found at /usr/lib/jvm/java-11-openjdk-amd64/bin/javac
# Search for Java keytool (keytool)
#  -> found at /usr/lib/jvm/java-11-openjdk-amd64/bin/keytool
# Install platform
# Run ['git', 'config', '--get', 'remote.origin.url']
# Cwd /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
https://github.com/kivy/python-for-android.git
# Run ['git', 'branch', '-vv']
# Cwd /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
* master e155baf9 [origin/master] Merge pull request #2891 from misl6/release-2023.09.16
# Run ['/home/daniil/Документы/PythonProgects/pygame/venv/python/bin/python', '-m', 'pip', 'install', '-q', 'appdirs', 'colorama>=0.3.3', 'jinja2', 'sh>=1.10, <2.0; sys_platform!="win32"', 'build', 'toml', 'packaging']
# Cwd None

[notice] A new release of pip is available: 23.3.1 -> 23.3.2
[notice] To update, run: pip install --upgrade pip
# Apache ANT found at /home/daniil/.buildozer/android/platform/apache-ant-1.9.4
# Android SDK found at /home/daniil/.buildozer/android/platform/android-sdk
# Recommended android's NDK version by p4a is: 25b
# Android NDK found at /home/daniil/.buildozer/android/platform/android-ndk-r25b
# Run ['/home/daniil/Документы/PythonProgects/pygame/venv/python/bin/python', '-m', 'pythonforandroid.toolchain', 'aab', '-h', '--color=always', '--storage-dir=/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a', '--ndk-api=21', '--ignore-setup-py', '--debug']
# Cwd /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[WARNING]: prerequisites.py is experimental and does not support all prerequisites yet.
[WARNING]: Please report any issues to the python-for-android issue tracker.
[WARNING]: prerequisites.py is experimental and does not support all prerequisites yet.
[WARNING]: Please report any issues to the python-for-android issue tracker.
usage: toolchain.py aab [-h] [--debug] [--color {always,never,auto}]
                        [--sdk-dir SDK_DIR] [--ndk-dir NDK_DIR]
                        [--android-api ANDROID_API]
                        [--ndk-version NDK_VERSION] [--ndk-api NDK_API]
                        [--symlink-bootstrap-files]
                        [--storage-dir STORAGE_DIR] [--arch ARCH]
                        [--dist-name DIST_NAME] [--requirements REQUIREMENTS]
                        [--recipe-blacklist RECIPE_BLACKLIST]
                        [--blacklist-requirements BLACKLIST_REQUIREMENTS]
                        [--bootstrap BOOTSTRAP] [--hook HOOK] [--force-build]
                        [--no-force-build] [--require-perfect-match]
                        [--no-require-perfect-match] [--allow-replace-dist]
                        [--no-allow-replace-dist]
                        [--local-recipes LOCAL_RECIPES]
                        [--activity-class-name ACTIVITY_CLASS_NAME]
                        [--service-class-name SERVICE_CLASS_NAME]
                        [--java-build-tool {auto,ant,gradle}] [--copy-libs]
                        [--no-copy-libs] [--add-asset ASSETS]
                        [--add-resource RESOURCES] [--private PRIVATE]
                        [--use-setup-py] [--ignore-setup-py] [--release]
                        [--with-debug-symbols] [--keystore KEYSTORE]
                        [--signkey SIGNKEY] [--keystorepw KEYSTOREPW]
                        [--signkeypw SIGNKEYPW]

options:
  -h, --help            show this help message and exit
  --debug               Display debug output and all build info
  --color {always,never,auto}
                        Enable or disable color output (default enabled on
                        tty)
  --sdk-dir SDK_DIR, --sdk_dir SDK_DIR
                        The filepath where the Android SDK is installed
  --ndk-dir NDK_DIR, --ndk_dir NDK_DIR
                        The filepath where the Android NDK is installed
  --android-api ANDROID_API, --android_api ANDROID_API
                        The Android API level to build against defaults to 33
                        if not specified.
  --ndk-version NDK_VERSION, --ndk_version NDK_VERSION
                        DEPRECATED: the NDK version is now found automatically
                        or not at all.
  --ndk-api NDK_API     The Android API level to compile against. This should
                        be your *minimal supported* API, not normally the same
                        as your --android-api. Defaults to min(ANDROID_API,
                        21) if not specified.
  --symlink-bootstrap-files, --ssymlink_bootstrap_files
                        If True, symlinks the bootstrap files creation. This
                        is useful for development only, it could also cause
                        weird problems.
  --storage-dir STORAGE_DIR
                        Primary storage directory for downloads and builds
                        (default: /home/daniil/.local/share/python-for-
                        android)
  --arch ARCH           The archs to build for.
  --dist-name DIST_NAME, --dist_name DIST_NAME
                        The name of the distribution to use or create
  --requirements REQUIREMENTS
                        Dependencies of your app, should be recipe names or
                        Python modules. NOT NECESSARY if you are using Python
                        3 with --use-setup-py
  --recipe-blacklist RECIPE_BLACKLIST
                        Blacklist an internal recipe from use. Allows
                        disabling Python 3 core modules to save size
  --blacklist-requirements BLACKLIST_REQUIREMENTS
                        Blacklist an internal recipe from use. Allows
                        disabling Python 3 core modules to save size
  --bootstrap BOOTSTRAP
                        The bootstrap to build with. Leave unset to choose
                        automatically.
  --hook HOOK           Filename to a module that contains python-for-android
                        hooks
  --local-recipes LOCAL_RECIPES, --local_recipes LOCAL_RECIPES
                        Directory to look for local recipes
  --activity-class-name ACTIVITY_CLASS_NAME
                        The full java class name of the main activity
  --service-class-name SERVICE_CLASS_NAME
                        Full java package name of the PythonService class
  --java-build-tool {auto,ant,gradle}
                        The java build tool to use when packaging the APK,
                        defaults to automatically selecting an appropriate
                        tool.
  --add-asset ASSETS    Put this in the assets folder in the apk.
  --add-resource RESOURCES
                        Put this in the res folder in the apk.
  --private PRIVATE     the directory with the app source code files
                        (containing your main.py entrypoint)
  --use-setup-py        Process the setup.py of a project if present.
                        (Experimental!
  --ignore-setup-py     Don't run the setup.py of a project if present. This
                        may be required if the setup.py is not designed to
                        work inside p4a (e.g. by installing dependencies that
                        won't work or aren't desired on Android
  --release             Build your app as a non-debug release build. (Disables
                        gdb debugging among other things)
  --with-debug-symbols  Will keep debug symbols from `.so` files.
  --keystore KEYSTORE   Keystore for JAR signing key, will use jarsigner
                        default if not specified (release build only)
  --signkey SIGNKEY     Key alias to sign PARSER_APK. with (release build
                        only)
  --keystorepw KEYSTOREPW
                        Password for keystore
  --signkeypw SIGNKEYPW
                        Password for key alias

  Whether to force compilation of a new distribution

  --force-build
  --no-force-build      (this is the default)
  --require-perfect-match
  --no-require-perfect-match
                        (this is the default)
  --allow-replace-dist  (this is the default)
  --no-allow-replace-dist
  --copy-libs
  --no-copy-libs        (this is the default)
# Check application requirements
# Compile platform
# Run ['/home/daniil/Документы/PythonProgects/pygame/venv/python/bin/python', '-m', 'pythonforandroid.toolchain', 'create', '--dist_name=firstpygame', '--bootstrap=sdl2', '--requirements=python3,pygame,jnius,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf,png,jpeg', '--arch=arm64-v8a', '--arch=armeabi-v7a', '--copy-libs', '--color=always', '--storage-dir=/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a', '--ndk-api=21', '--ignore-setup-py', '--debug']
# Cwd /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[WARNING]: prerequisites.py is experimental and does not support all prerequisites yet.
[WARNING]: Please report any issues to the python-for-android issue tracker.
[WARNING]: prerequisites.py is experimental and does not support all prerequisites yet.
[WARNING]: Please report any issues to the python-for-android issue tracker.
[INFO]:    Will compile for the following archs: armeabi-v7a, arm64-v8a
[INFO]:    Found Android API target in $ANDROIDAPI: 31
[INFO]:    Available Android APIs are (20, 30, 31)
[INFO]:    Requested API target 31 is available, continuing.
[INFO]:    Found NDK dir in $ANDROIDNDK: /home/daniil/.buildozer/android/platform/android-ndk-r25b
[INFO]:    Found NDK version 25b
[INFO]:    Getting NDK API version (i.e. minimum supported API) from user argument
[INFO]:    ccache is missing, the build will not be optimized in the future.
[DEBUG]:   All possible dists: []
[DEBUG]:   Dist matching name and arch: []
[DEBUG]:   Dist matching ndk_api and recipe: []
[INFO]:    No existing dists meet the given requirements!
[DEBUG]:   Remove directory and subdirectory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/dists/firstpygame
[INFO]:    No dist exists that meets your requirements, so one will be built.
[INFO]:    Found a single valid recipe set: ['hostpython3', 'jnius', 'jpeg', 'libffi', 'openssl', 'png', 'sdl2_image', 'sdl2_mixer', 'sdl2_ttf', 'sqlite3', 'python3', 'sdl2', 'setuptools', 'pygame', 'six', 'pyjnius', 'android']
[INFO]:    The selected bootstrap is sdl2
[INFO]:    # Creating dist with sdl2 bootstrap
[INFO]:    Dist will have name firstpygame and requirements (python3, pygame, jnius, sdl2, sdl2_image, sdl2_mixer, sdl2_ttf, png, jpeg)
[INFO]:    Dist contains the following requirements as recipes: ['hostpython3', 'jpeg', 'libffi', 'openssl', 'png', 'sdl2_image', 'sdl2_mixer', 'sdl2_ttf', 'sqlite3', 'python3', 'sdl2', 'setuptools', 'pygame', 'six', 'pyjnius', 'android']
[INFO]:    Dist will also contain modules (jnius) installed from pip
[INFO]:    Dist will be build in mode debug
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/bootstrap_builds/sdl2
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[DEBUG]:   Create directory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/dists/firstpygame
[INFO]:    Recipe build order is ['hostpython3', 'jpeg', 'libffi', 'openssl', 'png', 'sdl2_image', 'sdl2_mixer', 'sdl2_ttf', 'sqlite3', 'python3', 'sdl2', 'setuptools', 'pygame', 'six', 'pyjnius', 'android']
[INFO]:    The requirements (jnius) were not found as recipes, they will be installed with pip.
[INFO]:    # Downloading recipes 
[INFO]:    Downloading hostpython3
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/hostpython3
[DEBUG]:   -> running basename https://www.python.org/ftp/python/3.10.10/Python-3.10.10.tgz
[DEBUG]:        Python-3.10.10.tgz
[INFO]:    hostpython3 download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading jpeg
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/jpeg
[DEBUG]:   -> running basename https://github.com/libjpeg-turbo/libjpeg-turbo/archive/2.0.1.tar.gz
[DEBUG]:        2.0.1.tar.gz
[INFO]:    jpeg download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading libffi
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/libffi
[DEBUG]:   -> running basename https://github.com/libffi/libffi/archive/v3.4.2.tar.gz
[DEBUG]:        v3.4.2.tar.gz
[INFO]:    libffi download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading openssl
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/openssl
[DEBUG]:   -> running basename https://www.openssl.org/source/openssl-1.1.1m.tar.gz
[DEBUG]:        openssl-1.1.1m.tar.gz
[INFO]:    openssl download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading png
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/png
[DEBUG]:   -> running basename https://github.com/glennrp/libpng/archive/v1.6.37.zip
[DEBUG]:        v1.6.37.zip
[INFO]:    png download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading sdl2_image
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/sdl2_image
[DEBUG]:   -> running basename https://github.com/libsdl-org/SDL_image/releases/download/release-2.6.2/SDL2_image-2.6.2.tar.gz
[DEBUG]:        SDL2_image-2.6.2.tar.gz
[INFO]:    sdl2_image download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading sdl2_mixer
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/sdl2_mixer
[DEBUG]:   -> running basename https://github.com/libsdl-org/SDL_mixer/releases/download/release-2.6.2/SDL2_mixer-2.6.2.tar.gz
[DEBUG]:        SDL2_mixer-2.6.2.tar.gz
[INFO]:    sdl2_mixer download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading sdl2_ttf
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/sdl2_ttf
[DEBUG]:   -> running basename https://github.com/libsdl-org/SDL_ttf/releases/download/release-2.20.1/SDL2_ttf-2.20.1.tar.gz
[DEBUG]:        SDL2_ttf-2.20.1.tar.gz
[INFO]:    sdl2_ttf download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading sqlite3
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/sqlite3
[DEBUG]:   -> running basename https://www.sqlite.org/2021/sqlite-amalgamation-3350500.zip
[DEBUG]:        sqlite-amalgamation-3350500.zip
[INFO]:    sqlite3 download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading python3
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/python3
[DEBUG]:   -> running basename https://www.python.org/ftp/python/3.10.10/Python-3.10.10.tgz
[DEBUG]:        Python-3.10.10.tgz
[INFO]:    python3 download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading sdl2
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/sdl2
[DEBUG]:   -> running basename https://github.com/libsdl-org/SDL/releases/download/release-2.26.1/SDL2-2.26.1.tar.gz
[DEBUG]:        SDL2-2.26.1.tar.gz
[INFO]:    sdl2 download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading setuptools
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/setuptools
[DEBUG]:   -> running basename https://pypi.python.org/packages/source/s/setuptools/setuptools-51.3.3.tar.gz
[DEBUG]:        setuptools-51.3.3.tar.gz
[INFO]:    setuptools download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading pygame
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/pygame
[DEBUG]:   -> running basename https://github.com/pygame/pygame/archive/2.1.0.tar.gz
[DEBUG]:        2.1.0.tar.gz
[INFO]:    pygame download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading six
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/six
[DEBUG]:   -> running basename https://pypi.python.org/packages/source/s/six/six-1.15.0.tar.gz
[DEBUG]:        six-1.15.0.tar.gz
[INFO]:    six download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading pyjnius
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/packages/pyjnius
[DEBUG]:   -> running basename https://github.com/kivy/pyjnius/archive/1.5.0.zip
[DEBUG]:        1.5.0.zip
[INFO]:    pyjnius download already cached, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Downloading android
[INFO]:    Skipping android download as no URL is set
[INFO]:    # Building all recipes for arch armeabi-v7a
[INFO]:    # Unpacking recipes
[INFO]:    Unpacking hostpython3 for armeabi-v7a
[DEBUG]:   -> running basename https://www.python.org/ftp/python/3.10.10/Python-3.10.10.tgz
[DEBUG]:        Python-3.10.10.tgz
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/hostpython3/desktop
[INFO]:    hostpython3 is already unpacked, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[DEBUG]:   Create directory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21
[INFO]:    Unpacking jpeg for armeabi-v7a
[DEBUG]:   -> running basename https://github.com/libjpeg-turbo/libjpeg-turbo/archive/2.0.1.tar.gz
[DEBUG]:        2.0.1.tar.gz
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21
[DEBUG]:   Moving libjpeg-turbo-2.0.1 to /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[DEBUG]:   Create directory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21
[INFO]:    Unpacking libffi for armeabi-v7a
[DEBUG]:   -> running basename https://github.com/libffi/libffi/archive/v3.4.2.tar.gz
[DEBUG]:        v3.4.2.tar.gz
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21
[DEBUG]:   Moving libffi-3.4.2 to /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[DEBUG]:   Create directory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21
[INFO]:    Unpacking openssl for armeabi-v7a
[DEBUG]:   -> running basename https://www.openssl.org/source/openssl-1.1.1m.tar.gz
[DEBUG]:        openssl-1.1.1m.tar.gz
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21
[DEBUG]:   Moving openssl-1.1.1m to /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[DEBUG]:   Create directory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/png/armeabi-v7a__ndk_target_21
[INFO]:    Unpacking png for armeabi-v7a
[DEBUG]:   -> running basename https://github.com/glennrp/libpng/archive/v1.6.37.zip
[DEBUG]:        v1.6.37.zip
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/png/armeabi-v7a__ndk_target_21
[DEBUG]:   Moving libpng-1.6.37 to /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/png/armeabi-v7a__ndk_target_21/png
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Unpacking sdl2_image for armeabi-v7a
[DEBUG]:   -> running basename https://github.com/libsdl-org/SDL_image/releases/download/release-2.6.2/SDL2_image-2.6.2.tar.gz
[DEBUG]:        SDL2_image-2.6.2.tar.gz
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/bootstrap_builds/sdl2/jni
[INFO]:    sdl2_image is already unpacked, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Unpacking sdl2_mixer for armeabi-v7a
[DEBUG]:   -> running basename https://github.com/libsdl-org/SDL_mixer/releases/download/release-2.6.2/SDL2_mixer-2.6.2.tar.gz
[DEBUG]:        SDL2_mixer-2.6.2.tar.gz
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/bootstrap_builds/sdl2/jni
[INFO]:    sdl2_mixer is already unpacked, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Unpacking sdl2_ttf for armeabi-v7a
[DEBUG]:   -> running basename https://github.com/libsdl-org/SDL_ttf/releases/download/release-2.20.1/SDL2_ttf-2.20.1.tar.gz
[DEBUG]:        SDL2_ttf-2.20.1.tar.gz
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/bootstrap_builds/sdl2/jni
[INFO]:    sdl2_ttf is already unpacked, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[DEBUG]:   Create directory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21
[INFO]:    Unpacking sqlite3 for armeabi-v7a
[DEBUG]:   -> running basename https://www.sqlite.org/2021/sqlite-amalgamation-3350500.zip
[DEBUG]:        sqlite-amalgamation-3350500.zip
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21
[DEBUG]:   Moving sqlite-amalgamation-3350500 to /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[DEBUG]:   Create directory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21
[INFO]:    Unpacking python3 for armeabi-v7a
[DEBUG]:   -> running basename https://www.python.org/ftp/python/3.10.10/Python-3.10.10.tgz
[DEBUG]:        Python-3.10.10.tgz
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21
[DEBUG]:   Moving Python-3.10.10 to /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[INFO]:    Unpacking sdl2 for armeabi-v7a
[DEBUG]:   -> running basename https://github.com/libsdl-org/SDL/releases/download/release-2.26.1/SDL2-2.26.1.tar.gz
[DEBUG]:        SDL2-2.26.1.tar.gz
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/bootstrap_builds/sdl2/jni
[INFO]:    sdl2 is already unpacked, skipping
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[DEBUG]:   Create directory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/setuptools/armeabi-v7a__ndk_target_21
[INFO]:    Unpacking setuptools for armeabi-v7a
[DEBUG]:   -> running basename https://pypi.python.org/packages/source/s/setuptools/setuptools-51.3.3.tar.gz
[DEBUG]:        setuptools-51.3.3.tar.gz
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/setuptools/armeabi-v7a__ndk_target_21
[DEBUG]:   Moving setuptools-51.3.3 to /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/setuptools/armeabi-v7a__ndk_target_21/setuptools
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[DEBUG]:   Create directory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/pygame/armeabi-v7a__ndk_target_21
[INFO]:    Unpacking pygame for armeabi-v7a
[DEBUG]:   -> running basename https://github.com/pygame/pygame/archive/2.1.0.tar.gz
[DEBUG]:        2.1.0.tar.gz
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/pygame/armeabi-v7a__ndk_target_21
[DEBUG]:   Moving pygame-2.1.0 to /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/pygame/armeabi-v7a__ndk_target_21/pygame
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[DEBUG]:   Create directory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/six/armeabi-v7a__ndk_target_21
[INFO]:    Unpacking six for armeabi-v7a
[DEBUG]:   -> running basename https://pypi.python.org/packages/source/s/six/six-1.15.0.tar.gz
[DEBUG]:        six-1.15.0.tar.gz
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/six/armeabi-v7a__ndk_target_21
[DEBUG]:   Moving six-1.15.0 to /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/six/armeabi-v7a__ndk_target_21/six
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[DEBUG]:   Create directory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/pyjnius-sdl2/armeabi-v7a__ndk_target_21
[INFO]:    Unpacking pyjnius for armeabi-v7a
[DEBUG]:   -> running basename https://github.com/kivy/pyjnius/archive/1.5.0.zip
[DEBUG]:        1.5.0.zip
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/pyjnius-sdl2/armeabi-v7a__ndk_target_21
[DEBUG]:   Moving pyjnius-1.5.0 to /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/pyjnius-sdl2/armeabi-v7a__ndk_target_21/pyjnius
[INFO]:    <- directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android
[DEBUG]:   Create directory /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/android-sdl2/armeabi-v7a__ndk_target_21
[DEBUG]:   -> running cp -a /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android/pythonforandroid/recipes/android/src /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/android-sdl2/armeabi-v7a__ndk_target_21/android
[INFO]:    # Prebuilding recipes
[INFO]:    Prebuilding hostpython3 for armeabi-v7a
[INFO]:    hostpython3 has no prebuild_armeabi_v7a, skipping
[INFO]:    Applying patches for hostpython3[armeabi-v7a]
[INFO]:    hostpython3 already patched, skipping
[INFO]:    Prebuilding jpeg for armeabi-v7a
[INFO]:    jpeg has no prebuild_armeabi_v7a, skipping
[INFO]:    Prebuilding libffi for armeabi-v7a
[INFO]:    libffi has no prebuild_armeabi_v7a, skipping
[INFO]:    Applying patches for libffi[armeabi-v7a]
[INFO]:    Applying patch remove-version-info.patch
[DEBUG]:   -> running patch -t -d /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi -p1 -i /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android/pythonforandroid/recipes/libffi/remove-version-info.patch
[DEBUG]:        patching file Makefile.am
[DEBUG]:        Hunk #1 succeeded at 138 with fuzz 2 (offset -18 lines).
[INFO]:    Prebuilding openssl for armeabi-v7a
[INFO]:    openssl has no prebuild_armeabi_v7a, skipping
[INFO]:    Prebuilding png for armeabi-v7a
[INFO]:    png has no prebuild_armeabi_v7a, skipping
[INFO]:    Prebuilding sdl2_image for armeabi-v7a
[INFO]:    -> directory context /home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/bootstrap_builds/sdl2/jni/SDL2_image/external
[DEBUG]:   -> running download.sh
[DEBUG]:        fatal: целевой путь «external/jpeg» уже существует и не является пустым каталогом.
Exception in thread background thread for pid 4058:
Traceback (most recent call last):
  File "/usr/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.10/threading.py", line 953, in run
    self._target(*self._args, **self._kwargs)
  File "/home/daniil/Документы/PythonProgects/pygame/venv/python/lib/python3.10/site-packages/sh.py", line 1641, in wrap
    fn(*rgs, **kwargs)
  File "/home/daniil/Документы/PythonProgects/pygame/venv/python/lib/python3.10/site-packages/sh.py", line 2569, in background_thread
    handle_exit_code(exit_code)
  File "/home/daniil/Документы/PythonProgects/pygame/venv/python/lib/python3.10/site-packages/sh.py", line 2269, in fn
    return self.command.handle_command_exit_code(exit_code)
  File "/home/daniil/Документы/PythonProgects/pygame/venv/python/lib/python3.10/site-packages/sh.py", line 869, in handle_command_exit_code
    raise exc
sh.ErrorReturnCode_128: 

  RAN: '/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/bootstrap_builds/sdl2/jni/SDL2_image/external/download.sh'

  STDOUT:
fatal: целевой путь «external/jpeg» уже существует и не является пустым каталогом.


  STDERR:

Traceback (most recent call last):
  File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android/pythonforandroid/toolchain.py", line 1262, in <module>
    main()
  File "/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android/pythonforandroid/entrypoints.py", line 18, in main
    ToolchainCL()
  File "/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android/pythonforandroid/toolchain.py", line 680, in __init__
    getattr(self, command)(args)
  File "/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android/pythonforandroid/toolchain.py", line 99, in wrapper_func
    build_dist_from_args(ctx, dist, args)
  File "/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android/pythonforandroid/toolchain.py", line 158, in build_dist_from_args
    build_recipes(build_order, python_modules, ctx,
  File "/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android/pythonforandroid/build.py", line 496, in build_recipes
    recipe.prebuild_arch(arch)
  File "/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android/pythonforandroid/recipes/sdl2_image/__init__.py", line 21, in prebuild_arch
    shprint(sh.Command("./download.sh"))
  File "/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/python-for-android/pythonforandroid/logger.py", line 167, in shprint
    for line in output:
  File "/home/daniil/Документы/PythonProgects/pygame/venv/python/lib/python3.10/site-packages/sh.py", line 915, in next
    self.wait()
  File "/home/daniil/Документы/PythonProgects/pygame/venv/python/lib/python3.10/site-packages/sh.py", line 845, in wait
    self.handle_command_exit_code(exit_code)
  File "/home/daniil/Документы/PythonProgects/pygame/venv/python/lib/python3.10/site-packages/sh.py", line 869, in handle_command_exit_code
    raise exc
sh.ErrorReturnCode_128: 

  RAN: '/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/bootstrap_builds/sdl2/jni/SDL2_image/external/download.sh'

  STDOUT:
fatal: целевой путь «external/jpeg» уже существует и не является пустым каталогом.


  STDERR:

# Command failed: ['/home/daniil/Документы/PythonProgects/pygame/venv/python/bin/python', '-m', 'pythonforandroid.toolchain', 'create', '--dist_name=firstpygame', '--bootstrap=sdl2', '--requirements=python3,pygame,jnius,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf,png,jpeg', '--arch=arm64-v8a', '--arch=armeabi-v7a', '--copy-libs', '--color=always', '--storage-dir=/home/daniil/Документы/PythonProgects/pygame/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a', '--ndk-api=21', '--ignore-setup-py', '--debug']
# ENVIRONMENT:
#     SHELL = '/bin/bash'
#     SESSION_MANAGER = 'local/ubuntu-vmware:@/tmp/.ICE-unix/1209,unix/ubuntu-vmware:/tmp/.ICE-unix/1209'
#     QT_ACCESSIBILITY = '1'
#     SNAP_REVISION = '364'
#     XDG_CONFIG_DIRS = '/etc/xdg/xdg-ubuntu:/etc/xdg'
#     SSH_AGENT_LAUNCHER = 'gnome-keyring'
#     XDG_MENU_PREFIX = 'gnome-'
#     GNOME_DESKTOP_SESSION_ID = 'this-is-deprecated'
#     SNAP_REAL_HOME = '/home/daniil'
#     TERMINAL_EMULATOR = 'JetBrains-JediTerm'
#     SNAP_USER_COMMON = '/home/daniil/snap/pycharm-professional/common'
#     LC_ADDRESS = 'be_BY.UTF-8'
#     GNOME_SHELL_SESSION_MODE = 'ubuntu'
#     LC_NAME = 'be_BY.UTF-8'
#     SSH_AUTH_SOCK = '/run/user/1000/keyring/ssh'
#     TERM_SESSION_ID = 'a8e61bf2-9717-4fed-b829-9a67166fc787'
#     SNAP_INSTANCE_KEY = ''
#     XMODIFIERS = '@im=ibus'
#     DESKTOP_SESSION = 'ubuntu'
#     LC_MONETARY = 'be_BY.UTF-8'
#     BAMF_DESKTOP_FILE_HINT = '/var/lib/snapd/desktop/applications/pycharm-professional_pycharm-professional.desktop'
#     GTK_MODULES = 'gail:atk-bridge'
#     SNAP_EUID = '1000'
#     PWD = '/home/daniil/Документы/PythonProgects/pygame'
#     XDG_SESSION_DESKTOP = 'ubuntu'
#     LOGNAME = 'daniil'
#     XDG_SESSION_TYPE = 'wayland'
#     SYSTEMD_EXEC_PID = '1230'
#     XAUTHORITY = '/run/user/1000/.mutter-Xwaylandauth.J4NMH2'
#     DESKTOP_STARTUP_ID = 'gnome-shell/PyCharm Professional Edition/1230-0-ubuntu-vmware_TIME44849'
#     SNAP_CONTEXT = 'sCgl5_UzkCodqHtmSoxBVv9ZPahGmvJs7jlpyhvgZ2aAAKd3nudv'
#     GJS_DEBUG_TOPICS = 'JS ERROR;JS LOG'
#     HOME = '/home/daniil'
#     USERNAME = 'daniil'
#     IM_CONFIG_PHASE = '1'
#     LANG = 'ru_RU.UTF-8'
#     LC_PAPER = 'be_BY.UTF-8'
#     LS_COLORS = 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:'
#     XDG_CURRENT_DESKTOP = 'ubuntu:GNOME'
#     VIRTUAL_ENV = '/home/daniil/Документы/PythonProgects/pygame/venv/python'
#     WAYLAND_DISPLAY = 'wayland-0'
#     SNAP_ARCH = 'amd64'
#     SNAP_INSTANCE_NAME = 'pycharm-professional'
#     SNAP_USER_DATA = '/home/daniil/snap/pycharm-professional/364'
#     INVOCATION_ID = 'f75b4b1bc7054812b27013d57d52e245'
#     MANAGERPID = '1011'
#     SNAP_REEXEC = ''
#     SNAP_UID = '1000'
#     GJS_DEBUG_OUTPUT = 'stderr'
#     GNOME_SETUP_DISPLAY = ':1'
#     LESSCLOSE = '/usr/bin/lesspipe %s %s'
#     XDG_SESSION_CLASS = 'user'
#     TERM = 'xterm-256color'
#     LC_IDENTIFICATION = 'be_BY.UTF-8'
#     LESSOPEN = '| /usr/bin/lesspipe %s'
#     USER = 'daniil'
#     SNAP = '/snap/pycharm-professional/364'
#     SNAP_COMMON = '/var/snap/pycharm-professional/common'
#     SNAP_VERSION = '2023.3.2'
#     DISPLAY = ':0'
#     SHLVL = '1'
#     SNAP_LIBRARY_PATH = '/var/lib/snapd/lib/gl:/var/lib/snapd/lib/gl32:/var/lib/snapd/void'
#     SNAP_COOKIE = 'sCgl5_UzkCodqHtmSoxBVv9ZPahGmvJs7jlpyhvgZ2aAAKd3nudv'
#     LC_TELEPHONE = 'be_BY.UTF-8'
#     QT_IM_MODULE = 'ibus'
#     LC_MEASUREMENT = 'be_BY.UTF-8'
#     VIRTUAL_ENV_PROMPT = 'python'
#     SNAP_DATA = '/var/snap/pycharm-professional/364'
#     XDG_RUNTIME_DIR = '/run/user/1000'
#     PS1 = ('(python) \\[\\e]0;\\u@\\h: '
 '\\w\\a\\]${debian_chroot:+($debian_chroot)}\\[\\033[01;32m\\]\\u@\\h\\[\\033[00m\\]:\\[\\033[01;34m\\]\\w\\[\\033[00m\\]\\$ ')
#     LC_TIME = 'be_BY.UTF-8'
#     SNAP_NAME = 'pycharm-professional'
#     JOURNAL_STREAM = '8:35518'
#     XDG_DATA_DIRS = '/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop'
#     PATH = '/home/daniil/.buildozer/android/platform/apache-ant-1.9.4/bin:/home/daniil/Документы/PythonProgects/pygame/venv/python/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin'
#     GDMSESSION = 'ubuntu'
#     DBUS_SESSION_BUS_ADDRESS = 'unix:path=/run/user/1000/bus'
#     GIO_LAUNCHED_DESKTOP_FILE_PID = '1990'
#     GIO_LAUNCHED_DESKTOP_FILE = '/var/lib/snapd/desktop/applications/pycharm-professional_pycharm-professional.desktop'
#     LC_NUMERIC = 'be_BY.UTF-8'
#     _ = '/home/daniil/Документы/PythonProgects/pygame/venv/python/bin/buildozer'
#     PACKAGES_PATH = '/home/daniil/.buildozer/android/packages'
#     ANDROIDSDK = '/home/daniil/.buildozer/android/platform/android-sdk'
#     ANDROIDNDK = '/home/daniil/.buildozer/android/platform/android-ndk-r25b'
#     ANDROIDAPI = '31'
#     ANDROIDMINAPI = '21'
# 
# Buildozer failed to execute the last command
# The error might be hidden in the log above this error
# Please read the full log, and search for it before
# raising an issue with buildozer itself.
# In case of a bug report, please add a full log with log_level = 2
