# alx-backend-user-data

Repository for ALX Backend User Authentication Service

## Table of Contents

1. [User Model](#user-model)
2. [Create User](#create-user)
3. [Find User](#find-user)
4. [Update User](#update-user)
5. [Hash Password](#hash-password)
6. [Register User](#register-user)
7. [Basic Flask App](#basic-flask-app)
8. [Credentials Validation](#credentials-validation)
9. [Generate UUIDs](#generate-uuids)
10. [Get Session ID](#get-session-id)
11. [Log In](#log-in)
12. [Find User by Session ID](#find-user-by-session-id)
13. [Destroy Session](#destroy-session)
14. [Log Out](#log-out)
15. [User Profile](#user-profile)
16. [Generate Reset Password Token](#generate-reset-password-token)
17. [Get Reset Password Token](#get-reset-password-token)
18. [Update Password](#update-password)
19. [Update Password Endpoint](#update-password-endpoint)

---

### User Model
Implementation of a SQLAlchemy `User` model for a database table named `users`.

### Create User
Implementing the `add_user` method in the `DB` class to add a new user to the database.

### Find User
Implementing the `find_user_by` method in the `DB` class to search for a user based on given criteria.

### Update User
Implementing the `update_user` method in the `DB` class to update a user's attributes in the database.

### Hash Password
Implementing the `_hash_password` function to securely hash passwords using bcrypt.

### Register User
Implementing the `register_user` method in the `Auth` class to register a new user with email and password.

### Basic Flask App
Setting up a basic Flask app with a single route ("/") returning a JSON payload.

### Credentials Validation
Implementing the `valid_login` method in the `Auth` class to validate user credentials.

### Generate UUIDs
Implementing the `_generate_uuid` function in the `auth` module to generate UUIDs.

### Get Session ID
Implementing the `create_session` method in the `Auth` class to create a session ID for a user.

### Log In
Implementing a login endpoint ("/sessions") to authenticate users and set session cookies.

### Find User by Session ID
Implementing the `get_user_from_session_id` method in the `Auth` class to retrieve a user based on session ID.

### Destroy Session
Implementing the `destroy_session` method in the `Auth` class to delete a user's session.

### Log Out
Implementing a logout endpoint ("/sessions") to destroy a user's session.

### User Profile
Implementing a user profile endpoint ("/profile") to retrieve user information based on session ID.

### Generate Reset Password Token
Implementing the `get_reset_password_token` method in the `Auth` class to generate a reset password token.

### Get Reset Password Token
Implementing a reset password endpoint ("/reset_password") to generate and return a reset token.

### Update Password
Implementing the `update_password` method in the `Auth` class to update a user's password using a reset token.

### Update Password Endpoint
Implementing an update password endpoint ("/reset_password") to allow users to update their password using a reset token.

