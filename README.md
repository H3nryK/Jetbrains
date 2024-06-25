<p align="center">
    <img src="./frontend/assets/images/logo.png" alt="Jetbrains College" width="170" height="170">
</p>

# <p align="center">Jetbrains Institute of Information Technologies</p>

The official website for our institution for efficient service &amp; information delivery to our community.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contributing)
- [Appreciation](#appreciation)

## About

Jetbrains College provides a wide range of courses designed to equip students with practical skills in web development, programming, and computer packages. Our mission is to empower learners with the knowledge they need to succeed in the digital age.

## Features

- Responsive web design
- Interactive course cards
- Student testimonials carousel
- Contact form and information
- Smooth scrolling navigation
- Preloader animation
- Sticky navbar
- Social media integration

## Installation

To run Jetbrains College locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/H3nryK/Jetbrains.git
    ```
2. Get inside the directory:
    ```bash
    cd Jetbrains
    ```
3. Install the dependencies:
    ```bash
    pip install django, pillow, whitenoise
    ```

## Usage 

Once done with the installation:

1. Get inside the frontend directory and run the static files:
    ```bash
    cd frontend
    ```
2. Open the `index.html`.

or alternatively:

3. Get inside the backend directory:
    ```bash
    cd backend
    ```
4. Make migrations:
    ```bash
    py manage.py makemigrations
    py manage.py migrate
    ```
5. Collect static files:
    ```bash
    py manage.py collectstatic
    ```
    type `yes` if prompted.
6. Run the server:
    ```bash
    py manage.py runserver
    ```
    navigate to `http://localhost:8000` in your web browser to access the website.

## Contributing

We welcome contributions from the community! If you would like to contribute to Jetbrains College, please follow these guidelines:

- Fork the repository
- Create your feature branch (`git checkout -b feature/AmazingFeature`)
- Commit your changes (`git commit -m 'Add some AmazingFeature'`)
- Push to the branch (`git push origin feature/AmazingFeature`)
- Open a pull request

## Appreciation

We would like to extend our heartfelt thanks to everyone who has contributed to the success of Jetbrains College. Your support, feedback, and contributions have been invaluable in shaping this project into what it is today.

Special thanks to:

- Mr. Samuel Njenga
- Our amazing community of users - Your enthusiasm and feedback drive us to continually improve Jetbrains College.

Thank you all for being part of our journey!

<p align="center">
    -----------------------------------------------------------------------------
</p>

<p align="center">
    ©2024 Jetbrains College || All rights reserved.
</p>