apiVersion: v1
kind: Service
metadata:
  name: ipapp-nodeport
  namespace: ingress-nginx
spec:
  selector:
    app: ipapp
  type: NodePort
  ports:
  - protocol: TCP
    port: 8080
    targetPort: 80
    nodePort: 30003

