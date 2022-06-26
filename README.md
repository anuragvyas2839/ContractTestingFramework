# ContractTestingFramework                 
A framework to publish contract tests.            
             
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
             

