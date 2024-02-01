# heliopay_api_tests_demo
Automated API tests example for demo purpose, using Behave Framework (Python)
This repo contains basic setup for the demo purpose of the Helio pay. It consists of
creating paylink, and testing paylink endpoint functionality. 
Very basic scenarios have been created. 


### Install all libraries: 
`pip3 install -r requirements.txt`

## How to run tests?
Tests can be run in several ways. 
>Via Terminal 

Open up your terminal and write `behave`
This will run entire test suite. 
It will also ignore all the tests that are not implemented. (They will have custom defined tag @not-implemented)

Note: Since jwt is needed for login, I'm not grabbing jwt value automagically as I do not have internal api for that.
So this demo approach grabs jwt manually, and jwt value must be passed on before the test run. 
Otherwise, tests will fail on authentication. This approach would not be used in reality. It would be automated.  
To add jwt, grab it from browser (after you login) and pass it in terminal befoer behave command: 
`export JWT_TOKEN={HERE_PASTE_JWT_VALUE}`

![Screenshot 2024-02-01 at 5.05.28 PM.png](..%2F..%2F..%2F..%2FDesktop%2FScreenshot%202024-02-01%20at%205.05.28%20PM.png)



>Via IDE

Let us assume you are using PyCharm. You would need to edit your runner confirguation. 
Go to runner -> `Edit Configuration` -> open `Environment Variable` -> for `Name` add value `JWT_TOKEN` -> for `Value` paste jwt value that you grabbed from the browser