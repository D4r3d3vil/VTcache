## Installation
first clone the project:
```bash
git clone https://github.com/D4r3d3vil/VTcache.git
```

install the required packages (python):
```bash
pip install -r requirements.txt
```

## Running
The entire project is dockerized to start it simply run:
```bash
docker-compose up
```

## Admin Panel
Django provides a powerful admin interface which integrates well with this project
to use it first create a superuser: 
```bash 
docker-compose exec web python manage.py createsuperuser
```
then re-run the project:
```bash
docker-compose up
```

## API
There are 4 main API endpoints