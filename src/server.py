import uvicorn

from src import globals


def run_server():
    uvicorn.run(
        "src.app:app",
        host=globals.SERVER_HOST,
        port=globals.SERVER_PORT,
        debug=globals.DEBUG,
    )


if __name__ == "__main__":
    run_server()
