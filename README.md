 #  VlogHub (Personal project)
VlogHub is a web application developed using Django, PostgreSQL, HTML, CSS, and JavaScript. It serves as a platform where users can post their vlogs and interact with other users by liking and commenting on their vlogs. Each user has a profile page, and you can follow other users to stay updated with their latest vlogs.
## Feature 
* User Registration and Authentication: Users can create an account and log in to the application. Passwords are securely stored using encryption techniques.
* Profile Pages: Each user has a dedicated profile page where they can showcase their vlogs and provide information about themselves.
* Vlog Creation: Users can create and publish their vlogs by adding a title, description, and multimedia content (e.g., images,..).
* Interactions: Users can like and comment on vlogs posted by other users, fostering engagement and interaction within the community.
* Following: Users have the option to follow other users, allowing them to see updates and new vlogs from the users they follow.
* Searching: Users can search for other users or vlogs based on specific criteria. The search function allows users to find users whose usernames contain the entered string or vlogs that include the entered string in content.
* Edit and Delete Vlogs: Users have the ability to edit or delete vlogs that they have posted before. This allows users to update their vlogs with new information or remove vlogs that are no longer relevant.
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
5. Install the dependencies
```console
pip install -r requirements.txt
```
6. Set up the database:
   * Install PostgreSQL if you haven't already.
   * Create a new database in PostgreSQL.
   * Update the database settings in **vloghub/settings.py** to match your PostgreSQL configuration.
7. Apply the database migrations
```console
python manage.py makemigrations
python manage.py migrate
```
8. Start the development server
```console
python manage.py runserver
```
9. Access VlogHub in your web browser at **http://localhost:8000/**<br>
## The Reason Why i built this web app
i choice django framework because its convenience, how it's fexible with database, high sercurity and
i already have a friend-collaborate web app project build on django framework. So with pre-existing foundation about html,css and django, i quickly start building **Vloghub**
## Time
The project was started to be created from 2/7/2023 and first uploaded to github on 4/7/2023
## Deployment
To deploy VlogHub and make it accessible to others, i used ngrok, a tool that creates secure tunnels to my locally hosted web application<br>
<a href="https://ead2-14-191-166-50.ngrok-free.app" target="_blank">Vloghub</a>
> **Notice:** The link may be unaccessable by the time you access because i turned the server off or be modified because of ngrok free version

## Contact
> If you have any questions, suggestions, or feedback, please contact me at **nguenxuantung437@gmail.com**


[![My Skills](https://skills.thijs.gg/icons?i=py,postgres,html,css,javascript&theme=light)](https://skills.thijs.gg)
