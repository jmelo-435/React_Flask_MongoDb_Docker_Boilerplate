
<a name="readme-top"></a>

[![MIT License][license-shield]][license-url]


  <h1 align="center">React-Flask-MongoDB-Docker Hello-World</h1>

  <p align="center">
    A boilerplate repository to a dockerized app using React as front-end, Flask as back-end and MongoDb as database.  
    <br />
    <a href="https://github.com/jmelo-435/React_Flask_MongoDb_Docker_Boilerplate/issues">Report Bug</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]()
This app consists in a enviroment with four Docker containers(Ngninx,React,Flask,MongoDb). The front-end allows the creation of elements in the database via API endpoints. The objective of this app is to provide a good start point for projects using this kind of stack, and show how simple is to deploy this kind of Docker based projects. 

### Built With

<p align="left">
  <a href="https://flask.palletsprojects.com/en/2.2.x/">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  </a>
  <a href="https://reactjs.org/">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  </a>
   <a href="https://www.docker.com/">
    <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  </a>
   <a href="https://www.mongodb.com/">
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" />
  </a>
  <a href = "https://www.nginx.com/">
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" />
  </a>
  <a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  </a>
  <a href="https://www.javascript.com/">
  <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
  </a>
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

To set up the enviroment, it's required to have Docker and Docker compose installed in your system. You can install booth following the <a href="https://docs.docker.com/desktop/">oficial documentation</a>. 
After following the steps in the documentation:

1. Check the Docker installation:
    ```sh
   docker --version
   ```

2. Check the Docker Compose installation:
   ```sh
   docker compose version
   ```

### Building the Enviroment


1. Clone the repo
   ```sh
   https://github.com/jmelo-435/React_Flask_MongoDb_Docker_Boilerplate
   ```
2. In the same directory of the docker-compose.yml file, run this command:
   ```sh
   docker compose up
   ```
3. That's it. You can visit your localhost directory and see the app running. Make sure that all your ports are free, otherwise the Docker build will exit    with an error. You can check if your docker containers are running using the following command:
   ```sh
   docker ps
   ```
If you have any questions please feel free to contact me. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Jeferson Melo - jefersonmedeiros000@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


* [Best README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png

