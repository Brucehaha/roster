# Back End Developer Exercise

The aim of this exercise is to simulate real working conditions to provide context for a code/design review session. The follow up review session will focus on your reasons for database/API design and pseudo-code/code implementation. As such it isn’t necessary to build a complete implementation, however having some runnable code is recommended (preferably in Python).

The suggested time to spend on this exercise is at least 2 hours.

### Instructions

- install app on you local machine: 
    1. ```docker-compose build```
    2. ```docker-compose run --rm app sh -c "python manage.py makegrations"```
    3. ```docker-compose run --rm app sh -c "python manage.py migrate"```    
    4. ```docker-compose up```
    5. open link: localhost:8000
    6. login detail: 
          email: admin@admin.com
          password: admin

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
5. no design
6. warning has been created in [app/shift/utils.py](https://bitbucket.org/brucematrix/rosterapp/src/027a934a35de/app/shift/utils.py?at=master "Utils.py") for algorithms

