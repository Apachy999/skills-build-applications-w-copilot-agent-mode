from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create Users
        users = [
            User(email='tony@stark.com', name='Tony Stark', team='marvel', is_superhero=True),
            User(email='steve@rogers.com', name='Steve Rogers', team='marvel', is_superhero=True),
            User(email='bruce@wayne.com', name='Bruce Wayne', team='dc', is_superhero=True),
            User(email='clark@kent.com', name='Clark Kent', team='dc', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create Workouts
        workouts = [
            Workout(name='Super Strength', description='Heavy lifting', suggested_for='marvel'),
            Workout(name='Flight Training', description='Aerial maneuvers', suggested_for='dc'),
        ]
        Workout.objects.bulk_create(workouts)

        # Create Activities
        tony = User.objects.get(email='tony@stark.com')
        bruce = User.objects.get(email='bruce@wayne.com')
        Activity.objects.create(user=tony, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='swim', duration=45, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=200, rank=1)
        Leaderboard.objects.create(user=bruce, score=180, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
