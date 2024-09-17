from django.urls import path
from .views import leads_list, lead_detail, lead_create, lead_update, lead_delete
from .views import LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name="leads_list"),
    path('create/', LeadCreateView.as_view(), name="lead_create"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead_detail"),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead_update"),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="lead_delete")
]