from libs.snowboy import snowboydecoder
import signal


class HotWordDetector:
    interrupted = False
    sensitivity = 0.5
    routines = {}
    detector = None

    def __init__(self, routines):
        # capture SIGINT signal, e.g., Ctrl+C
        signal.signal(signal.SIGINT, self.signal_handler)
        self.sensitivity = [0.5]*len(routines)
        self.routines = routines

    def signal_handler(self, signal, frame):
        self.interrupted = True

    def interrupt_callback(self):
        return self.interrupted

    def listen(self, message="Listening..."):
        print(message)
        self.detector = snowboydecoder.HotwordDetector(
            [routine['model'] for routine in self.routines],
            sensitivity=self.sensitivity
        )
        self.detector.start(
            detected_callback=[routine['callback'] for routine in self.routines],
            interrupt_check=self.interrupt_callback,
            sleep_time=0.03
        )

    def terminate(self):
        self.detector.terminate()
