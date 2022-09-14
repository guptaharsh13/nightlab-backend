from celery import shared_task
import time


@shared_task(bind=True)
def task(self):
    time.sleep(5)
    print("done: task")
    return True
