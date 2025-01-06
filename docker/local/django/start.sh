#!/bin/bash

set -o errexit

set -o pipefail

set -o nounset

if [ -z "${POSTGREST_DB:-}" ]; then
  echo "Error: POSTGREST_DB is not set."
  exit 1
fi

python manage.py migrate --no-input
python manage.py collectstatic --no-input
exec python manage.py runserver 0.0.0.0:8000
