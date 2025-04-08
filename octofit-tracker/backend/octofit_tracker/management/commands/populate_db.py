from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate Users
        users = [
            {"username": "john_doe", "email": "john@example.com"},
            {"username": "jane_smith", "email": "jane@example.com"},
        ]
        for user_data in users:
            User.objects.create(**user_data)

        # Populate Teams
        teams = [
            {"name": "Team Alpha"},
            {"name": "Team Beta"},
        ]
        for team_data in teams:
            Team.objects.create(**team_data)

        # Populate Activities
        activities = [
            {"name": "Running", "calories_burned": 300},
            {"name": "Cycling", "calories_burned": 250},
        ]
        for activity_data in activities:
            Activity.objects.create(**activity_data)

        # Populate Leaderboard
        leaderboards = [
            {"user_id": 1, "team_id": 1, "points": 100},
            {"user_id": 2, "team_id": 2, "points": 150},
        ]
        for leaderboard_data in leaderboards:
            Leaderboard.objects.create(**leaderboard_data)

        # Populate Workouts
        workouts = [
            {"user_id": 1, "activity_id": 1, "duration_minutes": 30},
            {"user_id": 2, "activity_id": 2, "duration_minutes": 45},
        ]
        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
