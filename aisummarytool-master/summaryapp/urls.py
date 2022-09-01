from django.urls import path, include
from django.contrib.auth import views as auth_views
from summaryapp.views import RootView, generate_summary, SummaryListView, convert_csv

urlpatterns = [
	path('', RootView.as_view(), name='root'),
	path('login/', auth_views.LoginView.as_view(), name="login"),
	path('logout/', auth_views.LogoutView.as_view(), name="logout"),
	path('accounts/', include('django.contrib.auth.urls')),
	path('summary/', SummaryListView.as_view(), name='summary-list'),
	path('generate_summary/', generate_summary, name='generate-summary'),
	path('convert_csv/', convert_csv, name='convert-csv'),
	]
