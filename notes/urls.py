
from django.urls import path
from notes import views

urlpatterns = [
    
    path('notes/new', views.NoteCreateView.as_view(), name="notes.new"),
    path('notes', views.NoteListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.DetailView.as_view(), name="notes.detail"),
    path('notes/<int:pk>/edit', views.NoteUpdateView.as_view(), name="notes.update"),
    path('notes/<int:pk>/delete', views.NoteDeleteView.as_view(), name="notes.delete")
]
