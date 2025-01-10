from time import sleep
from threading import Thread

class CustomThread(Thread):

    def run(self):
        print("Now .....")

        # Wait for a moment
        sleep(10)

        print("Fuck You")

if __name__ == "__main__":

    # create thread
    thread = CustomThread()

    # Start the thread
    thread.start()

    print("Think of a number and color ...")
    thread.join()