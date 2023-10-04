# Implementation (NodeJs Web application)

## Implementation

To set up and run this Node.js web application, follow these steps:

### 1. Install Node.js

Install Node.js, You can download it from the official website: [Node.js Download](https://github.com/nodesource/distributions#nodejs).

* Download and import the Nodesource GPG key

```sh
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
```

* Create deb repository

```sh
NODE_MAJOR=18
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
```

> ***Optional***: ``NODE_MAJOR`` can be changed depending on the version you need.
>
> ```sh
> NODE_MAJOR=16
> NODE_MAJOR=18
> NODE_MAJOR=20
> ```

* Run Update and Install

```sh
sudo apt-get update
sudo apt-get install nodejs -y
```
## To Get Ready for Running the Project

### Step 1: Add your OPENAI_API_KEY to the project
```
$ cp .env.example .env
$ vi .env
```
Copy your OpenAi API Key into the file.

### Step 2: Install Dependencies
Install packages needed for Next.js project
```
$ npm install
```

Install packages needed to run Python Scripts
```
$ npm run install
```
### 3. Update Package.json Scripts

Update your `package.json` file to include the following scripts:

```json
"scripts": {
    "install": "pip install -r requirements.txt",
    "crawl": "python3 crawl.py",
    "embed": "python3 embed.py"
},
```

These scripts are used to install Python dependencies, crawl a website, and create embeddings.
### Step 3: Crawl Data and Embedding

I keep crawling data and embedding seperate from the main program to avoid TIMEOUT error and save cost on embedding.

* Crawl Data First

```
$ npm run crawl
```
<br>

* Then Embedding Data

Since we need to use the OpenAI model to embedding the data, we need to config the key before running this.

```
$ export OPENAI_API_KEY=<YOUR_API_KEY>
$ npm run embedding
```

## Run

```
$ npm run dev
```
Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.
