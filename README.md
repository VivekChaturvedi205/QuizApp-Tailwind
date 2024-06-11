# Quiz App with Tailwind CSS

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Introduction
This is a Quiz Application built with Django and styled using Tailwind CSS. The application allows users to register, log in, choose quizzes based on categories, take quizzes with a countdown timer, and view results with a comparison of right and wrong answers. The application also includes functionality for resetting passwords both inside and outside the web app.

## Features
- **User Registration**: Allows new users to register an account.
- **User Login**: Allows existing users to log in to their account.
- **Choose Category Wise Quizzes**: Users can select quizzes based on different categories.
- **Quiz App**: Users can take quizzes with multiple-choice questions.
- **Count Down Timer**: Each quiz has a countdown timer to limit the time for answering questions.
- **Result Calculation**: After completing the quiz, users can see their results.
- **Show Wrong and Right Answer Comparison**: The result page shows which answers were correct and which were incorrect.
- **Forgot Password (Outside Web App)**: Users can reset their passwords if they forget them, via a form that does not require email.
- **Reset Password (Inside Web App)**: Logged-in users can reset their passwords within the application.

## Technologies Used
- **Django**: The web framework used to build the backend of the application.
- **Tailwind CSS**: A utility-first CSS framework used to style the frontend.
- **JavaScript**: Used for the countdown timer functionality.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/VivekChaturvedi205/QuizApp-Tailwind.git
    cd QuizApp-Tailwind
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (admin):**
    ```bash
    python manage.py createsuperuser
    ```

7. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage
1. **Register and Login:**
    - Visit the `/register/` URL to create a new user account.
    - Login at the `/login/` URL.

2. **Choose a Quiz Category:**
    - After logging in, choose a quiz category from the available options.

3. **Take the Quiz:**
    - Answer the multiple-choice questions within the time limit provided by the countdown timer.

4. **View Results:**
    - After completing the quiz, view your results including a comparison of right and wrong answers.

5. **Reset Password:**
    - **Forgot Password (Outside Web App)**: Visit `/forgot_password/` to reset your password using your username.
    - **Reset Password (Inside Web App)**: Logged-in users can change their password by visiting their profile settings.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any questions or feedback, please contact:
- **Name**: Vivek Chaturvedi
- **Email**: vivekchaubey205@gmail.com
- **GitHub**: [VivekChaturvedi205](https://github.com/VivekChaturvedi205)
