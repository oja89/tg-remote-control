################
Surveillance Bot
################

Surveillance Bot is a Telegram bot that uses a camera (such a webcam) for
surveillance. Photos and videos can be taken from the camera and sent via
Telegram instantly. Those actions can be triggered by commands sent by the
user or when motion is detected.

All files in this project are covered under the `GPLv3 LICENSE
<http://www.gnu.org/licenses/gpl.html>`_, if you modify this project in any
way you MUST publish the changes you made and submit your contribution to the
community under the same license.


FORK MODIFICATIONS
******************

Added option to control Philips Hue Smart Plug with Bluetooth.
Dropped dockerization.


Features
********

- Motion detection.
- Real time notification.
- Motion tracking.
- Photo and video capture on demand.
- Bot configuration via telegram chat.
- Timestamp in photos and videos.
- H264 video encoding (when codec is available).
- Multi-platform: Linux, Windows and MacOS.
- NEW IN THIS FORK: Control of Hue Plug

Requirements
************
- python
- OpenCV
- python-telegram-bot
- NEW: bleak

Quick-start (camera only)
***********

1. Install package with ``pip``::

    DONT
    (if you use pip install surveillance_bot you will not get these modifications)

2. Set application configuration variables (see `Advanced configuration`_)::

    export BOT_API_TOKEN=<api_token>
    export AUTHORIZED_USER=<username>

3. Run script::

    py main.py

Add power control
*****************

pip install bleak

Advanced configuration
**********************
The application is configured using this environment variables:
  - ``BOT_API_TOKEN`` *(mandatory)*

    The `Telegram bot API <https://core.telegram.org/bots/api>`_ token of a
    telegram bot.

  - ``AUTHORIZED_USER`` *(mandatory)*

    The `Telegram username
    <https://telegram.org/faq#q-what-are-usernames-how-do-i-get-one>`_
    (without @) of the user authorized to interact with the bot.

  - ``PERSISTENCE_DIR``

    If this variable is set the bot configuration (set via telegram chat) will
    persist on disk into a file placed in this directory.

  - ``LOG_LEVEL``

    Global log level for application and libraries using the
    `python standard logging library
    <https://docs.python.org/3/library/logging.html#logging-levels>`_.

  - ``BOT_LOG_LEVEL``

    Specific Bot application log level.

H264 Encoding
*************

This application generates MP4 video files, if H264 codec is available it will
use it to generate smaller files.

The OpenCV library provided by the PyPi package (installed with pip)
`doesn't have H264 support
<https://github.com/skvark/opencv-python/issues/81#issuecomment-376166468>`_
so if you wish to use H264 encoding you have to do a manual build or use a
precompiled library with H264 support (some distributions, like Ubuntu, have
OpenCV library supporting this codec).

For Windows 10, you can get the .dll from <https://github.com/cisco/openh264/releases/tag/v1.8.0>

