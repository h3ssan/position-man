# position-man

## Overview

`position-man` is a Django-based application designed to streamline the management of candidates, job positions, and CV submissions. It leverages the default Django admin panel to provide an intuitive interface for managing recruitment workflows.

## Features

- **Candidate Management**: Add, update, and manage candidate profiles.
- **Position Management**: Create and manage job positions.
- **Submission Tracking**: Link candidates to specific job positions and track their submissions.
- **CV Upload**: Upload and store candidate CVs for easy access.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/h3ssan/position-man.git
    cd position-man
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Access the admin panel at `http://127.0.0.1:8000/`.

## Usage

1. Log in to the Django admin panel using the superuser credentials.
2. Use the admin interface to:
    - Add candidates and upload their CVs.
    - Create job positions.
    - Link candidates to positions by creating submissions.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Description of changes"
    ```
4. Push to your branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Contact

For questions or support, feel free to open an issue.