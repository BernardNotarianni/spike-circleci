## Some usefull gcloud/kubectl commands

Activate gcloud service account

    $ gcloud auth activate-service-account --key-file=/home/bernard/gcloud-key-project-concourse.json
    
Get `kubeconfig.yml`

    $ KUBECONFIG=kubeconfig.yml gcloud --project spike-concourse container clusters get-credentials concourse --region europe-west1-c

List nodes

    $ KUBECONFIG=kubeconfig.yml kubectl get nodes
