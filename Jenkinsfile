node {
    logstashSend failBuild: true, maxLines: 1000
    stage('build') {
       echo 'I only build on the master branch'
    }
    stage('test') {
       echo 'I only test on the master branch'
    }
    stage('deploy') {
       echo 'I only deploy on the master branch'
    }
}
timestamps {
  logstash {
    node('somelabel') {
      sh'''
      echo 'Hello, World!'
      '''
    }
  }
}