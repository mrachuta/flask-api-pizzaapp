#!/bin/bash

# Skip DB migration if variable FLASK_SKIP_MIGRATION is set
if [[ -z "${FLASK_SKIP_DB_MIGRATION}" ]]; then
  echo "INFO: Running DB migrations..."
  python manage.py db init
  python manage.py db migrate
  python manage.py db upgrade
fi

echo "INFO: Starting application..."
python manage.py runserver --host=0.0.0.0