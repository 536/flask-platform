import datetime

from .extensions import scheduler


@scheduler.task(
    "interval",
    id="job01",
    seconds=10,
    max_instances=1,
    start_date="2000-01-01 12:19:00",
    args=('job01', )
)
def job01(name, *args, **kwargs):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("job01: {}".format(name), now)
    with scheduler.app.app_context():
        print(scheduler.app.config)


def job02(name, *args, **kwargs):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("job02: {}".format(name), now)
