#!/usr/bin/env groovy

pipeline {

    agent { label 'java-docker-slave' }

    parameters {
    string(name: 'GitTag', defaultValue: "", description: "Human Readable Git Tag/Github Release (takes precedence over GitSha)")
    string(name: 'GitSha', defaultValue: "", description: '8-chars commit SHA or docker tag')
    string(name: 'DeployTo', defaultValue: "DEV", description: 'Pick environment to deploy to')
  }

environment{
    shortCommit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim().take(8)
    //gittagcommit = sh(returnStdout: true, script: 'git rev-list -n -1 "v.123-test"').trim().take(8)
    registry = "akshaymohan340/application"
    registryCredential = 'dockerhub_id'
}
    stages {
        stage('Build') {
            steps {
                script{
                    //setBuildName(buildName: "${params.git-tag-commit}: ${env.shortCommit}")
                    sh "echo hello 123"
                }
                
                
            }
        }
    stage('Building our image') {
    steps{
    script {
    dockerImage = docker.build registry + ":${env.shortCommit}"
    }
    }
    }
    stage('Deploy our image') {
steps{
script {
docker.withRegistry( '', registryCredential ) {
dockerImage.push()
}
}
}
}
        stage('Test') {
            steps {
                withAWS(region:'us-east-1',credentials:'aws_id')
                {
                    sh 'aws s3 ls'
                }
                
            }
        }
    }
}

String setBuildName(Map parameters = [:]) {

  echo 'setBuildName parameters: ' + parameters
  def buildName = parameters.get('buildName')  
  currentBuild.displayName = buildName
}