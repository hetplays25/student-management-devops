# Automated CI/CD Pipeline for a Student Management System

## Project
A simple Flask + SQLite Student Management System automated using GitHub, Jenkins and Docker.

## Local run without Docker
1. Install Python 3.12+.
2. Create a virtual environment:
   `python -m venv .venv`
3. Activate it on Windows:
   `.venv\Scripts\activate`
4. Install dependencies:
   `pip install -r requirements.txt`
5. Run:
   `python app.py`
6. Open:
   `http://localhost:5000`

## Test
`pytest -q`

## Run with Docker
Build:
`docker build -t student-management .`

Run:
`docker run -d --name student-management -p 5000:5000 student-management`

Open:
`http://localhost:5000`

## Docker Compose
`docker compose up --build`

## CI/CD flow
Developer -> GitHub -> Jenkins -> Test -> Docker Build -> Docker Container -> Application

## Important
For the presentation, the simplest reliable Jenkins demonstration is:
1. Push a code change to GitHub.
2. Trigger the Jenkins job (manually with Build Now if GitHub webhook is not configured).
3. Show Checkout -> Tests -> Docker Build -> Deploy -> SUCCESS.
4. Open localhost:5000 and show the updated application.


## Jenkins using Docker Desktop (Windows)
The supplied `jenkins/Dockerfile` creates a Jenkins image with Python, Git and Docker CLI.

From the project folder:
1. `docker build -t student-jenkins -f jenkins/Dockerfile .`
2. `docker run -d --name jenkins --restart unless-stopped -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v //var/run/docker.sock:/var/run/docker.sock --user root student-jenkins`
3. Open `http://localhost:8080`.
4. Get the first password with:
   `docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword`
5. Install the suggested plugins.
6. Create a Pipeline job and point it to your GitHub repository, using the Jenkinsfile in the repository.
7. Click Build Now for the first run.
8. For automatic polling, configure the job's Build Triggers -> Poll SCM and use `H/2 * * * *`.

If Docker Desktop on your machine does not expose `/var/run/docker.sock`, use the GitHub Actions workflow included in `.github/workflows/ci.yml` for the CI portion and keep Docker Compose for the live application demo.
