# Presentation Cheat Sheet

## One-line project explanation
"We built a Student Management System and automated its build, testing, containerization and deployment using a CI/CD pipeline."

## Architecture
GitHub -> Jenkins -> Checkout -> Install -> Test -> Docker Build -> Deploy -> Running Container

## What Docker does
Docker packages the application and its dependencies into a container so it runs consistently.

## What Jenkins does
Jenkins automatically executes the pipeline whenever new code is submitted/triggered.

## What CI means
Continuous Integration: frequently integrate code and automatically build/test it.

## What CD means
Continuous Delivery/Deployment: automatically prepare/deploy a validated application.

## Live demo
1. Open application.
2. Add a student.
3. Change a visible text in index.html, e.g. subtitle.
4. git add .
5. git commit -m "Update application"
6. git push
7. Open Jenkins and run the pipeline.
8. Show green SUCCESS.
9. Open localhost:5000 and show updated application.
