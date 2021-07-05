from tartiflette import Resolver

from src.resolvers.utils import gl_handler


@Resolver("Query.projects")
async def projects(parent, args, context, info):
    gl = await gl_handler()

    return gl.projects.list(archived=args.get("archived", False))
