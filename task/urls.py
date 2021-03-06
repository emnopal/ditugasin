from django.urls import path

from .views import (
    index_view,
    detail_view,
    create_view,
    update_view,
    delete_view,
    to_csv,
    search
)

from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d%m%Y%H%M%S") # get current date and time

app_name = 'task'
urlpatterns = [
    path('', index_view, name='index'),
    path('<int:task_id>', detail_view, name='detail'),
    path('create', create_view, name='create'),
    path('edit/<int:task_id>', update_view, name='edit'),
    path('delete/<int:task_id>', delete_view, name='delete'),
    path(f'to_csv/{dt_string}.csv', to_csv, name='to_csv'),
    path('search/', search, name='search'),
]
