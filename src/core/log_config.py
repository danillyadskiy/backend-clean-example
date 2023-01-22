import uvicorn

LOG_CONFIG = uvicorn.config.LOGGING_CONFIG
LOG_CONFIG["formatters"]["access"][
    "fmt"
] = "%(levelprefix)s %(asctime)s - %(client_addr)s - %(request_line)s %(status_code)s"
LOG_CONFIG["formatters"]["default"]["fmt"] = "%(levelprefix)s %(asctime)s - %(message)s"
