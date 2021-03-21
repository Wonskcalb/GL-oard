# GL-oard

(Yes this is an awful pun)

## Requirements

 - Python 3.9

## Project Startup

Currently authentication is not handled, connection with the server and
host/credential definition is done through environment variables

To generate a token, go to `https://<your-gl-host>/-/profile/personal_access_tokens`
and generate a token there with scope `api`
```bash
# Gloard/.env
GITLAB_HOST=https://<your-gl-host>
GITLAB_TOKEN=<token>
```

Once the file is generated, run the following to install the packages and run the server

```bash
poetry install
poetry run uvicorn src.app:app
```
