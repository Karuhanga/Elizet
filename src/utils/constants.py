ACTIONS = {
    # app specific commands todo customise these from context
    "save":         "ctrl+s",
    "close":        "alt+F4",
    "pause":        "space",
    "play":         "space",
    # system commands
    "lock":         "win+l",
    "select_all":   "ctrl+a",#
    "minimise":     "win+down",#
    "maximize":     "win+up",
    "undo":         "ctrl+z",
    "cut":          "ctrl+x",
    "copy":         "ctrl+c",
    "paste":        "ctrl+v",
    "desktop":      "win+d",
    "screenshot":   "prtsc",#
    "switch":       "win+tab",#
    "sleep":        "ctrl+esc",
    # todo account for other commands
}

LAUNCHER_COMMANDS = {
    "sublime": "subl",
    "firefox": "firefox",
    "chrome": "chromium-browser",
    "vlc": "vlc",
    "files": "nautilus",
}


def get_launcher_commands():
    from app.models import App
    apps = App.objects.all()
    from app.serializers import AppSerializer
    serializer = AppSerializer(apps, many=True)
    commands = {app['name']: app['command'] for app in serializer.data}
    return commands.keys()


def get_launcher_command_action(command):
    from app.models import App
    apps = App.objects.all()
    from app.serializers import AppSerializer
    serializer = AppSerializer(apps, many=True)
    commands = {app['name']: app['command'] for app in serializer.data}
    return commands[command]


## Legacy
COMMAND_SCOPE = (
"save", "pause", "close", "minimise", "lock", "maximise", "undo", "cut", "desktop", "switch", "search", "find", "sleep",
"screenshot", "eliza", "play", "launch",)
def get_music_path():
    return "/home/karuhanga/Music"  # todo this should be a setting
HOME_PATH = "/home/karuhanga/"
