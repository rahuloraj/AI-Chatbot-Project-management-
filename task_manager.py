from utils.db_utils import save_task

def log_task_update(task_update):
    save_task(task_update)
    print("✅ Task update saved.")