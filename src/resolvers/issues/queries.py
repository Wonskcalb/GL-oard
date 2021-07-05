from tartiflette import Resolver

from src.resolvers.utils import gl_handler


@Resolver("Query.issues")
async def issues(parent, args, context, info):
    gl = await gl_handler()

    if project_id := args.get("projectId"):
        handler = gl.projects.get(project_id).issues.list
    else:
        handler = gl.issues.list

    query_kwargs = {}
    if state := args.get("state"):
        query_kwargs["state"] = state.lower()

    return handler(**query_kwargs)
