CoderCo Containers Challenge
For this challenge, I built a Flask app with two routes and used Redis to store a visit counter. Both run in separate containers, managed with Docker Compose.
- / shows a welcome message.
- /count increases the counter and displays the new number.
Building the app
I started by importing Flask and creating the welcome route. Then I added /count, which just returned "Counter coming soon!" while I worked on the rest.
When I first ran the app, I thought only one route was working because I could only see the welcome message. I realised I needed to add /count after the URL to see the other page.
<!-- Add screenshot of the initial Flask app. -->

Next, I added the Redis client to the Python code. The /count function uses incr("visits") to increase the number stored in Redis and return it in a message.
One thing I had to get my head around was the difference between the Python Redis package and Redis itself. The package lets my code talk to Redis, but the actual database runs in its own container.
<!-- Add screenshot of the counter code. -->

Putting it in containers
I wrote a Dockerfile for Flask using a Python base image. It copies my code into /app, installs Flask and the Redis package, and sets the command to run the app. Flask listens on port 5002.
I saved the files, built the image with docker build, then ran a container from it to check the welcome page worked.
<!-- Add screenshot of the Flask Dockerfile and build. -->

For the database, I created another Dockerfile in a separate redis folder. This uses the official redis:7 image, which already includes the Redis server and its startup command.
<!-- Add screenshot of the Redis Dockerfile. -->

Running them together
I created docker-compose.yml with two services: web and redis. Compose puts them on a shared network, so the Flask app can find Redis using redis as the hostname and 6379 as the port.
To start the app from the folder containing the Compose file:
docker compose up --build
The web service maps 5002:5002, so I can open it in my browser at:
- http://localhost:5002/
- http://localhost:5002/count
<!-- Add screenshot of the Compose file. -->

Testing
The welcome page displayed my message. I then opened /count and refreshed it a few times. Each refresh increased the number by one, so the Flask app was successfully talking to Redis.
<!-- Add screenshots of both pages and the counter increasing. -->

What I learnt
- Each Flask route handles a different URL path.
- Redis stores the count; Flask requests an update and displays the result.
- Building an image and running a container are separate steps.
- Dependencies installed on my Mac aren't automatically available inside a container.
- Compose saves me from starting each container and setting up their network manually.
The basic challenge is working. I haven't added the persistence, environment variable or scaling bonuses yet.