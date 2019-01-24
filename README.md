# aircalc
### Requiments
 * Python 3.7
 * npm
 * pipenv
### Install
 * `pipenv i` to install backend dependencies
 * `cd static && npm i` to install frontend dependencies
 * `npm run build` to build staticfiles for backend
 * `pipenv shell && python manage.py makemigrations && python manage.py migrate` to generate db files
### Run
#### Frontend
 * `npm start` from `static/` to run webpack-devserver
#### Backend
 * `pipenv shell`
 * `python manage.py runserver`
