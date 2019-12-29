



1. Create a project


```python

django start-admin startproject Student

```


2. Create an app names **information**


```pythoon

python manage.py startapp information

```



3. In settings.py register your app *information*


**Before**


```python


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```


**After**

> information named app is registered now

```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'information',
]

```



4. Create urls.py in information app


```python

from django.urls import path

from . import views

urlpatterns = [
    path(),
]
```



5. Register information apps url in projects urls.py


**Before**

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

```


**After**

```python

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('information.urls')),
]

```





6. In informations models.py create a new model names Student with given
attributes.

> name\
  age\
  school\
  description



```python

from django.db import models

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(default=0,blank=True)
    school=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.name




```


---


# Important commands to save the changes of models.py


1. ```python python manage.py makemigrations```

2. ```python python manage.py migrate```

3. ```python manage.py createsuperuser```




---


7. In admin.py import model Student and register it.

```python
from django.contrib import admin

# Register your models here.


from .models import Student


admin.site.register(Student)
```


---

1. Create index.html and studentform.html file within templates folder


---


8. Now create a view named index in information app


```python
from django.shortcuts import render,redirect

# Create your views here.

from .models import Student

def index(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,'index.html',context)


```


**In index.html file use a for loop so that all the students can be displayed**

```html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

    {% for student in students %}
        <h1> {{ student.name }} </h1>
        <h3>{{ student.age }}</h3>
        <h2>{{ student.school }}</h2>
        <h4>{{ student.description }}</h4>
        <hr/>
    {% endfor %}
</body>
</html>
```


---

1. Student is imported from .models

2. instance or better to say object of Student class is made.

3. A dictionary named context is made and students object is added as key value 
pair.


4. Eventually the render() method takes three arguments.

  1. request 
  2. A template i.e HTML file which is index.html in this case.
  
  > In html file we just used a for loop to display information within\
    h1,h2 tags
  
  
  3. A dictionary  which is *context* in this case.





---




9. In views.py add a new view names create ,this will provide a form
that will help to create enter the data of new students.

```python


def create(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        school=request.POST['school']
        description=request.POST['description']
        newstudent=Student.objects.create(name=name,age=age,school=school,description=description)
        newstudent.save()
        return redirect('index')
    else:
        print(' something is wroing')

    return render(request,'studentform.html',{})

```









10. The views.py file will look like this.


```python
from django.shortcuts import render,redirect

# Create your views here.

from .models import Student

def index(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,'index.html',context)



def create(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        school=request.POST['school']
        description=request.POST['description']
        newstudent=Student.objects.create(name=name,age=age,school=school,description=description)
        newstudent.save()
        return redirect('index')
    else:
        print(' something is wroing')

    return render(request,'studentform.html',{})
```


11. It's time for studentform.html file


```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form method="post">
        {% csrf_token %}

        <input type="text" name="name" >
        <input type="number" name="age">
        <input type="text" name="school">
        <input type="text" name="description">
        <input type="submit" value="submit">

    </form>
</body>
</html>
```




12. In urls.py of information app import both the views that we created

```python
from django.urls import path

from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
]
```




13. 127.0.0.1 displays all the students

14. 127.0.0.1/create will display the form 