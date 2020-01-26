"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from authors import views as author_views
from books import views as book_views
from students import views as student_views
from issues import views as issue_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', views.dashboard,name="dashboard"),

    path('authors', author_views.index,name="author_index"),
    path('author/create', author_views.create,name="author_create"),
    path('author/save', author_views.store,name="author_create"),
    path('author/edit/<int:id>', author_views.edit,name="author_edit"),
    path('author/update/<int:id>', author_views.update,name="author_update"),
    path('author/delete/<int:id>', author_views.destroy,name="author_delete"),

    path('books', book_views.index,name="book_index"),
    path('book/create', book_views.create,name="book_create"),
    path('book/save', book_views.store,name="book_create"),
    path('book/edit/<int:id>', book_views.edit,name="book_edit"),
    path('book/update/<int:id>', book_views.update,name="book_update"),
    path('book/delete/<int:id>', book_views.destroy,name="book_delete"),

    path('students', student_views.index,name="student_index"),
    path('student/create', student_views.create,name="student_create"),
    path('student/save', student_views.store,name="student_create"),
    path('student/edit/<int:id>', student_views.edit,name="student_edit"),
    path('student/update/<int:id>', student_views.update,name="student_update"),
    path('student/delete/<int:id>', student_views.destroy,name="student_delete"),

    path('issues', issue_views.index,name="issue_index"),
    path('issue/create', issue_views.create,name="issue_create"),
    path('issue/save', issue_views.store,name="issue_create"),
    path('issue/edit/<int:id>', issue_views.edit,name="issue_edit"),
    path('issue/update/<int:id>', issue_views.update,name="issue_update"),
    path('issue/delete/<int:id>', issue_views.destroy,name="issue_delete"),
]
