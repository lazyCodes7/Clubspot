<!-- PROJECT LOGO -->
<br />
<p align="center">


  <h3 align="center">Clubspot</h3>

  <p align="center">
    Clubspot is a web application that tackles the problems of people who want to join clubs and want to manage clubs.

</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Let's think about schools. Almost all schools have student clubs but due to CoVID-19 these clubs have been disrupted. What if there was a way to provide a platform for students to join clubs and for club-admins to monitor attendance, their club-feedback online. These are the problems that Clubspot was built to solve.

### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Django](https://www.djangoproject.com/)
* [SQLite](https://www.sqlite.org/index.html)
* [NLTK](https://opencv.org/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [expert.AI](https://www.expert.ai/)
* [Plotly](https://plotly.com/)
* [Pandas](https://pandas.pydata.org/)



<!-- GETTING STARTED -->
## Getting Started

Follow the instructions to setup the project locally!

### Prerequisites

Make sure to have virtualenv package from python installed before proceeding to installation.
  ```sh
  pip install virtualenv
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/lazyCodes7/Clubspot.git
   ```
2. Activate the virtual environment
   ```sh
   cd Clubspot
   virtualenv venv
   . venv/bin/activate
   ```
3. Install the required packages using pip
   ```sh
   pip install -r requirements.txt
   ```
4. Final step and ta-da open the app!
  ```sh
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver

  ```
## Usage
1. Clubspot provides you with the ability to join, create or search existing clubs
![Screenshot from 2021-09-19 19-21-38](https://user-images.githubusercontent.com/53506835/133930093-c19af1b7-947b-4ec7-816e-3e2473b67ed5.png)

2. On Clubspot it is possible to find activites of your choice once you join the club. Either an admin suggests them for you or we suggest it:)
![Screenshot from 2021-09-19 19-37-08](https://user-images.githubusercontent.com/53506835/133930530-d9e5552d-eaaf-4774-8dbe-050231823661.png)

3. As a club admin we provide data analytics services which helps you in analyzing your attendance data which is collecting dust:)



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

