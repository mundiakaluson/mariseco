# Django Powered School Website



[![TravisCI (.org) build status](https://travis-ci.com/mundiakaluson/mariseco.svg?branch=main)]() [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Updates](https://pyup.io/repos/github/mundiakaluson/mariseco/shield.svg)](https://pyup.io/repos/github/mundiakaluson/mariseco/) [![Python 3](https://pyup.io/repos/github/mundiakaluson/mariseco/python-3-shield.svg)](https://pyup.io/repos/github/mundiakaluson/mariseco/) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) ![Maintaner](https://img.shields.io/badge/maintainer-mundiakaluson-blue) [![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://shields.io/) [![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](http://ansicolortags.readthedocs.io/?badge=latest) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 

###### This Django app is configured to use SQLite3 on the development server and Postgres in the Heroku Production server. However, you can configure a local Postgres server which will also run in production. 😊

-------------------------
###### The reason why I made a configuration for two different servers is because the django app might finish up all the space on the free heroku Postgres server. Two Databases, more space ☺️!
--------------------------
#### Features
This website is Django Powered with many different features.
- User Registration with approval system
- Blog system with admin approval
- Comment system with admin approval
- Event management system
- Control Panel for dispalying admin contents within the web interface


> Apart from these features, the web application also has different relationships
> in the database.
#### Relationships
- The ```Blog``` model:
-- ```author = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Article Publisher')``` - which references to the ```User``` model.

- The ```Comment``` model:
-- ```blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)``` - which references to ```Blog``` model to get the current ```blog``` in context which will be posted to the database.

- The ```Profile``` model:
-- ```user = models.OneToOneField(User, on_delete=CASCADE, related_name='user_profile', null=True)``` - This acts as a reference to the Django ```User``` model. By extending this model, we get the ability to add more functionality without  creating a custom ```User``` model which can sometimes be time-consuming.

#### Installation and running the App

```sh
git clone git@github.com:mundiakaluson/mariseco.git
cd mariseco
pipenv install [OR] pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Don't forget to turn ```DEBUG``` to ```True``` for development purpose.

#### Running Tests
> Test directory: ```/main/tests```


I have written minimal tests for the app which cover ```urls``` and some of the models. If you want to modify the tests, use ```python manage.py test``` to run your custom tests.


#### Still Working on...

- Email sending system for registration
- Token generation on successful registration
- Automatic Comment reviewal system
- Automatic article reviewal system


#### Development

Feel free to contribute! I'm open for any changes or improvements. 😀
