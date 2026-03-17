from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    CommentForm,
    MentorProfileForm,
    NoteForm,
    QuestionForm,
    SignUpForm,
)
from .models import MentorProfile, Note, Question

def home(request):
    questions = Question.objects.all().order_by('-created_at')
    notes = Note.objects.all().order_by('-uploaded_at')[:5]
    mentors = MentorProfile.objects.filter(is_available=True)[:5]
    return render(
        request,
        'home.html',
        {'questions': questions, 'notes': notes, 'mentors': mentors},
    )

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'ask.html', {'form': form})


@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    comment_form = CommentForm(prefix='comment')

    if request.method == 'POST':
        if 'submit_comment' in request.POST:
            comment_form = CommentForm(request.POST, prefix='comment')
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.question = question
                comment.user = request.user
                comment.save()
                return redirect('question_detail', question_id=question.id)

    context = {
        'question': question,
        'comment_form': comment_form,
    }
    return render(request, 'question_detail.html', context)


@login_required
def notes_list(request):
    notes = Note.objects.all().order_by('-uploaded_at')
    return render(request, 'notes_list.html', {'notes': notes})


@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploaded_by = request.user
            note.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'upload_note.html', {'form': form})


@login_required
def mentor_matching(request):
    keyword = request.GET.get('q', '').strip()
    mentors = MentorProfile.objects.filter(is_available=True).select_related('user')
    if keyword:
        mentors = mentors.filter(
            Q(expertise__icontains=keyword)
            | Q(department__icontains=keyword)
            | Q(bio__icontains=keyword)
            | Q(user__username__icontains=keyword)
        )
    return render(request, 'mentor_matching.html', {'mentors': mentors, 'keyword': keyword})


@login_required
def create_or_update_mentor_profile(request):
    profile, _created = MentorProfile.objects.get_or_create(
        user=request.user,
        defaults={'department': 'General', 'expertise': 'General guidance'},
    )
    if request.method == 'POST':
        form = MentorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('mentor_matching')
    else:
        form = MentorProfileForm(instance=profile)
    return render(request, 'mentor_profile_form.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def search(request):
    query = request.GET.get('q', '').strip()
    notes = Note.objects.none()
    questions = Question.objects.none()
    mentors = MentorProfile.objects.none()
    if query:
        notes = Note.objects.filter(
            Q(title__icontains=query) | Q(subject__icontains=query)
        ).order_by('-uploaded_at')
        questions = Question.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).order_by('-created_at')
        mentors = MentorProfile.objects.filter(
            Q(user__username__icontains=query)
            | Q(department__icontains=query)
            | Q(expertise__icontains=query)
            | Q(bio__icontains=query)
        ).select_related('user')
    context = {
        'query': query,
        'notes': notes,
        'questions': questions,
        'mentors': mentors,
    }
    return render(request, 'search_results.html', context)
