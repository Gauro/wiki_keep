# WikiKeep

WikiKeep is a Python module for managing and saving Wikipedia articles. It provides a backend server built using FastAPI that allows users to register, login, save articles, retrieve articles, retrieve tags, and filter articles based on tags and users.

## Features

- User registration and login
- Saving articles with tags
- Retrieving articles based on tags and users
- Real-time communication via WebSocket
- Sentiment analysis of articles

## Installation

To install WikiKeep, you can use pip:

```
pip install wiki_keep
```
Alternatively, you can clone this repository and install the dependencies listed in req.txt.


Usage
1. Register a User: Use the /register endpoint to register a new user by providing a username, password, and email.
2. Login: Use the /login endpoint to login with the registered credentials.
3. Save Article: Use the /save_article endpoint to save an article by providing the title, content, tags, and user ID.
4. Retrieve Article: Use the /article endpoint to retrieve an article by providing its title.
5. Retrieve Tags: Use the /tags endpoint to retrieve tags associated with a user.
6. Filter Articles on Tag: Use the /filter_articles_on_tag endpoint to filter articles based on a tag and user ID.
7. Real-time Communication: Use the WebSocket endpoint /ws for real-time communication to search and save articles.


Configuration
WikiKeep uses a configuration file config.ini to store MySQL database connection details and other environment variables. You can find the configuration file in the data directory.
