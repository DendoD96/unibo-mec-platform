import queue
import threading
import time
from flask import current_app

task_queue = queue.Queue()


def update(url: str):
	task_queue.put(url)


def manager():
	current_app.logger.debug(f'I am {threading.current_thread()} and i am going to start my job')
	while True:
		item = task_queue.get()
		time.sleep(5)
		current_app.logger.debug(f'I am {threading.current_thread()} and i have finished my job, sending result to {item}')
		task_queue.task_done()
