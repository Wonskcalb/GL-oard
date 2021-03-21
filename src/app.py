import os
from pkgutil import iter_modules
from typing import List

import asyncio
from tartiflette import create_engine
from tartiflette.engine import Engine
from tartiflette_asgi import TartifletteApp

import src.globals as settings


def get_schema_files() -> List[str]:
    files = filter(lambda p: p.endswith(".graphql"), os.listdir(settings.SDL_PATH))

    return [os.path.join(settings.SDL_PATH, name) for name in files]


engine = Engine(
    sdl=get_schema_files(),
    modules=[
        "src.resolvers.queries",
        "src.resolvers.mutations",
        "src.resolvers.subscriptions",
        "src.directives.auth",
        "src.directives.rate_limiting",
    ],
)

app = TartifletteApp(engine=engine, graphiql=settings.DEBUG)
