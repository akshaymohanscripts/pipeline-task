#!/usr/bin/env groovy

pipeline {

  agent {
    label 'java-docker-slave'
  }

  parameters {
    string(name: 'GitTag', defaultValue: "", description: "Human Readable Git Tag/Github Release (takes precedence over GitSha)")
    string(name: 'GitSha', defaultValue: "", description: '8-chars commit SHA or docker tag')
    string(name: 'DeployTo', defaultValue: "DEV", description: 'Pick environment to deploy to')
  }

  environment {
    shortCommit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim().take(8)
    //gittagcommit = sh(returnStdout: true, script: 'git rev-list -n -1 "v.123-test"').trim().take(8)
    registry = "akshaymohan340/application"
    registryCredential = 'dockerhub_id'
    ansible_cred = '943b9c16-9e94-4438-94e0-b015c6156c0a'
  }
  stages {
    stage('Init') {
      steps {
        script {
                      if (params.GitSha != "") {
            ArtifactSha = params.GitSha
            setBuildName(buildName: "${params.DeployTo}: ${ArtifactSha}")
          } else {
            ArtifactSha = env.shortCommit
            setBuildName(buildName: "${params.DeployTo}: ${ArtifactSha}")
          }
          
          
        }

      }
    }

    stage('Building our image') {
      when {

        expression {
          params.DeployTo == "DEV"
        }

      }
      steps {
        script {
          dockerImage = docker.build registry + ":${ArtifactSha}"
        }
      }
    }
    stage('Deploy our image') {
      when {

        expression {
          params.DeployTo == "DEV"
        }

      }
      steps {
        script {
          docker.withRegistry('', registryCredential) {
            dockerImage.push()
          }
        }
      }
    }
    stage(" execute Ansible") {
      agent {
        label 'ansible-node'
      }

      steps {
        withCredentials([string(credentialsId: 'password', variable: 'password123')]) {
          ansiblePlaybook(disableHostKeyChecking: true, installation: 'Ansible', inventory: 'dev.inv', playbook: 'application.yml', extraVars: [COMMIT_HASH: "${ArtifactSha}", docker_password: "${password123}", host-group: "${params.DeployTo}"])
        }
      }
    }
    stage('Test') {
      steps {
        withAWS(region: 'us-east-1', credentials: 'aws_id') {
          sh 'aws s3 ls'
        }

      }
    }
  }
}

String setBuildName(Map parameters = [: ]) {

  echo 'setBuildName parameters: ' + parameters
  def buildName = parameters.get('buildName')
  currentBuild.displayName = buildName
}