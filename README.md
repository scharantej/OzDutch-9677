## Application Design for Flashcard Translation

### HTML Files

- **index.html**: This file will be the main page of the application. It will provide a form for users to input flashcards.
- **results.html**: This file will display the translated flashcards.

### Routes

- **Homepage**: `/`
    - This route will render the `index.html` file.
- **Translate**: `/translate`
    - This route will handle the form submission from the index page.
    - It will use the Flask-Translate extension to translate the flashcards.
    - It will then render the `results.html` file with the translated flashcards.

### Notes

- The application will use Bootstrap for its frontend design.
- The application will not refer to any local files, ensuring it can be deployed to any platform.