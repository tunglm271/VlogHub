 #  VlogHub (Personal project)
VlogHub is a web application developed using Django, PostgreSQL, HTML, CSS, and JavaScript. It serves as a platform where users can post their vlogs and interact with other users by liking and commenting on their vlogs. Each user has a profile page, and you can follow other users to stay updated with their latest vlogs.
## Feature 
* User Registration and Authentication: Users can create an account and log in to the application. Passwords are securely stored using encryption techniques.
* Profile Pages: Each user has a dedicated profile page where they can showcase their vlogs and provide information about themselves.
* Vlog Creation: Users can create and publish their vlogs by adding a title, description, and multimedia content (e.g., images, videos).
* Interactions: Users can like and comment on vlogs posted by other users, fostering engagement and interaction within the community.
* Following: Users have the option to follow other users, allowing them to see updates and new vlogs from the users they follow.
## Installation
To run VlogHub locally on your machine, follow the instructions below:
1. Clone the repository:
```console
git clone https://github.com/your-username/vloghub.git
```
2. Navigate to the project directory
```console
cd vloghub
```
3. Create a virtual environment
```console
python3 -m venv venv
```
4. Activate the virtual environment
5. Set up the database:
   * Install PostgreSQL if you haven't already.
   * Create a new database in PostgreSQL.
   * Update the database settings in **vloghub/settings.py** to match your PostgreSQL configuration.
6. Apply the database migrations
```console
python manage.py makemigrations
python manage.py migrate
```
7. Start the development server
```console
python manage.py runserver
```
8. Access VlogHub in your web browser at **http://localhost:8000/**<br>
## The Reason Why a build this web app
i choice django framework because its convenience, how it's fexible with database, high sercurity and
i already have a friend-collaborate web app project build on django framework. So with pre-existing foundation about html,css and django, i quickly start building **Vloghub**
## Time
The project was started to be created from 2/7/2023 and first uploaded to github on 4/7/2023
## Contact
> If you have any questions, suggestions, or feedback, please contact me at **nguenxuantung437@gmail.com**


[![My Skills](https://skills.thijs.gg/icons?i=py,postgres,html,css&theme=light)](https://skills.thijs.gg)
