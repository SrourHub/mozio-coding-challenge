# mozio coding challenge
Deployed server url: https://backend-project-deployment.herokuapp.com

Provider Endpoints:

    To get all providers or to add a new provider (GET AND POST):
        * https://backend-project-deployment.herokuapp.com/providers/ 
    
    To get a provider or update a provider or delete a provider (GET, PUT AND DELETE):
        * https://backend-project-deployment.herokuapp.com/providers/<id>

Service Area Endpoints

    To get all service areas or to add a new service area (GET AND POST):
        * https://backend-project-deployment.herokuapp.com/service_areas/
    
    To get a service area or update a service area or delete a service area (GET, PUT AND DELETE):
        * https://backend-project-deployment.herokuapp.com/service_areas/<id>

    To get all service areas that contain a lat/lng pair with the corresponding provider name and price:
        * https://backend-project-deployment.herokuapp.com/service_areas/contain_point/<lat>/<lng>/
    
Note:
    I tried to deploy my application on AWS, however, I needed to add a bank account information which I can't at the moment. Thank you for your consideration.
