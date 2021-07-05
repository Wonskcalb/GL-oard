import logging

import gitlab
from gitlab.exceptions import GitlabAuthenticationError

from src.globals import GITLAB_HOST, GITLAB_TOKEN

logger = logging.getLogger(__name__)


async def gl_handler():
    gl = gitlab.Gitlab(GITLAB_HOST, private_token=GITLAB_TOKEN)

    try:
        gl.auth()
    except GitlabAuthenticationError:
        logging.error("Could not connect user")

    return gl
