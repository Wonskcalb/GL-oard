import logging
from typing import Any, Dict, List, Optional

import gitlab
from gitlab.exceptions import GitlabAuthenticationError
from tartiflette import Resolver

from src.globals import GITLAB_HOST, GITLAB_TOKEN

logger = logging.getLogger(__name__)


@Resolver("Query.projects")
async def projects(parent, args, context, info):
    gl = gitlab.Gitlab(GITLAB_HOST, private_token=GITLAB_TOKEN)

    try:
        gl.auth()
    except GitlabAuthenticationError as e:
        logging.error("Could not connect user")

    return gl.projects.list(archived=args.get("archived", False))
