az login
az account list -o table
az account set --subscription <subscription-id>
export SUBSCRIPTION=XXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX

export RESOURCE_GROUP_NAME=aks-getting-started
export LOCATION=eastasia
export AKS_CLUSTER_NAME=aks-getting-started
export AKS_CLUSTER_VERSION=1.28.3
export AKS_NODE_COUNT=2
export AKS_NODE_VM_SIZE=Standard_DS2_v2
export AKS_NODE_DISK_SIZE=50

az group create --name $RESOURCE_GROUP_NAME --location $LOCATION


SERVICE_PRINCIPAL_JSON=$(az ad sp create-for-rbac --skip-assignment --name aks-getting-started-sp -o json)
SERVICE_PRINCIPAL=$(echo $SERVICE_PRINCIPAL_JSON | jq -r '.appId')
SERVICE_PRINCIPAL_SECRET=$(echo $SERVICE_PRINCIPAL_JSON | jq -r '.password')

az role assignment create --assignee $SERVICE_PRINCIPAL \
--scope "/subscriptions/$SUBSCRIPTION/resourceGroups/$RESOURCE_GROUP_NAME" \
--role Contributor

az aks get-credentials --resource-group $RESOURCE_GROUP_NAME --name $AKS_CLUSTER_NAME

kubectl get nodes

kubectl apply -f aks-store-quickstart.yaml

kubectl get pods
kubectl get service store-front --watch


az aks delete --resource-group $RESOURCE_GROUP_NAME
az ad sp delete --id $SERVICE_PRINCIPAL
kubectl config delete-content $AKS_CLUSTER_NAME