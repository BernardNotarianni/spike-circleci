A dashboard to display available kubernetes deployment.

You need a `gcp-key.json` file containing the gcloud service account credentials.

Create a `kubeconfig.yml` file:

    $ KUBECONFIG=./kubeconfig.yml gcloud container clusters get-credentials concourse --zone=europe-west1-c

Build the docker container:

    $ docker build -t gcr.io/spike-concourse/dashboard .

Push it to gcr:

    $ docker push gcr.io/spike-concourse/dashboard
    
Deploy it on kubernetes:

    $ KUBECONFIG=./kubeconfig.yml kubectl apply -f deployment.yml

