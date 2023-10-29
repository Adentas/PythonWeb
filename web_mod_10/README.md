# mod_10

## Homework Description

This home-project is a website for promoting and storing quotes from famous authors. You can browse quotes and author information without registration. Adding new authors and quotes is only available for registered users.

## Main Features

- Registration and login to the site.
- Adding a new author (only for registered users).
- Adding a new quote with author specification (only for registered users).
- Ability to view each author's page without authentication.
- All quotes are available for viewing without authentication.

## Database Migration

|Custom-script: migrations.py| for Migration from MongoDB to Postgres has been conducted for storing user and quote data.

## Usage

To launch the website, execute the command:

```bash
python manage.py runserver
```

After this, the website will be accessible at `http://localhost:8000/`.
