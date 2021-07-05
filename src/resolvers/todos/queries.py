from tartiflette import Resolver

from src.resolvers.utils import gl_handler


@Resolver("Query.todos")
async def get_todos(parent, args, context, info):
    gl = await gl_handler()

    return gl.todos.list()
