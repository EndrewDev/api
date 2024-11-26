#!/bin/bash

if [ -n "$VIRTUAL_VENV" ]; then
	echo "Desativando o ambiente virtual..."
	deactivate
else
	echo "Nenhum ambiente virtual está ativo."
fi
