from django.urls import path, include
from hospital import views

urlpatterns = [
    # Path to render the Homepage
    path('', views.frontend, name='frontend'),
    # Path LOGIN/LOGOUT
    path('login/', include('django.contrib.auth.urls')),




    # =============== #
    # BACKEND SECTION #
    # =============== #

    # Path to access the backend page
    path('backend/', views.backend, name='backend'),
    # Path to add patient
    path('add_patient', views.add_patient, name='add_patient'),
    # Path to delete patient
    path('delete_patient/<str:patient_id>', views.delete_patient, name='delete_patient'),
    # Path to patient
    path('patient/<str:patient_id>', views.patient, name='patient'),
    # Path to add patient
    path('edit_patient', views.edit_patient, name='edit_patient'),
]
