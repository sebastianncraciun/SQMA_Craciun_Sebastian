pipeline {
    agent any
    parameters {
        choice(name: 'TEST_CASE', choices: ['test_case1', 'test_case2'], description: 'Select which test case to run')
    }
    environment {
        VENV_PATH = "${WORKSPACE}/venv"  // Virtual environment path
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sebastianncraciun/SQMA_Craciun_Sebastian'
            }
        }
        stage('Setup Environment') {
            steps {
                script {
                    if (!fileExists(env.VENV_PATH)) {
                        sh 'python3 -m venv venv'
                    }
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh "./venv/bin/python -m unittest discover -s tests -p tests/${params.TEST_CASE}.py"
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
            junit '**/TEST-*.xml'
        }
    }
}