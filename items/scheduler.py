from django.utils import timezone
from django_q.models import Schedule

current_date = timezone.now()
fixed_time = current_date.replace(hour=0, minute=0, second=0, microsecond=0)


Schedule.objects.create(
    func='items.tasks.get_latest_published_news',
    name='Get Latest News',
    schedule_type=Schedule.MINUTES,
    minutes=5,
    repeats=-1,
    next_run=fixed_time
)
