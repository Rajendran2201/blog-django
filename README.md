# Django Blog Website

This is a blog website built using Django, a high-level Python web framework. The project allows users to read blog posts, create new posts, and manage existing posts. It also includes features like user authentication and a rich-text editor for creating blog content.

## Features

- User registration and login.
- CRUD (Create, Read, Update, Delete) functionality for blog posts.
- Categories and tags for organizing posts.
- Search functionality to find specific posts.
- Responsive design using Bootstrap (or your chosen CSS framework).
- Admin panel for managing users and posts.
- Pagination for better user experience.

## Technologies Used

- **Django**: Backend framework for building the application.
- **SQLite**: Default database for development (can be replaced with PostgreSQL/MySQL in production).
- **HTML/CSS**: For front-end design.
- **JavaScript**: For interactivity.
- **Bootstrap** (or your preferred CSS framework): For responsive UI.
- **Rich Text Editor**: Integrated for creating and editing blog posts.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Rajendran2201/blog-django.git
   cd blog-django
   ```

2. Create a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open the application in your browser at `http://127.0.0.1:8000`.

## Usage

1. Navigate to the home page to view all blog posts.
2. Use the search bar to find posts by title or content.
3. Log in or register to create and manage your own blog posts.
4. Admin users can manage posts and users via the Django admin panel.


## Future Enhancements

- Adding a commenting system for posts.
- Implementing post likes/dislikes or reactions.
- Supporting image uploads in posts.
- Adding RSS feed support for blog posts.
- Enabling social media sharing of posts.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

