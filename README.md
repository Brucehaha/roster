# Back End Developer Exercise

The aim of this exercise is to simulate real working conditions to provide context for a code/design review session. The follow up review session will focus on your reasons for database/API design and pseudo-code/code implementation. As such it isn’t necessary to build a complete implementation, however having some runnable code is recommended (preferably in Python).

The suggested time to spend on this exercise is 2 hours.

### Instructions

For this challenge, we are looking for you to create the backend for a a simple rostering application for editing the shifts of employees. For example this application could be used for a small business that works 24/7 to manage the shifts of it's employees to make sure everyone gets adequate days off and doesn't get shifts which are directly back-to-back (eg working on a night shift followed by a morning shift the next day).

We're providing you with two mock data csv files which are typical of the type of data collected:

- Employees: The people who are being rostered
- Shifts: These are the bits of work assigned to employees.

### Challenge

The amount of time you spend on this exercise is up to you, and there are several activities you could consider depending on your strengths:

- Develop some questions (for the rosterer) that support further requirements that you might need in order to more fully specify such an application.
- Create a minimal database schema (or equivalently, ORM model definitions) for the application. You could also demonstrate the effectiveness of your schema by writing a routine to read the sample data from the database.
- Design and/or implement a web API which could be used for communication between the web app's server and client. For example a file upload which validates the csv data before inputting it into the database, or endpoints for manual interactions with the data.
- Describe and/or implement an algorithm which generates an allocation of staff to shifts.

If any of the requirements are unclear feel free to send through questions for clarification or make assumptions - we are not trying to test you on your knowledge of rostering.

### Deliverables

What you deliver is up to you, some suggestions based on our current practices are:

- Python 3
- Django
- Postgresql
- Pseudo-code
- Diagrams (e.g. UML)
- Notes on assumptions or next steps you would take

Please create your solution in a fork off this repo. When you're ready to share your solution with us, email a link to your recruiter or Biarri contact.

On completion, if there are additional things you think you could have done better/did not have enough time to complete, feel free to compile a quick list and bring it to the technical interview to help remind yourself during the discussion.
