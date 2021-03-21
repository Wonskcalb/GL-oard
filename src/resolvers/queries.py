from typing import Any, Dict, List, Optional

from tartiflette import Resolver


@Resolver("Query.hello")
async def hello(parent, args, context, info):
    name = args["name"]
    return f"Hello, {name}!"
