# l-space
(test commit)
A distributed library created from your friend's bookshelves

## Quickstart

### One-time setup for Python and Postgres

l-space requires [Python 3.7](https://www.python.org/downloads/) and [Postgres 10](https://www.postgresql.org/download/).
 
Once you've installed Postgres, run it to create a database for l-space:

`psql -U <your-superuser-username> -d postgres`

where `<your-superuser-username>` is the name of the superuser you created when first installing Postgres. This should launch a Postgres terminal, from which you can create
the database and username that the l-space app will use:

```
create database l_space_dev;
create user librarian with superuser password 'librarian';
```

(This username and database name are defined in Django's configuration file for l-space, which can be found at `config/settings.py`.)

### Running the app locally

To run the l-space web app locally, first install requirements:
 
 `pip install -r requirements.txt`

Ensure all migrations are applied:

`python manage.py migrate`

Then, run the Django server:

`python manage.py runserver`

## Running tests

(Coming soon)


## Deployment

()