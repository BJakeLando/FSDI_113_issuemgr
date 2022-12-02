from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Issue, Status, Priority

class BoardView(ListView):
    template_name = "issues/board.html"
    model = Issue

    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        to_do_status = Status.objects.get(name="to do")
        in_p_status = Status.objects.get(name="in progress")
        done_status = Status.objects.get(name="done")

        context["to_do_list"] = Issue.objects.filter( 
            status = to_do_status).order_by("created_on").reverse()
        context["in_p_list"]= Issue.objects.filter( 
            status = in_p_status).order_by("created_on").reverse()
        context["done_list"]= Issue.objects.filter( 
            status = done_status).order_by("created_on").reverse()

        return context


class IssueDetailView(DetailView):
    template_name= "issues/detail.html"
    model = Issue

class IssueCreateView(CreateView):
    template_name= "issues/new.html"
    model= Issue
    fields = ["summary", "description", "priority","status","assignee"]

    def form_valid(self, form):
        form.instance.reporter= self.request.user
        return super().form_valid(form)
        
class IssueUpdateView(UpdateView):
    template_name= "issues/edit.html"
    model = Issue
    fields = ["summary", "description", "priority","status","assignee"]

    def test_fun(self):
        issue_obj = self.get_object()
        return self.request.user == issue_obj.reporter

class IssueDeleteView(DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    succes_url = reverse_lazy('board')

    def test_fun(self):
        issue_obj = self.get_object()
        return self.request.user == issue_obj.reporter


