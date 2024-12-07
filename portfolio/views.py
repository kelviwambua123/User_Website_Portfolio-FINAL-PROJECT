from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Feedback, ContactMessage  # Ensure ContactMessage is imported
from .forms import ProjectForm, FeedbackForm, ContactForm  # Ensure ContactForm is imported
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

@login_required  # Ensures the user is logged in
def project_list(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'portfolio/project_list.html', {'projects': projects})

@login_required  # Ensures the user is logged in
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)  # Ensure user owns the project
    feedbacks = project.feedbacks.all()  # Get all feedback related to the project

    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback = feedback_form.save(commit=False)
            feedback.project = project
            feedback.user = request.user  # Set user if logged in
            feedback.save()
            messages.success(request, 'Your feedback has been submitted!')
            return redirect('portfolio:project_detail', pk=project.pk)
    else:
        feedback_form = FeedbackForm()

    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'feedbacks': feedbacks,
        'feedback_form': feedback_form,
    })

@login_required  # Ensures the user is logged in
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, 'Project created successfully!')
            return redirect('portfolio:project_list')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/project_form.html', {'form': form})

@login_required  # Ensures the user is logged in
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('portfolio:project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/project_form.html', {'form': form})

@login_required  # Ensures the user is logged in
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == "POST":
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('portfolio:project_list')
    return render(request, 'portfolio/project_confirm_delete.html', {'project': project})

# Contact section
def contact_view(request, project_id=None):
    project = None
    if project_id:
        project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.project = project  # Associate with the project if provided
            contact_message.save()

            # Send email notification
            send_mail(
                'New Contact Message',
                f"Message from {contact_message.name} ({contact_message.email}):\n\n{contact_message.message}",
                'kelvinmutuku84@gmail.com',  #  email
                ['kelvinmutuku84@gmail.com'],  #  email
                fail_silently=False,
            )

            messages.success(request, 'Your message has been successfully sent. We will get back to you soon!')
            return redirect('portfolio:project_detail', pk=project.id if project else None)

    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form, 'project': project})
