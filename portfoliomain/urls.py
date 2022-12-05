from django.contrib import admin
from django.urls import path, include



from weather import views as weather
from todo import views as todo
from stopwatch import views as stopwatch
from tictactoe import views as tictactoe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('weather-api', weather.weather, name='weather' ),
    path('todo-app', todo.todo, name='todo-app' ),
    path('tictactoe-game', tictactoe.tictactoe, name='tictactoe' ),
    path('stopwatch', stopwatch.stopwatch, name='stopwatch' ),
    path('hospital/', include('hospital.urls')),
    path('CRUD/', include('CRUD.urls')),
]
