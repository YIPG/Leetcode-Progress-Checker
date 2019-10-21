# Leetcode Progress Checker

This is Leetcode Progress Checker for your own account.

Image is like below.

<p align="center">
<img src="https://pbs.twimg.com/media/EC4_LWPUwAAseOb?format=jpg&name=large" width="350px" />
</p>

# Requirement

We use `pipenv` in order to manage dependencies. So first of all, Install pipenv.

Then, we have to install dependencies.

```shell
pipenv install
```

Good! And you have to set Twitter API key and leetcode id/password to `.env`. It's like below one.

```shell
# Leetcode id or email
USER_NAME=your_leetcode_id_or_email

# Leetcode password
PASSWORD=your_pass

# Twitter Api
CONSUMER_KEY=your_key
CONSUMER_SECRET=your_key
ACCESS_TOKEN_KEY=your_key
ACCESS_TOKEN_SECRET=your_key
```

# How to use

Enter below command and check your timeline! :)

```shell
pipenv run start
```

Enjoy leetcode life.
