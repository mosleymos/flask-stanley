bluemix hello world in python
================================================================================

The sample is using [Flask microframework](http://flask.pocoo.org/) and
intended to test the Python support on [IBM Bluemix](https://bluemix.net/).



run locally
--------------------------------------------------------------------------------

- [install flask](http://flask.pocoo.org/docs/0.10/installation/)
- run `python hello.py`
- visit web site



run on bluemix
--------------------------------------------------------------------------------

- edit the `manifest.yml` file and edit the `hostname` property to make it unique
- run `cf push`
- visit web site


Old project from an hackathon about IBM Bluemix service

## Todolist

- [] Remettre version python a jour
- [] Gestion dépendances
- [] Dockerize ?
- [] Proto simple pour marche
- [] Essai pour marche
- [] Separer du front et back
- [] pylint et autres outils pour gestion code
