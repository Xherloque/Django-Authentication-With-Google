# Django Google Authentication System

This project demonstrates how to set up a **Django project** with Google authentication, allowing users to register and log in either using Django’s built-in authentication system or their Google account. It also includes features like a well-styled homepage, user profile management, and more.

---

## Features

1. **Registration**  
   Users can register with:
   - Django’s built-in authentication system.
   - Google account authentication.

2. **Login**  
   - Log in with a username/email and password.
   - Log in using Google authentication.

3. **User Profile**  
   - Displays the user’s profile with details.

4. **Homepage**  
   - Simple homepage after login.

5. **Styling**  
   - Clean and attractive templates styled with CSS and JavaScript.

---

## Prerequisites

1. Python 3.8 or higher installed.
2. Django 5.1 or higher.
3. A Google Cloud Console account.
4. Git for version control.

---

## Setup Instructions

### Step 1: Clone the Repository

1. Open your terminal and navigate to the directory where you want the project.
2. Clone the repository:
   ```bash
   git clone <repository_url>
   cd django-google-auth
   ```

---

### Step 2: Set Up a Virtual Environment

1. Create a virtual environment:
   ```bash
   python -m venv env
   ```
2. Activate the environment:
   - Windows:
     ```bash
     env\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source env/bin/activate
     ```

---

### Step 3: Install Dependencies

Install the required Python packages:
```bash
pip install -r requirements.txt
```

---

### Step 4: Configure Google API Console

1. Go to [Google Cloud Console](https://cloud.google.com/).
2. Create a new project:
   - Click **"Select a Project"** → **"New Project"**.
   - Enter a name and click **"Create"**.
3. Enable the **Google People API**:
   - Navigate to **APIs & Services** → **Library**.
   - Search for "Google People API" and enable it.
4. Set up **OAuth Consent Screen**:
   - Go to **APIs & Services** → **OAuth Consent Screen**.
   - Configure as **External** and complete the required fields.
5. Create **OAuth Credentials**:
   - Navigate to **APIs & Services** → **Credentials**.
   - Click **Create Credentials** → **OAuth Client ID**.
   - Choose **Web Application** and add `http://127.0.0.1:8000` to the **Authorized Redirect URIs**.
   - Save the credentials file (`client_secret.json`) and place it in your Django project directory.

---

### Step 5: Configure the Django Project

1. Create a `.env` file in the root of the project and add:
   ```plaintext
   DJANGO_SECRET_KEY=<your_secret_key>
   GOOGLE_CLIENT_ID=<your_client_id>
   GOOGLE_CLIENT_SECRET=<your_client_secret>
   ```

2. Migrate the database:
   ```bash
   python manage.py migrate
   ```

3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

### Step 6: Test the Application

1. Visit `http://127.0.0.1:8000/` in your browser.
2. Register or log in using:
   - Django Authentication.
   - Google Authentication.

---

## Folder Structure

```
django-google-auth/
├── accounts/            # Main app for user authentication
├── templates/           # Contains HTML templates
│   ├── base.html        # Base template
│   ├── register.html    # User registration template
│   ├── login.html       # Login page template
│   ├── login_password.html  # Password entry template
│   ├── homepage.html    # Homepage after login
│   ├── profile.html     # User profile template
├── static/              # Static files (CSS, JS, images)
│   ├── css/
│   │   └── styles.css   # Styling for all templates
│   ├── js/
│   │   └── scripts.js   # JavaScript for interactivity
├── manage.py            # Django management script
├── requirements.txt     # List of required Python packages
├── .env                 # Environment variables
├── db.sqlite3           # SQLite database (optional if using another DB)
```

---

## Key Templates

### `register.html`

Provides the user with two options for registration:  
- Traditional (username/password).  
- Google Authentication.

### `login.html`

Allows users to:
- Input their username/email to proceed with Django login.
- Log in directly using Google Authentication.

### `homepage.html`

Welcomes the user upon successful login.

### `profile.html`

Displays user profile information, such as username and email.

---

## Styling and Design

The project is styled using CSS and JavaScript for a professional look and feel. You can customize styles by modifying files in the `static/css` and `static/js` directories.

---

## Troubleshooting

1. **Database Errors**:
   Ensure migrations are applied:
   ```bash
   python manage.py migrate
   ```

2. **Google OAuth Redirect Errors**:
   - Check if the redirect URI is properly configured in Google Cloud Console.

3. **Static Files Not Loading**:
   Run the following command to collect static files in production:
   ```bash
   python manage.py collectstatic
   ```

---

## Contributing

Feel free to fork the repository and submit a pull request for improvements or bug fixes.

---

## License

This project is licensed under the MIT License.
