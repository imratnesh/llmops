from kfp import Client
client = Client(host="http://127.0.0.1:8081")
client.create_run_from_pipeline_package("greeting_pipeline.yaml", 
                                        arguments={"recipient": "Ratnesh"})


# import kfp
# print(kfp.__version__)
# # 2.12.1
# from kfp import Client
# client = Client(host="http://localhost:8081/")
# print(client.list_pipelines())
#############################################
# import kfp
# from kfp.components import create_component_from_func
# from kfp.dsl import pipeline


# # Define a simple component
# @create_component_from_func
# def add(a: float, b: float) -> float:
#     """Calculates the sum of two numbers."""
#     return a + b


# Define a pipeline
# @pipeline(
#     name='Add Pipeline',
#     description='A simple pipeline that adds two numbers.'
# )
# def add_pipeline(
#     a: float = 1.0,  # Default value for 'a'
#     b: float = 2.0,  # Default value for 'b'
# ):
#     """
#     This pipeline defines the steps to add two numbers.
#     """
#     # Create a task using the 'add' component
#     add_task = add(a=a, b=b)



# if __name__ == '__main__':
#     # Specify the output YAML file
#     pipeline_file = 'add_pipeline.yaml'
#     # Compile the pipeline
#     kfp.compiler.Compiler().compile(
#         pipeline_func=add_pipeline,
#         package_path=pipeline_file)
#     print(f"Pipeline compiled to: {pipeline_file}")

#############################################
# from kfp.client import Client

# #  Replace <KFP_ENDPOINT> with the URL of your KFP deployment
# client = Client(host='<KFP_ENDPOINT>')

# #  Replace 'add_pipeline.yaml' with the path to your compiled YAML file
# pipeline_file = 'add_pipeline.yaml'

# #  Create an experiment to organize your pipeline runs
# experiment_name = 'my_experiment'
# client.create_experiment(experiment_name)

# #  Run the pipeline
# run_name = 'my_pipeline_run'
# run_result = client.create_run_from_pipeline_package(
#     pipeline_file,
#     arguments={'a': 5.0, 'b': 10.0},  #  Supply any pipeline parameters
#     experiment_name=experiment_name,
#     run_name=run_name
# )

# print(f"Pipeline run submitted.  Run ID: {run_result.run_id}")



"""

     curl http://127.0.0.1:8080/apis/v1beta1/pipelines
          kubectl top nodes
          minikube start
          minikube dashboard
   kubectl delete namespace kubeflow
      kubectl get namespaces
      kubectl create namespace kubeflow
      -----
   kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=release-1.8"
   kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/dev?ref=release-1.8"

   kubectl get pods -n kubeflow
   kubectl rollout restart deployment -n kubeflow

kubectl exec -it -n kubeflow mysql-xxxx-xxxx -- bash 
    kubectl port-forward -n kubeflow svc/ml-pipeline 8080:8888
       kubectl logs -n kubeflow ml-pipeline-84b9cc9c4d-jfbhv
          kubectl delete pod -n kubeflow mysql-757ffc45cf-gzx7z


   kubectl exec -it -n kubeflow mysql-7df8cfb5cc-jddn5 -- bash
   kubectl describe pod -n kubeflow mysql-649b8fc674-vmmf2

   kubectl rollout restart deployment -n kubeflow mysql

   kubectl apply -f add_pipeline.yaml -n kubeflow

/Users/ratnesh/Documents/llmops/greeting_pipeline.json

"""
