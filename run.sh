#!/usr/bin/env bash

set -euo pipefail

# Skip DB migration if variable FLASK_SKIP_MIGRATION is set
# - added because of possible UBOUND VARIABLE erorr
if [[ -z "${FLASK_SKIP_DB_MIGRATION-}" ]]; then
  echo "INFO: Running DB migrations..."
  flask --app pizzaapp.app db init
  flask --app pizzaapp.app db migrate
  flask --app pizzaapp.app db upgrade
fi

echo "INFO: Starting application..."
flask --app pizzaapp.app run --host=0.0.0.0
