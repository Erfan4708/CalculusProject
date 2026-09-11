# Calculus 3D

A small Django website for sharing 3D curves and surfaces from multivariable calculus. It was built in 2023 as a team project for a calculus course.

Each post describes a curve or surface and has a preview image. A post can also embed an interactive 3D scene exported from GeoGebra (rendered with Three.js). Visitors can browse the posts. Registered users can save posts to a personal favorites list.

## Features

- Paginated list of posts (6 per page) with preview images and short descriptions
- Post detail page that renders the post's embedded HTML/JavaScript (e.g. a rotatable 3D scene)
- Sign up, log in, log out and password change using Django's built-in authentication
- "Add to favorites" for logged-in users and a "My Favorites" page showing only their own saved posts
- Posts, favorites and users are managed through the Django admin

## Tech Stack

- Python / Django 4.2
- SQLite
- django-crispy-forms with the Bootstrap 4 template pack (for the auth forms)
- Pillow (for the `ImageField` on posts)
- A free Bootstrap 4 / jQuery HTML template for the front end
- Three.js (loaded from a CDN inside the embedded post content)

## Project Structure

```
CalculusProject/    Project settings, root URL configuration and WSGI entry point
blog/               Post and Favoritepost models, views and URLs for the public pages
accounts/           Sign-up view (login/logout/password change come from django.contrib.auth)
templates/          Base layout, post list/detail, favorites and registration templates
static/             CSS, JavaScript and images from the HTML template
media/images/       Uploaded post images
db.sqlite3          SQLite database with sample posts
requirements.txt    Python dependencies
manage.py           Django management script
```

## Getting Started

### Prerequisites

- Python 3.10 or 3.11 (developed on 3.10, re-tested on 3.11)
- pip

### Installation

```bash
git clone https://github.com/Erfan4708/CalculusProject.git
cd CalculusProject

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

### Database

The repository includes `db.sqlite3` with sample posts, and all migrations are already applied to it. If you delete it to start fresh, create a new database and an admin account:

```bash
python manage.py migrate
python manage.py createsuperuser
```

You can also run `createsuperuser` on the included database to get your own admin login.

### Run the development server

```bash
python manage.py runserver
```

Then open http://127.0.0.1:8000/.

## Configuration / Environment Variables

All settings are in `CalculusProject/settings.py`. A few can be overridden with environment variables. The defaults are meant for local development only.

| Variable               | Default                                  | Description                                  |
|------------------------|------------------------------------------|----------------------------------------------|
| `DJANGO_SECRET_KEY`    | an insecure development key              | Django secret key                            |
| `DJANGO_DEBUG`         | `True`                                   | Set to `False` to turn off debug mode        |
| `DJANGO_ALLOWED_HOSTS` | empty (Django allows localhost in debug) | Comma-separated host names, e.g. `example.com` |

Example (macOS / Linux):

```bash
export DJANGO_SECRET_KEY="replace-with-a-long-random-string"
export DJANGO_DEBUG=False
export DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

Example (Windows PowerShell):

```powershell
$env:DJANGO_SECRET_KEY = "replace-with-a-long-random-string"
```

Uploaded images are only served by Django when `DEBUG` is on.

## Usage

| URL                          | Page                                        |
|------------------------------|---------------------------------------------|
| `/`                          | Post list                                   |
| `/post/<id>/`                | Post detail                                 |
| `/add_favorite/<id>/`        | Adds a post to your favorites (login required) |
| `/favorite-list/`            | Your favorite posts                         |
| `/accounts/signup/`          | Sign up                                     |
| `/accounts/login/`           | Log in                                      |
| `/accounts/password_change/` | Change password                             |
| `/admin/`                    | Django admin                                |

New posts are added in the admin under **Blog → Posts**. Each post has a title, an image, a description and an optional `html_content` field. That field is rendered as-is on the detail page. The sample posts use it for a Three.js scene exported from GeoGebra.

## Testing

```bash
python manage.py test
```

A small test suite was added while cleaning the project up. It covers:

- the post list and detail pages
- adding favorites (login required, no duplicates)
- the favorites page showing only the current user's posts
- sign up and log out

## Technical Notes

- There are two Django apps. `blog` holds all of the site's content. `accounts` only adds a sign-up view on top of `django.contrib.auth`, and the default `User` model is used.
- Favorites are stored in a simple `Favoritepost` table (user → post) instead of a field on `Post`.
- `html_content` is rendered with the `|safe` filter so embedded scripts can run. This is fine for content written by trusted admins, but it should never hold user-submitted content.

## Limitations

- Only 2 of the 13 sample posts in `db.sqlite3` have their image files in `media/images/`, and only those two have an embedded 3D scene. The other posts show a broken image.
- There is no "remove from favorites" option yet. Adding a favorite is a plain link (GET request) rather than a form.
- `Post.favorite` is an unused boolean left over from an earlier approach. It was kept to avoid a schema change.
- The 3D scenes load Three.js r92 from external CDNs, so they need an internet connection.
- The front-end template still contains leftover assets, e.g. two copies of jQuery and plugins the site doesn't use.
- The project isn't set up for production: it uses SQLite, has no `STATIC_ROOT`, and serves media files through Django. The sample database also contains test accounts from development, so don't deploy it publicly.
