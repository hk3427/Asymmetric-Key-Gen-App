# Asymmetric-Key-Gen-App

Problem Statement:
Given the hypothetical scenario as discussed above, How can we use Python
programming and Docker Container constructs to develop an simple app that
can be deployed at scale. Assuming a simple Asymmetric-Key-Gen app can handle

10 concurrent requests per second, how can we run multiple asymmetric-key-
gen apps to scale the requests to 500 concurrent requests per second.

Functional Requirements
1. The asymmetric-key-gen app generates a Public-Private Key pair

2. The app should expose a GET /key REST API, which returns a public-
private key pair

3. This Public-Private Key pair must be encapsulated in a JSON object
4. The asymmetric-key-gen app must be packaged as a single docker
container
5. The API exposed by the app works on SSL (optional)
Expected Results
Following results are expected from the system,
1. The app is accessible via REST API
2. The app generates a Public-Private key pair and returns as a json
object


Example API Request
curl -X GET --url http://localhost:8080/key

Example API Response
{
"public_key": "'-----BEGIN RSA PRIVATE KEY-----\nMIIEpA...",
"private_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgk..."
}
