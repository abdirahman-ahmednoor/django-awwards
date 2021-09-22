##Awwards

## AUTHOR
Abdirahman Noor

## DESCRIPTION
This is a Django web application that allows users to view posted projects and their details. The user can also post a project to be rated or reviewed and a user can as well rate and review other users' projects.

## SETUP
To access this project on your local files, you can clone it using these steps:

1. Open your Terminal.
2. Use this command to clone `https://github.com/abdirahman-ahmednoor/django-awwards.git`
3. This will clone the repository into your local folder.

## BDD
1. Provides rating form
   | input       |    output  |
     | :--      | :---      |
   | user fills rating form  | new rating added to tyhe project |
2. Provides forms to post project 
   | input       |    output  |
     | :--      | :---      |
   | menu link "post site" clicked | new post added  |
3. Show user profile 
   | input       |    output  |
     | :--      | :---      |
   | user profile icon clicked  | profile page with user information displayed  |
4. Show project details
   | input       |    output  |
     | :--      | :---      |
   | project image clicked  |  a new page loaded with project details   |

5. Provides  delete function
   | input       |    output  |
     | :--      | :---      |
   | delete button clicked | project deleted  |

## DEPENDENCIES
1. django-bootstrap
2. Pillow
3. cloudinary
4. psycopg2
5. django-registration
6. python-decouple
7. Python Venv
8. Whitenoise
9. Gunicorn

## TECHNOLOGIES USED

1. Python3
2. HTML
3. CSS
4. Javascript

## LIVE
View [Live](https://awwards-090.herokuapp.com/)

## LICENSE
This project is under [MIT](Licence) license.