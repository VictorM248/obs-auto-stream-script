import obspython as obs
from datetime import datetime
import time

START_TIME = "16:40"
STOP_TIME = "16:42"
stream_started = False
stream_stopped = False
last_checked_date = ""

def check_time():
    global stream_started, stream_stopped, last_checked_date

    now = datetime.now()
    today_str = now.strftime("%Y-%m-%d")
    weekday = now.weekday()  # Monday = 0, Sunday = 6
    current_time = now.strftime("%H:%M")

    # Reset flags daily
    if today_str != last_checked_date:
        stream_started = False
        stream_stopped = False
        last_checked_date = today_str

    # Skip Sundays
    if weekday == 6:
        return

    if current_time == START_TIME and not stream_started:
        if not obs.obs_frontend_streaming_active():
            obs.obs_frontend_streaming_start()
            obs.script_log(obs.LOG_INFO, f"Streaming started at {START_TIME}")
            stream_started = True 

    if current_time == STOP_TIME and not stream_stopped and stream_started:
        if obs.obs_frontend_streaming_active():
            obs.obs_frontend_streaming_stop()
            obs.script_log(obs.LOG_INFO, f"Streaming stopped at {STOP_TIME}")
            stream_stopped = True

def script_description():
    return "Automatically starts and stops streaming daily (except Sunday)."

def script_tick(seconds):
    check_time()
