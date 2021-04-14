# DiazRock-instagram

This is a tiny clone of instagram, for learn how to use django and its features.

## The applications of the project

The prohject has two applications:

- Posts
- Users

### Posts app

The application `posts`, defines all the features of a post in diazrock-instagram. Each post can be created, liked, and inspect in its details. You can get the global feed of posts of all users, or of the users that you follow.

Inside, you can see the definition of `Post` model, for the post entity stored in the database, and a `PostLike` model, for express the many-to-many relation between liked posts and users.

### Users app

The application `users`, is related to all a user can do in diazrock-instagram.
You can register, login/logout, update your profile, follow/unfollow other users, create post, and like others.

Inside, you can see the definition of `Profile` model, for the user entity stored in the database, and a `FollowerRelation` model, for express the many-to-many relation between in following between users.


## Install app

You can install the app in dev mode, following the next instructions:

- Clone the repo
- `pipenv install`
- `pipenv shell`
- `cd ./platzigram`
- `./manage.py runserver`

## Deploy to heroku

It will become, very soon!!
