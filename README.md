
# Productive App API #

[Click here to visit the live frontend page.](https://productive-app-ui-80cca270cd7d.herokuapp.com/)

[Click here to visit the Github frontend repository.](https://github.com/TamasSomi/productiveapp-ui)

[Click here to visit the API Github repository.](https://github.com/TamasSomi/productive-app)

[Click here to visit the live API page.](https://productive-app-060b4c85d875.herokuapp.com/)

![Screenshot of the home page.](/docs/api-homepage.png)

[Click here to read the API user stories on Github Issues](https://github.com/TamasSomi/productive-app/issues)

[Click here to read the frontend user stories on Github Issues](https://github.com/users/TamasSomi/projects/7)

## Objective ##

The objective of the page is that people are able to create tasks with deadline so it can help to manage the dayli tasks.
The site allows people to add notes to the tasks so they can use notes like labels and they can add images as well.
Those could be motivational or something else they would like to add.

## Database Designs ##

### Profile Model ###

Model representing user profiles.

Attributes:

* owner: One-to-One relationship with the User model, linking each profile to a user.
* created_at: DateTimeField representing the timestamp when the profile was created.
* updated_at: DateTimeField representing the timestamp of the last update to the profile.
* name: CharField for storing the name of the user (optional, can be blank).
* content: TextField for additional content or information about the user (optional, can be blank).
* image: ImageField for storing the profile image, with a default image path.

ordering:

* Specifies the default ordering for queries, displaying profiles in descending order of creation.

Methods:

* Returns a string representation of the profile, indicating the owner's username.

Usage:

* Used to store additional information about users, such as names, profile images, and content.

### Task Model ###

Model representing a task in the system.

Attributes:

* owner: ForeignKey to the User model, representing the user who owns or created the task.
* created_at: DateTimeField representing the timestamp when the task was created.
* updated_at: DateTimeField representing the timestamp of the last update to the task.
* title: CharField for storing the title of the task.
* content: TextField for additional content or information about the task (optional).
* deadline: DateTimeField representing the deadline of the task (optional).
* image: ImageField for storing an image related to the task (optional).
* image_filter: CharField representing the selected image filter for the task's image.

ordering:

* Specifies the default ordering for queries, displaying tasks in descending order of creation.

Methods:

* Returns a string representation of the task, including its ID and title.

Usage:

* Used to store information about tasks, including ownership, timestamps, and associated data.

### Note Model ###

Represents a Note associated with a specific User and Task.

Attributes:

* owner (User): The User who owns or created the Note.
* task (Task): The Task to which the Note is related.
* created_at (DateTime): The timestamp when the Note was created, automaticallyset on creation.
* updated_at (DateTime): The timestamp when the Note was last updated, automatically updated on each modification.
* content (TextField): The textual content of the Note.

* ordering: ['-created_at']
 Defines the default sorting order for queries, displaying Notes in descending order of creation.

Methods:

* Returns a string representation of the Note based on its content.

Usage:

* Each Note instance is associated with a specific User and Task, storing relevant information in the content field.
* The created_at and updated_at fields provide timestamps for tracking the Note's lifecycle.

![A screenshot of data chart](/docs/data-chart.png)

## Manual testing ##

* See the tests in the [frontend app's readme!](https://github.com/TamasSomi/productiveapp-ui)

## Validation ##

* Files passed the [pep8 validator](https://www.pythonchecker.com/) without error.

## Features ##

* When you first enter the API site, you are directed to the Root Route hompage, with a message welcoming you to the API.

![Screenshot of the home page.](/docs/api-homepage.png)

* Profile data:

![Screenshot of the home page.](/docs/profile-data.png)

* Note data:

![Screenshot of the home page.](/docs/notes-data.png)

* Task data:

![Screenshot of the home page.](/docs/task-data.png)

## Technology Used ##

* [DjangoAllAuth](https://pypi.org/project/django-allauth/)
* [Github](https://github.com/)
* [Codeanywhere](https://codeanywhere.com/)
* [Heroku](https://dashboard.heroku.com/)
* [ElephantSql](https://www.elephantsql.com/)

### Languages and Frameworks ###

* [Python](https://www.python.org/)
* [Django Rest](https://www.django-rest-framework.org/)

## Deployment Steps: ##

Create a GitHub repository using the Code Institute's codeanywhere template.
Open the repository in the Gitpod/codeanywhere Editor by clicking the button.

* Install Django and necessary libraries:
pip3 install 'django<4' gunicorn
pip3 install 'dj_database_url psycopg2'
pip3 install 'dj3-cloudinary-storage'

* Create a requirements file: pip3 freeze --local > `requirements.txt`
* Create the project: django-admin startproject YOUR_PROJECT_NAME .
* Create applications: python3 manage.py startapp APP_NAME

* Add applications to settings.py in the INSTALLED_APPS list.

* Migrate and run the server:
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

* Deploy to Heroku:
Sign in to Heroku, click 'New' to create a new app.
Choose a unique app name, region, and click 'Create app.'

* Connect the database:
Go to ElephantSQL dashboard, create a new database instance.
Fill in details and click 'Create Instance.'
Copy the Database URL and go back to Heroku.
In Heroku app settings, click 'Reveal Config Vars,' create a variable named DATABASE_URL, and paste the copied URL.

* Create an env.py file in the app in the top level directory.

* Heroku Config Vars:
Create SECRET_KEY variable.
Use the same key as in `env.py`.
Add `env.py` to .gitignore.

* Update `settings.py`:
Import required modules.
Replace insecure secret key.
Comment out old database settings.
Add DATABASE_URL from env file.
Cloudinary Setup:

* Create Cloudinary account.
Copy API Environment Variable.
Add Cloudinary URL to `env.py`.
Add Cloudinary URL to Heroku Config Vars.
Settings.py Updates:

Add Cloudinary libraries to INSTALLED_APPS.
Configure static file storage in settings.
ALLOWED_HOSTS:

* Add Heroku app and localhost to ALLOWED_HOSTS.

* Create *Procfile with web: gunicorn PROJ_NAME.wsgi.

* Git Commands:
git add .
git commit -m "Deployment Commit"
git push

* Heroku Deployment:
Top of Heroku settings, click 'Deploy' tab.
Select 'Github' as deployment method.
Connect to repository.
Deploy branch manually.

* GitHub Repository Forking:
On GitHub, locate repository.
Click 'Fork' to create a copy.

* Cloning and Setup:
Copy repository URL.
Open Git Bash and use git clone.
Install requirements: pip3 install -r `requirements.txt`.
Set up environment file, don't push to GitHub.
Run migrations: python3 `manage.py` migrate.
Start local server: python3 `manage.py` runserver.

## Credit ##

* The project were built by following Code Institute's drf_API project tailored
to this projects needs.

* Found [this](https://stackoverflow.com/questions/28061550/model-datetime-field-validation-for-fields-with-auto-now)
for date_time validation.

* I used [Lucid](https://lucid.app/documents#/documents?folder_id=recent) for the data chart.