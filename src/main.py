from src.keywords.actions import snow_boy_action
from src.keywords.main import build_detector, build_wake_up_detector

wake_up_detector = None
detector = None


def listen_for_wake_up_word():
    global wake_up_detector
    if detector:
        detector.terminate()
    wake_up_detector = build_wake_up_detector("snowboy", listen_for_keyword)
    wake_up_detector.listen()


# todo: We might choose to do this asynchronously after, say, a minute
def stop_keyword_capture():
    print("Cool.")
    listen_for_wake_up_word()


def listen_for_keyword():
    global detector
    wake_up_detector.terminate()
    snow_boy_action()
    detector = build_detector("snowboy", stop_keyword_capture)
    try:
        detector.listen("Waiting for action...")
    except Exception as e:
        print("Issue: " + str(e))
    finally:
        listen_for_wake_up_word()


if __name__ == "__main__":
    listen_for_wake_up_word()
