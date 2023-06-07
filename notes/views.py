from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from .models import Note
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class NoteDeleteView(DeleteView):

    model = Note
    success_url = '/smart/notes'
    template_name = "notes/notes_delete.html"

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NotesForm
    success_url = '/smart/notes'

class NoteCreateView(CreateView, LoginRequiredMixin):
    model = Note
    form_class = NotesForm
    success_url = '/smart/notes'
    login_url = '/login'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/login'
    def get_queryset(self):
        return self.request.user.notes.all()

class DetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/detail.html'

def detail(request, pk):
    try: 
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/detail.html', {'note': note})