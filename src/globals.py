import os

from environs import Env

env = Env()
env.read_env()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = env.bool("DEBUG", True)

# PATH DEFINITIONS FOR ENGINE CONFIGURATION
# ------------------------------------------------------------
SDL_PATH = os.path.join(BASE_DIR, "sdl")
DIRECTIVES_PATH = os.path.join(BASE_DIR, "directives")
RESOLVERS_PATH = os.path.join(BASE_DIR, "resolvers")

# GITLAB AUTH
# ------------------------------------------------------------
GITLAB_HOST = env.str("GITLAB_HOST")
GITLAB_TOKEN = env.str("GITLAB_TOKEN")
