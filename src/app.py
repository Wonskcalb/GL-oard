import os
from pathlib import Path
from pkgutil import iter_modules, walk_packages
from typing import List

from tartiflette import create_engine
from tartiflette.engine import Engine
from tartiflette_asgi import TartifletteApp

from src import globals
from src import resolvers


def get_schema_files() -> List[str]:
    files = filter(lambda p: p.endswith(".graphql"), os.listdir(globals.SDL_PATH))

    return [os.path.join(globals.SDL_PATH, name) for name in files]


resolved_modules = []

# Find all modules recursively to add them the Engine.modules list
modules = list(iter_modules(resolvers.__path__))
print(modules)

while modules:
    module = modules.pop()

    module_path = Path(module.module_finder.path) / module.name

    if module.ispkg:
        modules.extend(iter_modules([module_path]))

    else:
        resolved_modules.append(
            str(module_path).rsplit("Gloard/")[-1].replace("/", ".")
        )


engine = Engine(
    sdl=get_schema_files(),
    modules=resolved_modules
    + [
        "src.directives.auth",
        "src.directives.rate_limiting",
    ],
)

app = TartifletteApp(engine=engine, graphiql=globals.DEBUG)
