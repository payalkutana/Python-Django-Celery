from celery import shared_task
from time import sleep

@shared_task
def first_shedule_task(args1):
    print("Schedule Task 1 Called")
    sleep(10)
    return args1
    
@shared_task
def second_schedule_task(args1):
    print("Schedule Task 2 Called")
    sleep(10)
    return args1