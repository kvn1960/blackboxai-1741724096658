from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Count
from .models import VehicleBreakdown
from .forms import VehicleBreakdownForm

class DashboardView(TemplateView):
    template_name = 'breakdown/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_breakdowns'] = VehicleBreakdown.objects.count()
        context['status_counts'] = VehicleBreakdown.objects.values('status').annotate(count=Count('id'))
        context['recent_breakdowns'] = VehicleBreakdown.objects.all()[:5]
        return context

class BreakdownListView(ListView):
    model = VehicleBreakdown
    template_name = 'breakdown/breakdown_list.html'
    context_object_name = 'breakdowns'
    paginate_by = 10

class BreakdownDetailView(DetailView):
    model = VehicleBreakdown
    template_name = 'breakdown/breakdown_detail.html'
    context_object_name = 'breakdown'

class BreakdownCreateView(CreateView):
    model = VehicleBreakdown
    form_class = VehicleBreakdownForm
    template_name = 'breakdown/breakdown_form.html'
    success_url = reverse_lazy('breakdown_list')

    def form_valid(self, form):
        messages.success(self.request, 'Breakdown report created successfully.')
        return super().form_valid(form)

class BreakdownUpdateView(UpdateView):
    model = VehicleBreakdown
    form_class = VehicleBreakdownForm
    template_name = 'breakdown/breakdown_form.html'
    success_url = reverse_lazy('breakdown_list')

    def form_valid(self, form):
        messages.success(self.request, 'Breakdown report updated successfully.')
        return super().form_valid(form)

class BreakdownDeleteView(DeleteView):
    model = VehicleBreakdown
    template_name = 'breakdown/breakdown_confirm_delete.html'
    success_url = reverse_lazy('breakdown_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Breakdown report deleted successfully.')
        return super().delete(request, *args, **kwargs)
