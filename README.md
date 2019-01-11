# aircalc
### Requiments
 * Python 3.6.5
 * postgresql
 * npm
### Install
 * `pipenv i` to install backend dependencies
 * `cd static && npm i` to install frontend dependencies
 * `npm run build` to build staticfiles for backend
### Run
#### Frontend
 * `npm start` from `static/` to run webpack-devserver*
#### Backend
 * init in `postgresql` user `myprojectuser` with password `password` and permissions to db `myproject` (also create it)
 * `pipenv shell`
 * `python manage.py runserver`
