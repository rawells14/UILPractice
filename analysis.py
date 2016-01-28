import datetime
import time


def this_month(linux_time):
    span = time.time() - linux_time
    return (
        datetime.datetime.fromtimestamp(
            int(span)
        ).strftime('%Y-%m-%d %H:%M:%S')
    )


print(this_month(1204044444))