# Docker Learning 
# Flask is a Python framework for building websites and APIs. It provides tools so you don't have to build everything from scratch.
1. Flask helps you build a Python web app. Your app.py uses Flask to return "Hello, world!" when someone visits /.
2. The Dockerfile describes how to package your app. It specifies Python, installs Flask, copies your code and sets the command to start it.
3. docker build reads the Dockerfile and creates an image. The image contains your app and everything it needs to run.
4. docker run creates and starts a container from that image. Your Flask app runs inside it.
5. You visit the app in your browser. Publishing the container's port, such as with -p 5000:5000, lets your browser reach it at http://localhost:5000.
Flask app → Dockerfile → build image → run container → visit in browser.