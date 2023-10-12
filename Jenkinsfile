#!/usr/bin/env groovy

pipeline {

    agent { label 'java-docker-slave' }

    parameters {
    string(name: 'GitTag', defaultValue: "", description: "Human Readable Git Tag/Github Release (takes precedence over GitSha)")
    string(name: 'GitSha', defaultValue: "", description: '8-chars commit SHA or docker tag')
    string(name: 'DeployTo', defaultValue: "DEV", description: 'Pick environment to deploy to')
  }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                
            }
        }
        stage('Test') {
            steps {
                echo 'Testing.123'
                
            }
        }
    }
}