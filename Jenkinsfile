pipeline {
  agent { docker { image 'python:3.5.1' } }
  stages {
    stage('version') {
      steps {
        powershell "python --version"
      }
    }
    stage('hello') {
      steps {
        powershell "python playground.py"
      }
    }
  }
}
