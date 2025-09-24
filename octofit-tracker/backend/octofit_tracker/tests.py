from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_create_activity(self):
        activity = Activity.objects.create(name='Test Activity', user_email='test@example.com')
        self.assertEqual(activity.name, 'Test Activity')
        self.assertEqual(activity.user_email, 'test@example.com')

    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=10)
        self.assertEqual(leaderboard.team, 'Test Team')
        self.assertEqual(leaderboard.points, 10)

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', difficulty='Easy')
        self.assertEqual(workout.name, 'Test Workout')
        self.assertEqual(workout.difficulty, 'Easy')
