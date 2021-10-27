<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/FxL5qM0.jpg" alt="Bot logo"></a>
</p>

<h3 align="center">Python IP telegram Bot</h3>

<div align="center">

</div>

---

<p align="center"> 🤖 Few lines describing what your bot does.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Demo / Working](#demo)
- [How it works](#working)
- [Usage](#usage)
- [Getting Started](#getting_started)
- [Deploying your own bot](#deployment)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Bot to add and control some different utilities in your raspberry pi.

## 🎥 Demo / Working <a name = "demo"></a>

![Working](https://media.giphy.com/media/20NLMBm0BkUOwNljwv/giphy.gif)

## 💭 How it works <a name = "working"></a>

It just creates a telegram bot ready to respond with the public IP address of his host machine.


## 🎈 Usage <a name = "usage"></a>

Standalone:

  1 - Create the TELEGRAM_TOKEN env variable using your bot's token
  2 - run : python3 ./main.py

Docker:
  You have 2 options:
  - Build the image by yourself using:
    
    docker build --build-arg --pull --rm -f "Dockerfile" -t name:tag "."

  -Or pull the image from:

    https://hub.docker.com/repository/docker/suarez605/python-ip-telegram-bot

  <b>linux/arm64:</b>
    docker pull suarez605/python-ip-telegram-bot:latest

  <b>linux/arm64</b>
    docker pull suarez605/python-ip-telegram-bot:latest-arm

  And running it with:
  
    docker run -e TELEGRAM_TOKEN=YOUR_TOKEN_HERE  rasp-ip-bot


## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

  Creating a telegram bot and get the TOKEN.
  Have Docker in your machine to run your custom images.
  Python +3.6
  Pip

### Installing

Just clone the repo into your favourite IDE.

## 🚀 Deploying your own bot <a name = "deployment"></a>

docker run -e TELEGRAM_TOKEN=YOUR_TOKEN_HERE  rasp-ip-bot

## ⛏️ Built Using <a name = "built_using"></a>

- [PRAW](https://praw.readthedocs.io/en/latest/) - Python Reddit API Wrapper
- [Heroku](https://www.heroku.com/) - SaaS hosting platform

## ✍️ Authors <a name = "authors"></a>

- [@suarez605](https://github.com/suarez605)
