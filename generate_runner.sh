#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Usage: ./generate_runner.sh <conda_env_name> <your_script_path>"
  exit 1
fi

CONDA_ENV_NAME="$1"
SCRIPT_PATH="$(realpath "$2")"
TEMPLATE_FILE="runner.sh.in"
OUTPUT_FILE="runner.sh"

sed -e "s|@CONDA_ENV_NAME@|$CONDA_ENV_NAME|g" \
    -e "s|@SCRIPT_PATH@|$SCRIPT_PATH|g" \
    "$TEMPLATE_FILE" > "$OUTPUT_FILE"
chmod +x "$OUTPUT_FILE"