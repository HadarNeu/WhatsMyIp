# WhatsMyIp
## Python Flask app to discover your own external IP!

This project is a helm chart which includes 2 pods: 
1. The App pod: Python Flask- returns your external and internal IP addresses.
2. The Nginx pod: a reverse proxy for the app.
## Thats the app's output:
![alt text](./Images/output.png?raw=true "output")

## How does it work?
1. I created a Python Flask app. 
   The deployment file pulls the app's docker image from Docker hub. (I also left the code public for your review)
2. The deployment of Nginx works as a reverse proxy for the app. 
3. In the config file, I configured Nginx to route traffic to the app's ClusterIP service.    
4. The NodePort service is then the deployment's gateway and is routing traffic to the Nginx pod. 
![alt text](./Images/InfrastructureDiagram.png?raw=true "output")

## So how can YOU use this app? 
1. Install minikube (a single node kubernetes tool). It's a great way for you to learn k8s and practice the skills in your home environment. 
Your'e going to need a docker engine installed as well. 
OR 
You can deploy this chart on your cloud kubernetes distribution. (Eks, Ecs etc.)

2. Clone the repository. 

3. Start the minikube cluster:

minikube start --driver=docker

3. Deploy the helm chart:

helm install ipapp ./ipappChart --values ./ipappChart/values.yaml

4. Expose the NodePort service (skip this step if you are running the app on a k8s cloud dist.)

minikube service nginx-service

## The browser will automatically open the page and now you have your external IP address AND your app's pod IP address!
