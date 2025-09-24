from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    import os
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    base_url = request.build_absolute_uri('/')
    if codespace_name:
        base_url = f'https://{codespace_name}-8000.app.github.dev/api/'
    else:
        base_url = base_url.rstrip('/') + '/api/'
    return Response({
        'users': base_url + 'users/',
        'teams': base_url + 'teams/',
        'activities': base_url + 'activities/',
        'leaderboards': base_url + 'leaderboards/',
        'workouts': base_url + 'workouts/',
    })
