#!/bin/bash

# Skip DB migration if variable FLASK_SKIP_MIGRATION is set
if [[ -z "${FLASK_SKIP_DB_MIGRATION}" ]]; then
  echo "INFO: Running DB migrations..."
  python flask --app pizzaapp.app db init
  python flask --app pizzaapp.app db migrate
  python flask --app pizzaapp.app db upgrade
fi

echo "INFO: Starting application..."
python flask --app pizzaapp.app run --host=0.0.0.0
