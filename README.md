# Writers-Corner API
A news application which allows writers to send articles from any location. https://writers-korner-api.herokuapp.com/
## Technologies Used
1. Python/Django
2. Django-rest-framework
3. Django-rest-auth
## API endpoints
**Users**
* /rest-auth/registration/ (POST),  User registration
  - username
  - password1
  - password2
  - email
* /rest-auth/login (POST), User Login
  - username
  - email
  - password
* /rest-auth/logout/ (POST)
* /rest-auth/user/ (GET, PUT, PATCH), get or update a user
  - username
  - first_name
  - last_name
* /users/ (GET), get all users
* /user/id/articles/ (GET), get user article
    - id is user id

**Articles**
* /articles/ (GET, POST), get all articles or post new article
    - title
    - text
    - author(user instance)
* /articles/id/ (GET, PUT, PATCH, DELETE)
    - id is article id
