from time import sleep
from threading import Thread

def task():

    sleep(10)
    print("Lo gi Ghori Aya jy.......")
    print("This is from another Thread")

if __name__ == "__main__":

    thread = Thread(target=task)
    thread.start()

    print("waiting for other Thread")
    thread.join()
    