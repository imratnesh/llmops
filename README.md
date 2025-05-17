# Kubeflow Pipeline Project

![Kubeflow Logo](https://www.kubeflow.org/images/logo.svg)

## 📋 Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This project demonstrates the implementation of a simple multiplication pipeline using Kubeflow Pipelines. It provides a basic example of how to create, compile, and run pipelines in a Kubeflow environment.

## Prerequisites

### System Requirements
- Python 3.7+
- Kubernetes cluster
- Kubeflow Pipelines
- Git
- GitHub CLI (gh)

### Required Python Packages
```python
kfp>=1.8.0
kubernetes>=12.0.0
```

## Installation

### For macOS

```bash
# Install Python dependencies
pip install kfp kubernetes

# Install kubectl
brew install kubectl

# Install gh (GitHub CLI)
brew install gh
```

### For Linux (Ubuntu/Debian)

```bash
# Install Python dependencies
pip install kfp kubernetes

# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Install gh (GitHub CLI)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

## Project Structure
.
├── README.md
├── LICENSE
├── .gitignore
├── advance.ipynb
└── mul_pipeline.yaml



## Usage

### 1. Compile the Pipeline

```bash
python advance.ipynb
```

This will generate a `mul_pipeline.yaml` file containing the compiled pipeline.

### 2. Run the Pipeline

```python
from kfp import Client

# Initialize the client
client = Client(host="http://localhost:8080")

# Create and run the pipeline
client.create_run_from_pipeline_package(
    pipeline_file='mul_pipeline.yaml',
    arguments={
        'a': 5.0,
        'b': 3.0
    }
)
```

### 3. Monitor the Pipeline

You can monitor the pipeline execution through:
- Kubeflow UI
- Programmatically using the client
- Kubernetes dashboard

# Kubeflow Pipeline Project

[Previous sections remain the same...]

## 🛠️ Troubleshooting Guide

### 1. Installation Commands

#### Docker Installation
```bash
# For macOS
brew install docker

# For Ubuntu/Debian
sudo apt-get update
sudo apt-get install docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
```

#### Minikube Installation
```bash
# For macOS
brew install minikube

# For Ubuntu/Debian
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

#### Kubeflow Installation
```bash
# Install kfctl
curl -L https://github.com/kubeflow/kfctl/releases/download/v1.2.0/kfctl_v1.2.0-0-gbc038f9_linux.tar.gz | tar xz
sudo mv kfctl /usr/local/bin/

# Download Kubeflow config
export KF_NAME=my-kubeflow
export BASE_DIR=/opt
export KF_DIR=${BASE_DIR}/${KF_NAME}
mkdir -p ${KF_DIR}
cd ${KF_DIR}
kfctl init ${KF_NAME} --config=https://raw.githubusercontent.com/kubeflow/manifests/v1.2-branch/kfdef/kfctl_k8s_istio.v1.2.0.yaml
kfctl generate all -V
kfctl apply all -V
```

### 2. Common Commands

#### Minikube Commands
```bash
# Start Minikube
minikube start --cpus 4 --memory 8192

# Check Minikube Status
minikube status

# Stop Minikube
minikube stop

# Delete Minikube
minikube delete

# Get Minikube IP
minikube ip

# Enable Ingress
minikube addons enable ingress
```

#### Kubernetes Commands
```bash
# Check Cluster Status
kubectl cluster-info

# Check Nodes
kubectl get nodes

# Check All Resources in Kubeflow Namespace
kubectl get all -n kubeflow

# Check Pods
kubectl get pods -n kubeflow

# Check Services
kubectl get svc -n kubeflow

# Check Deployments
kubectl get deployments -n kubeflow

# Check ConfigMaps
kubectl get configmaps -n kubeflow

# Check Secrets
kubectl get secrets -n kubeflow
```

#### Kubeflow Pipeline Commands
```bash
# Port Forward for Kubeflow UI
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80

# Port Forward for Pipeline API
kubectl port-forward -n kubeflow svc/ml-pipeline 8888:8888

# Check Pipeline Pods
kubectl get pods -n kubeflow | grep pipeline

# Check Pipeline Logs
kubectl logs -n kubeflow <pipeline-pod-name>

# Check Pipeline Service
kubectl get svc -n kubeflow | grep pipeline
```

### 3. Troubleshooting Steps

#### 1. Check System Requirements
```bash
# Check Docker Version
docker --version

# Check Minikube Version
minikube version

# Check kubectl Version
kubectl version

# Check System Resources
kubectl describe nodes
```

#### 2. Verify Kubeflow Installation
```bash
# Check Kubeflow Namespace
kubectl get namespace kubeflow

# Check All Resources
kubectl get all -n kubeflow

# Check Pod Status
kubectl get pods -n kubeflow -o wide

# Check Pod Logs
kubectl logs -n kubeflow <pod-name>
```

#### 3. Common Issues and Solutions

##### Issue: Pods in Pending State
```bash
# Check Pod Details
kubectl describe pod <pod-name> -n kubeflow

# Check Node Resources
kubectl describe nodes

# Check Events
kubectl get events -n kubeflow
```

##### Issue: Pipeline API Connection
```bash
# Test API Connection
curl http://localhost:8888/healthz

# Check API Pod
kubectl get pods -n kubeflow | grep ml-pipeline

# Check API Logs
kubectl logs -n kubeflow <ml-pipeline-pod-name>
```

##### Issue: UI Access
```bash
# Check UI Service
kubectl get svc -n kubeflow | grep ui

# Port Forward UI
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80

# Check UI Pod
kubectl get pods -n kubeflow | grep ui
```

### 4. Resource Management

#### Check Resource Usage
```bash
# Check Node Resources
kubectl top nodes

# Check Pod Resources
kubectl top pods -n kubeflow

# Check Container Resources
kubectl top pods -n kubeflow --containers
```

#### Clean Up Resources
```bash
# Delete Failed Pods
kubectl delete pod <pod-name> -n kubeflow

# Clean Up Completed Jobs
kubectl delete jobs --field-selector status.successful=1 -n kubeflow

# Clean Up Old Pipeline Runs
kubectl delete pipeline <pipeline-name> -n kubeflow
```

### 5. Logging and Debugging

#### View Logs
```bash
# View Pod Logs
kubectl logs <pod-name> -n kubeflow

# View Previous Container Logs
kubectl logs <pod-name> -n kubeflow --previous

# View Logs with Timestamps
kubectl logs <pod-name> -n kubeflow --timestamps
```

#### Debug Pods
```bash
# Describe Pod
kubectl describe pod <pod-name> -n kubeflow

# Exec into Pod
kubectl exec -it <pod-name> -n kubeflow -- /bin/bash

# Check Pod Events
kubectl get events -n kubeflow --sort-by='.lastTimestamp'
```

### 6. Backup and Restore

#### Backup Pipeline
```bash
# Export Pipeline
kubectl get pipeline <pipeline-name> -n kubeflow -o yaml > pipeline-backup.yaml

# Export All Pipelines
kubectl get pipelines -n kubeflow -o yaml > all-pipelines-backup.yaml
```

#### Restore Pipeline
```bash
# Apply Pipeline
kubectl apply -f pipeline-backup.yaml

# Apply All Pipelines
kubectl apply -f all-pipelines-backup.yaml
```

## Features

- 🔄 Simple multiplication pipeline
- ⚙️ Configurable input parameters
- 📦 YAML pipeline export
- 🔍 Pipeline monitoring capabilities
- 🛠️ Easy to extend and modify

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 guidelines
- Add comments for complex logic
- Update documentation as needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **LinkedIn** - [Ratnesh Kushwaha](http://linkedin.com/in/ratneshkushwaha/)
- **YouTube** - [India Analytica](https://www.youtube.com/@IndiaAnalytica)
- **Project Link** - [https://github.com/imratnesh/llmops](https://github.com/imratnesh/llmops)

## Connect With Me

### Professional Profiles
- [LinkedIn Profile](http://linkedin.com/in/ratneshkushwaha/) - Connect with me on LinkedIn for professional networking and updates
- [YouTube Channel](https://www.youtube.com/@IndiaAnalytica) - Subscribe to my YouTube channel for tutorials and tech content

### Social Media
- **GitHub** - [@imratnesh](https://github.com/imratnesh)
- **Project Repository** - [llmops](https://github.com/imratnesh/llmops)

---

## Additional Resources

### Useful Links
- [Kubeflow Documentation](https://www.kubeflow.org/docs/)
- [Kubeflow Pipelines SDK](https://kubeflow-pipelines.readthedocs.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)

### Troubleshooting

Common issues and their solutions:

1. **Pipeline Compilation Error**
   ```bash
   # Check Python version
   python --version
   
   # Verify kfp installation
   pip show kfp
   ```

2. **Connection Issues**
   ```bash
   # Check if Kubeflow is running
   kubectl get pods -n kubeflow
   
   # Verify port forwarding
   kubectl port-forward -n kubeflow svc/ml-pipeline 8080:8888
   ```

---

⭐️ If you find this project helpful, please give it a star!