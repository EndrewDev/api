#!/bin/bash

VENV_PATH="./venv"

if [ -d "$VENV_PATH" ]; then
	echo "Ativando o ambiente virtual..."
	source "$VENV_PATH/bin/activate"
else
	echo "Error: Ambiente virtual não encontrado no caminho $VENV_PATH"
	exit 1
fi

