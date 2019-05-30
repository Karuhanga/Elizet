import os

from src.one_start.actions import resolve_keyword_action, launch_action, \
    search_action, find_action, music_action, open_action, time_action
from src.one_start.snowboy import HotWordDetector
from src.utils.constants import ACTIONS


def build_path(param):
    # todo we can do something fancy here like first check for a .pmdl
    #   before falling back to a .umdl
    return os.path.abspath("src/one_start/data/" + param + ".umdl")


def build_quick_action_routines(actions):
    return [
        build_routine(action, resolve_keyword_action(action))
        for action in actions
    ]


def build_routine(name, callback, sensitivity=0.5):
    return {
            "name": name,
            "model": build_path(name),
            "callback": callback,
            "sensitivity": sensitivity
        }


def build_wake_up_detector(trigger, action):
    routines = []
    # test routine
    routines.append(build_routine(trigger, action))
    return HotWordDetector(routines)


def build_detector(stop_trigger, stop_action):
    routines = []
    # stop routine
    routines.append(build_routine(stop_trigger, stop_action))
    # quick action routines
    routines.extend(build_quick_action_routines(ACTIONS.keys()))
    # open
    routines.append(build_routine("launch", launch_action))
    # search
    routines.append(build_routine("search", search_action))
    # find
    routines.append(build_routine("find", find_action))
    # music
    routines.append(build_routine("music", music_action))
    # open
    routines.append(build_routine("open", open_action))
    # time
    routines.append(build_routine("time", time_action, sensitivity=0.6))

    return HotWordDetector(routines)
