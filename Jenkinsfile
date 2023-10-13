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
    gittagcommit = sh(returnStdout: true, script: 'git rev-list -n 1 v.123-test').trim().take(8)
}
    stages {
        stage('Build') {
            steps {
                script{
                    setBuildName(buildName: "${params.git-tag-commit}: ${env.shortCommit}")
                }
                
                
            }
        }
        stage('Test') {
            steps {
                echo 'Testing.23123'
                
            }
        }
    }
}

String setBuildName(Map parameters = [:]) {

  echo 'setBuildName parameters: ' + parameters
  def buildName = parameters.get('buildName')  
  currentBuild.displayName = buildName
}