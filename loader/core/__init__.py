from os import environ

MIN_PY = 3.8
MAX_PY = 4.0

CONF_PATH = "config.env"

# will be removed after pluggable utils and res
CORE_REPO = environ.get('CORE_REPO', "https://github.com/daviisdev/Hilzu")
CORE_BRANCH = environ.get('CORE_BRANCH', "master")
