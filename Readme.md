# DAY IN THE LIFE
### Description
In this particular application a user is required to login if he/she has an existing account or create an account if none is existent. Once the user is authenticated, they are allowed to leave a comment on the blogs  in the landing page of the application. As a writer in this blog application, once authenticated, you are allowed to add a blog on an topic of your choice with an option of either deleting or updating the blog. The writer is also allowed to delete comments that he/she finds degrading. The application also displays random quotes to keep our users motivated.
## author's Information
This code was done and compiled by Jeff Owuor

## user story- - 
- As a user, I would like to view the blog posts on the site
- As a user, I would like to comment on blog posts
- As a user, I would like to view the most recent posts
- As a user, I would like to an email alert when a new post is made by joining a subscription.
- As a user, I would like to see random quotes on the site
- As a writer, I would like to sign in to the blog.
- As a writer, I would also like to create a blog from the application.
- As a writer, I would like to delete comments that I find insulting or degrading.
- As a writer, I would like to update or delete blogs I have created.

## BEHAVIOUR DRIVEN DEVELOPMENT
| Behaviour  | input  |output   |
| :------------: | :------------: | :------------: |
|User registration   | username,email,password  | account ready for login   |
| User login  | username, password  |  Access every feature of app   |
| Create blog  | type a blog and submit   |displayed in home page   |
| Comment on a blog  | type a comment and submit  | displayed below the specific blog   |
| update profile picture  | choose a file   | The selected photo is displayed in your profile  |
|  View blogs from other users |Load the page   | All the different blogs are visible on the home page  |
|Delete a comment on a blog|Click the delete button |The comment is removed from the list|
|Delete a blog|Click the delete button|The blog is removed from the ones displayed on the screen|
|View a random quote|Refresh the page|A random quote is displayed upon every refresh|

## SETUP INSTRUCTIONS
To get the application ...
1. Clone the repo
2.  Install all the requirements listed in the requirements.txt file.
  $ pip install -r requirements.txt

3. Exporting configurations
   export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

4. Running the application
    python3.9 manage.py server

5. Testing the application
    python3.9 manage.py test


### Known bugs 
No known bugs but if you find any feel free to reach me at Xavierjeff451@gmail.com
### Technologies used
Python
Heroku
Flask
