**Deploy rest_api**

You need to run the following command to deploy rest_api

`docker-compose -f <PROJECT_PATH>/docker-compose.yml up`

**Admin**

Then you need to run the following command in new terminal tab to create a superuser
 
`docker exec -it <CONTAINER NAME RESTAPI> python manage.py createsuperuser`

(project_restapi_drf_1 it's an  example container name)

**Versions**

docker-compose version 1.25.5

Docker version 19.03.8

