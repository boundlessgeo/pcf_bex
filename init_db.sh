#!/bin/sh
echo "------ Create database tables ------"
python manage.py syncdb --noinput

echo "------ create default admin user ------"
echo "from geonode.people.models import Profile; Profile.objects.create_superuser('admin', 'admin@geonode.local', 'admin')" | python manage.py shell

echo "------ starting gunicorn  ------"
gunicorn pcf_bex.wsgi --workers 2
