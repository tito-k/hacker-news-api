from django_q.models import Schedule

Schedule.objects.create(
    func='items.tasks.get_latest_published_news',
    name='Get Latest News',
    schedule_type=Schedule.MINUTES,
    minutes=5,
    repeats=-1,
)

Schedule.objects.create(
    func='items.tasks.get_top_level_published_news',
    name='Get Top News',
    schedule_type=Schedule.MINUTES,
    minutes=5,
    repeats=-1,
)
