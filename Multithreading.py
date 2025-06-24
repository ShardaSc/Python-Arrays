import threading
import time

def walkin():
    time.sleep(8)
    print("Dog walking")

def trashout():
    time.sleep(2)
    print("Keep the trash out")

def mailcheck():
    time.sleep(4)
    print("Mailbox check")

chore1 = threading.Thread(target=walkin())
chore1.start()
chore2 = threading.Thread(target=trashout())
chore2.start()
chore3 = threading.Thread(target=mailcheck())
chore3.start()

print("All chores are completed")
chore1.join()
chore2.join()
chore3.join()
