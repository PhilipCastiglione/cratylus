# Python Flask Project

## Prerequisites

To run locally, you will need:

* python 3.10 - I manage language versions with asdf version manager
* pipenv, which can be installed using pip
* postgres installed and running - I use homebrew for this

## Usage


## TODO

- [ ] setup
    - [x] python version
    - [x] venv
    - [x] dependency management
    - [x] flask app scaffold
    - [x] secret management
    - [x] initial helper scripts, run local dev
    - [x] pages scaffold
    - [x] user authn/authz scaffold
    - [x] database & migrations setup & injection
        - [x] requirements: psycopg2, flask-sqlalchemy, alembic
        - [x] database creation script, migrations script
    - [ ] database models & migrations
        - [x] user
        - [ ] ingredient
        - [ ] meal
        - [ ] report
        - [ ] savedfile
    - [ ] user management
        - [ ] creation
        - [ ] logging in
        - [ ] logging out
        - [ ] authn requirement for a page
    - [ ] ...
- [ ] document
    - [ ] usage (run the dev server)
    - [ ] changes (workflow, tests)
    - [ ] setup (python version, pipenv install, migrations ...)