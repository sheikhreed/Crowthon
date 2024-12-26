#!/usr/bin/bash

export_variables(){
    while read line; do
        if [[ $line == *"="* && $line != \#* ]]; then
            export $line
        fi
    done <.env
    echo -e "Variables exported"
}

start_ciraag(){
    if [ -d "venv" ] || [ -d ".venv" ]; then
        if [ -d "venv" ]; then
            source venv/bin/activate
        elif [ -d ".venv" ]; then
            source .venv/bin/activate
        fi
        echo -e "The virtual environment has been successfully activated"
        if [ -f ".env" ]; then
            export_variables
            python3 -m ciraag
        else
            echo ".env not found"
            exit
        fi
    else
        echo "venv not found"
        exit
    fi
}

start_ciraag