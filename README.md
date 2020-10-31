# Test_Runner_Service

This is REST API service that is used for running existing
API Black Box tests. 

The service expects to receive a GET request that 
contains the name of the test file or a name of a folder that
contains test files. 

Once it happens the requested tests are executed, 
a report with executed tests results is sent in response as JSON.

The Test Runner Service can be placed together with the tests in 
Docker container (see requirements list) - while the container is
running each test can be executed on client's request. 

Build image "test_runner"

Run with:
**docker run -it -p 5000:5000 test_runner**