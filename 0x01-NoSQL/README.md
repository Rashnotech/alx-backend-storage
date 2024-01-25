# No SQL
No SQL means "Not only SQL"

## Installation
Before Installing Mongo Database make sure you are the root user else always use sudo

**STEP 1**
This step gives you access to generate a public key before downloading mongo db on your local machine. Using shell pipe to add key.
```
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
```

**STEP 2**
Create a source list directory for mongo db using this instruction.
```
echo "deb [ arch=amd64,arm64] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
```
