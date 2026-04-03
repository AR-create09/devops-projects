# Project 3 - Kubernetes Deployment

## Tools Used
- Kubernetes
- Minikube
- kubectl
- Docker

## What I Built
Deployed a containerised nginx application on a
local Kubernetes cluster with 2 replicas.

## Files
- deployment.yaml: Creates 2 nginx pods
- service.yaml: Exposes app via NodePort

## Commands Used
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods
kubectl scale deployment anil-deployment --replicas=4
kubectl get all

## How to Run
1. Start minikube: minikube start --driver=docker
2. Apply files: kubectl apply -f deployment.yaml
3. Apply service: kubectl apply -f service.yaml
4. Open app: minikube service anil-service
