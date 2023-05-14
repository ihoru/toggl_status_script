# Search for "API Token" at https://track.toggl.com/profile
TOGGL_TRACK_API_TOKEN = ''

try:
    # to overwrite all settings with local once
    from local_settings import *
except ImportError:
    pass
