# Asymmetric-Key-Gen-App

Problem Statement:
Given the hypothetical scenario as discussed above, How can we use Python
programming and Docker Container constructs to develop an simple app that
can be deployed at scale. Assuming a simple Asymmetric-Key-Gen app can handle
10 concurrent requests per second, how can we run multiple asymmetric-key-
gen apps to scale the requests to 500 concurrent requests per second.

<br>
Functional Requirements:
<br>
1. The asymmetric-key-gen app generates a Public-Private Key pair
<br>
2. The app should expose a GET /key REST API, which returns a public-
private key pair
<br>
3. This Public-Private Key pair must be encapsulated in a JSON object
<br>
4. The asymmetric-key-gen app must be packaged as a single docker
container
<br>
5. The API exposed by the app works on SSL (optional)
<br>
<br>
<br>

Expected Results : 
<br>
Following results are expected from the system,
1. The app is accessible via REST API
2. The app generates a Public-Private key pair and returns as a json
object.
<br>
<br>

Example API Request : <br>
curl -X GET --url http://localhost:8080/key

<br>
Example API Response : <br>
{
"public_key": "'-----BEGIN RSA PRIVATE KEY-----\nMIIEpA...",
<br>
"private_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgk..."
}
