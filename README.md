### Solution Summary
Create PosgreSQL, Django, Redis, Celery using docker.


## Instructions

### install app on you local machine: 
    1. ```docker-compose build```
    2. ```docker-compose run --rm app sh -c "python manage.py makegrations"```
    3. ```docker-compose run --rm app sh -c "python manage.py migrate"```    
    4. ```docker-compose up```
    5. open link: localhost:8000 or http://127.0.0.1:8000/
    6. login detail: 
        ```email: admin@admin.com```
         ```password: admin```
### After login:
    1. go ```http://127.0.0.1:8000/api/user/token/``` and get a token
    2. if you are using chrome browser, download 'modhearder' plugin.
    3. Put token in modeHeader like:
    4. ```Header: Authorization value: Token c72880baebd93316e499824e1ca68e97aa633027```
### Other link:
    1. create new user after login: http://127.0.0.1:8000/api/user/create/
    2. update my user name or password: http://127.0.0.1:8000/api/user/me/
    3. edit employee, shift, uploading file to create employee, callout pattern: http://127.0.0.1:8000/api/shift/
    4. edit employees: http://127.0.0.1:8000/api/shift/employees/
    5. edit shifts: http://127.0.0.1:8000/api/shift/shifts/
    6. uploads: http://127.0.0.1:8000/api/shift/uploads/
    7. callout function : http://127.0.0.1:8000/api/shift/celery/

###  Required algorithms for :
- Minimum of 10hr overnight rest
- Maximum of 5 days working out of 7 any rolling 7 day window
- Maximum of 5 days working in a row
  
###  Solutions: 
  - see [pp/shift/utils.py](https://bitbucket.org/brucematrix/rosterapp/src/027a934a35de/app/shift/utils.py?at=master "Utils.py") for algorithms

### Challenge

The amount of time you spend on this exercise is up to you, and there are several activities you could consider depending on your strengths:

1. (Required) Create a database schema for the application.
2. Write code for reading and validating the clients csv files into the database.
3. sign and/or implement a web API which could be used for communication between the web app's server and client. For example, endpoints for the manual interactions with the data.
4. Develop some questions (for the rosterer) that support further requirements that you might need in order to more fully specify such an application.
5. Design and/or implement a pattern for calling an external process where a mathematical algorithm can run (these can sometimes run for many minutes)
6. Design and/or implement a pattern for validating shifts and returning or storing warnings



### Challenge Deliverables
1. see [app/core/models.py](https://bitbucket.org/brucematrix/rosterapp/src/master/app/core/models.py?at=master "models.py") for model. 
   see [UML](https://drive.google.com/file/d/1mmIjisNYPS-pSBPlLaCF0pMm-WRjzYk7/view?usp=sharing "models.py") for UML diagram.
   There are differences between models.py and UML database design. In models.py, I did not create store table and shift_choices table. for convienience, store the shift choice and stores 
   directly in shift table.
2. crreate a task table in [app/core/models.py](https://bitbucket.org/brucematrix/rosterapp/src/master/app/core/models.py?at=master "models.py").
   create Upload serializer in [app/shift/employee_serializer.py](https://bitbucket.org/brucematrix/rosterapp/src/master/app/shift/employee_serializer.py?at=master).
   create UploadViewSet in [app/shift/UploadViewSet](https://bitbucket.org/brucematrix/rosterapp/src/master/app/shift/views.py?at=master) to read file and write to database.
3. please see [app/shift/](https://bitbucket.org/brucematrix/rosterapp/src/master/app/shift/?at=master) folder to find the code
4. I do not need create least cost algrithom, I only need to design a pattern to call out and get least cost solution.
   But what is the call back data format is? Can I have a sample. So I can store them to the database.
5.  see [app/core/](https://bitbucket.org/brucematrix/rosterapp/src/master/app/core/), ```celery_serializer.py,  models.py, tasks.py```.
    and ```settings.py, rosterapp/roster/__init__.py, rosterapp/src/master/app/shift/urls.py ```
6. warning has been created in [app/shift/utils.py](https://bitbucket.org/brucematrix/rosterapp/src/027a934a35de/app/shift/utils.py?at=master "Utils.py") for algorithms

