from django.urls import path
from notes.views import CreateNoteView, ListNotesView, DeleteNoteView

urlpatterns = [
    path('create/', CreateNoteView.as_view(), name='create_note'),
    path('list/', ListNotesView.as_view(), name='list_notes'),
    path('delete/<int:pk>/', DeleteNoteView.as_view(), name='delete_note'),
]
