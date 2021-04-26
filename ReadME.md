# Django Zuri Task.



This is Task 7 giving to people in the Django track. Expand the CRUD capablity of the blog.
# Deployment
The Blog was deployed on Heroku, and Debug is set to False and the secret_key was kept in an env file and the variables were set using the Heroku variables.

here is the link: 

https://zuri-blog-py.herokuapp.com/


# Tasks

-    A register page (a new user can register, their details stored in a database file). 

-    login (checks in the file and logs them in if they are already registered)

-    reset password

-    logout

-    A comment section, you must be logged in to comment

-    Host the project on heroku

# The URLs of the website.

 - Root:'', 'home',
- Post: 'post_detail',
- Create Post: 'new_post/', name='post_new'
- Update post:    'post/<int:pk>/edit/', name='edit_post'
- Delete: 'post/<int:pk>/delete/', name= 'delete_post'
- Signup/Register page: 'signup/', name='signup'
- Adding a comment to a Post: 'post/<int:pk>/comment/', name='add_comment'


# The tests.
Tests were written, and they passed. Some test did not pass due to the login requirement and the permissions, that will be fixed.