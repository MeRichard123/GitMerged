# GitMerged

This is a tinder App for Developers build with Django.

## Features
- Users can make and account an login 
- Then you fill out their profile details -> tech stack etc.. 
- Users can browse and filter other users
- They can also express intrest towards other users with a heart
- If both users express intrest it's match
- Users can send each other messages and view eachothers profiles 
- Users can block each other

This Idea came from the [RTC Project Ideas Repo](https://github.com/RealToughCandy/project-ideas-for-web-developers)
The Requirements for the app can be found [here](https://github.com/RealToughCandy/project-ideas-for-web-developers/blob/master/projects/dating-app.md)

Demo Video Comming Soon

## Usage Instructions 
If you would like to try this youself then clone the repo

Then I recommend you start a virtual environment:
```
pip install virtual env
vritualenv env
env\Scripts\activate.bat
```
Mac is similar the only differenct is the activate. 

Now you can install requirements: `pip install -r requirements.txt`

Now create a .env file:
```
KEY = secret_key
PASSWORD = your_email_password
MAIL = your_email

```
To generate a secret key there are many methods. For example 
Open the Django shell `python manange.py shell`
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
Then copy that into the key field as a string.

You should be done. Just run 
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

