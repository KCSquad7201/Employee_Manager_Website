from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views
urlpatterns = [
    path('dashboard', views.dashboardView, name='ndashboard'),
    path('add-task', views.AddTaskView, name='nadd-task'),
    path('get_today_tasks', views.GetTodayTasksView, name='get_today_tasks'),
    path('get_yest_tasks', views.GetYestTasksView, name='get_yest_tasks'),
    path('get_weekly_tasks', views.GetWeeklyTasksView, name='get_weekly_tasks'),
    path('profile', views.ProfileView, name='nprofile')
]