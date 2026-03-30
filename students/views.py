from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all().order_by('name')
    return render(request, 'students/list.html', {'students': students})

def student_add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student added successfully!')
        return redirect('student_list')
    return render(request, 'students/form.html', {'form': form, 'title': 'Add Student'})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, f'"{student.name}" updated successfully!')
        return redirect('student_list')
    return render(request, 'students/form.html', {'form': form, 'title': 'Edit Student'})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        name = student.name
        student.delete()
        messages.warning(request, f'"{name}" has been deleted.')
        return redirect('student_list')
    return render(request, 'students/confirm_delete.html', {'student': student})
