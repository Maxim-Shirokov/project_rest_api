You need to run the following commands to deploy rest_api

`docker-compose -f <PROJECT_PATH>/project_restapi/docker-compose.yml build`

`docker-compose -f <PROJECT_PATH>/project_restapi/docker-compose.yml up`

Then you need to run the following command in new terminal tab to create a superuser
 
`docker exec -it project_restapi_drf_1 python manage.py createsuperuser`

(project_restapi_drf_1 is  container name restapi)

