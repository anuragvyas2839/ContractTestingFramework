# ContractTestingFramework                 
A framework to publish contract tests.    
It currently uses a get single user api from [https://reqres.in/](https://reqres.in/) as provider to demonstrate the flow and create a pact.
             
## Requirements:      
Python3     
           
Libraries :              
- pact-python=1.5.2       
- requests==2.27.1      
                  
## What is pact:        
Pact documentation link : [readme](https://docs.pact.io/implementation_guides/python/readme).             
           
## How to run:          
You can run individual files inside */contract_tests* directory to generate pact files for the consumer and producer api corresponding to the file.      
Command : python <path to file inside contract_tests>             
  
## Output:       
Generates pact file in json format.       
File naming convention : \<consumer\>-\<provider\>.json   
The pact output for this framework is here : [displayuserconsumer-getuserprovider.json](https://github.com/anuragvyas2839/ContractTestingFramework/blob/main/displayuserconsumer-getuserprovider.json).      
          
## Understanding major directories :              
- **[contract_tests](https://github.com/anuragvyas2839/ContractTestingFramework/tree/main/contract_tests)** : Each file here is to publish pacts between a specific consumer & provider api. It uses resources from other directories.        
- **[pact_block_params](https://github.com/anuragvyas2839/ContractTestingFramework/tree/main/pact_block_params)** : Each file here corresponds to a file in contract_tests for a specific consumer & provider api. The file contains blocks of params that are needed to create multiple pact interactions for the contract test between our consumer & provider api.       
- **[static_data](https://github.com/anuragvyas2839/ContractTestingFramework/tree/main/static_data)** : Contains all data that would remain static and can be used by test files and utils, eg., the url endpoints.           

 
             

