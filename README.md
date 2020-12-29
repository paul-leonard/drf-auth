# drf-auth
A website and database to daily journal entries was created using Django web and REST framework and containerized using Docker.  Permissions are established so that only the authors can modify and delete their own stories.

## Lab Submission Pull Requests
[Lab33: Authentication & Production Server](https://github.com/paul-leonard/drf-auth/pull/1)

## Release Info
**Author**: Paul Leonard
**Version**: 0.9.0

## Overview
A website and database to daily journal entries was created using Django web and REST framework and containerized using Docker.  Permissions are established so that only the authors can modify and delete their own stories.

## Architecture
Website, consisting of webpages and a postgresql database, created using the Django web framework with full Create, Read, Update, and Delete (CRUD) capabilities which are accessible through the Django REST Frameworks API. The website is containerized using Docker.  Restricted permissions are established to prevent inadvertent modification and deletion of book instances stored in the database.  JSON Web Tokens (JWT) are planned to be used for authentication when accessing via API.

## Change Log
**0.9.0** 12-28-2020 - Initial beta release
**1.0.0** 12-TBD-2020 - Initial release

## Testing
Tested the API with JWT authentication using terminal based HTTPie.  First, information was requested without providing any credentials... and access was denied.  Next, a token was requested with username/password supplied.  An access and refresh token were supplied.  Using one of the tokens provided, another request for data was sent.  The API determined correct access and returned the requested data successfully.

## Credits and Collaborations
- intentionally left blank
