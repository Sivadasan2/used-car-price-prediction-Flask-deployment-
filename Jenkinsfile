pipeline{

	environment{

		imagename='siva1975/user_car_price_pred'
		registryCredential='Docker_hub_cred'
		dockerImage=''
	}

agent any { 
	stages{
		stage('Cloning Git'){
			steps{
				git([url:'https://github.com/Sivadasan2/used-car-price-prediction-Flask-deployment-.git',branch: 'master', credentialsId: 'git_credentials'])
			}
		stage('Building the image')
		{

			steps{

				script{dockerImage=docker.build imagename}
			
			}
		}
		stage('Deploy image')
		{
			steps{

				script{

					docker.withregistry('',registryCredential)
					{
						dockerImage.push('latest')
					}

				}
			}
		}
		stage('Remove Unused docker image')
		{
      		steps{
        		sh "docker rmi $imagename:$BUILD_NUMBER"
         		sh "docker rmi $imagename:latest"

		}

	} 
	
}
}