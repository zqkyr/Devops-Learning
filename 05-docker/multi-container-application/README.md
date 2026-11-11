CoderCo Containers Challenge


For this challenge, I built a Flask app with two routes and used Redis to store a visit counter. Both run in separate containers, managed with Docker Compose.

- / shows a welcome message.
- /count increases the counter and displays the new number.

Building the app:

I started by importing Flask and creating the welcome route.


<img width="1000" height="1000" alt="IMG_6526" src="https://github.com/user-attachments/assets/ccdae500-eee0-4cd0-b692-b8169d4df98f" />




Then I added /count, which just returned "Counter coming soon!" while I worked on the rest.

When I first ran the app, I thought only one route was working because I could only see the welcome message. I realised I needed to add /count after the URL to see the other page.



<img width="3000" height="1121" alt="Welcome " src="https://github.com/user-attachments/assets/2389e3d6-a837-4e1d-bf01-e4901e924afc" />


<img width="4202" height="1121" alt="IMG_6528" src="https://github.com/user-attachments/assets/905dfd63-1a1b-4b3c-863b-f22a0dce564a" />




Next, I added the Redis client to the Python code. The /count function uses incr("visits") to increase the number stored in Redis and return it in a message.
One thing I had to get my head around was the difference between the Python Redis package and Redis itself. The package lets my code talk to Redis, but the actual database runs in its own container.




<img width="4284" height="5712" alt="Count incr " src="https://github.com/user-attachments/assets/c3ad7b01-89ce-4f25-829c-3dc640e523b5" />



Putting it in containers:

I wrote a Dockerfile for Flask using a Python base image. It copies my code into /app, installs Flask and the Redis package, and sets the command to run the app. Flask listens on port 5002.

I saved the files, built the image with docker build, then ran a container from it to check the welcome page worked.



<img width="4223" height="2366" alt="Dockerfilepython2" src="https://github.com/user-attachments/assets/034f8b1f-dbc2-4e13-ab1f-d489e0552ad5" />




For the database, I created another Dockerfile in a separate redis folder. This uses the official redis:7 image, which already includes the Redis server and its startup command.


<img width="3024" height="4032" alt="IMG_6532" src="https://github.com/user-attachments/assets/2bac7bda-c1d0-4941-83ac-8ad475acdc74" />


Running them together:



I created docker-compose.yml with two services: web and redis. Compose puts them on a shared network, so the Flask app can find Redis using redis as the hostname and 6379 as the port.




<img width="4284" height="5712" alt="IMG_6531" src="https://github.com/user-attachments/assets/256445c7-6ba5-4fde-869a-bcedd2099d6a" />



To start the app from the folder containing the Compose file:

docker compose up --build

The web service maps 5002:5002, so I can open it in my browser at:
- http://localhost:5002/
- http://localhost:5002/count




<img width="4284" height="5712" alt="IMG_6533" src="https://github.com/user-attachments/assets/9e5f1eed-cec1-4f29-80e5-ef4cd8031b7f" />




Testing:
The welcome page displayed my message. I then opened /count and refreshed it a few times. Each refresh increased the number by one, so the Flask app was successfully talking to Redis.




<img width="2965" height="852" alt="IMG_6534" src="https://github.com/user-attachments/assets/23326401-5ebd-4b08-9f2f-0dff0a7b6563" />


<img width="4148" height="975" alt="IMG_6536" src="https://github.com/user-attachments/assets/41292f8a-7c93-467c-9d8f-9053e1727088" />




What I learnt:

- Each Flask route handles a different URL path.

- Redis stores the count; Flask requests an update and displays the result.

- Building an image and running a container are separate steps.

- Dependencies installed on my Mac aren't automatically available inside a container.

- Compose saves me from starting each container and setting up their network manually.




The basic challenge is working. I haven't added the persistence, environment variable or scaling bonuses yet.
