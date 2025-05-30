from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Create teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')
        team1.members.append(user1)
        team1.members.append(user2)
        team2.members.append(user3)
        team1.save()
        team2.save()

        # Create workouts
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        workout2 = Workout.objects.create(name='Running', description='Run 1 mile')

        # Create activities
        Activity.objects.create(user=user1, activity_type='Pushups', duration=10)
        Activity.objects.create(user=user2, activity_type='Running', duration=20)
        Activity.objects.create(user=user3, activity_type='Pushups', duration=15)

        # Create leaderboard
        Leaderboard.objects.create(team=team1, points=30)
        Leaderboard.objects.create(team=team2, points=15)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
