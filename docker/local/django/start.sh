#!/bin/bash

set -o errexit

set -o pipefail

set -i nounset

python manage.py migrate --no-input
python manage.py collecstatic --no-input
exec python manage.py runserver 0.0.0.0:8000
