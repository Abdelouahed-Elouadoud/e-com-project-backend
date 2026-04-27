from celery import shared_task
import time

@shared_task
def test_task():
    print("Début de la tâche...")
    time.sleep(5)
    print("Fin de la tâche")
    return "OK"