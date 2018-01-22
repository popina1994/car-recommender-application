#!/bin/bash

PROJECT_DIR=$(dirname $0)
echo -e $PROJECT_DIR
ENV="../${PROJECT_DIR}/env"

if [[ ! -e ${ENV} ]]; then
    echo -e "Pravljenje virtual env-a\n"
    virtualenv -p python3 ${ENV}
elif [[ ! -d ${ENV} ]]; then
    echo -e "Doslo je do problema brisanje starog i kreiranje novog virtual env -a"
    rm -f ${ENV}
    virtualenv -p -python3 ${ENV}
fi

echo -e "\n Aktiviranje \n"
source ${ENV}/bin/activate

echo -e "\n Instaliranje potrebinih biblioteka! \n"
pip install -r ../${PROJECT_DIR}/requirements3.txt -U

echo -e "\n Pokretanje web servera! \n"

python3 ../${PROJECT_DIR}/api/main.py
