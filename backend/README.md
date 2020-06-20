# Dev env:

docker-compose ps <br>
docker-compose up -d --build <br>
docker-compose down -v <br>

http://localhost:8000/

# Prod env:

ansible-vault decrypt envs/prod/env.prod.db envs/prod/env.prod <br>
mkdir envs/prod/{postgres_db_data,staticfiles,mediafiles} <br><br>

docker-compose -f docker-compose.prod.yml up -d --build <br>
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput<br>
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear<br>
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser<br><br>

docker-compose -f docker-compose.prod.yml ps<br>
docker-compose -f docker-compose.prod.yml logs -f<br>

http://localhost:8080/

# Prod clean up:
docker-compose -f docker-compose.prod.yml down -v<br>

rm -rf envs/prod/staticfiles/ envs/prod/postgres_db_data/<br>

ansible-vault encrypt envs/prod/env.prod.db envs/prod/env.prod<br>
