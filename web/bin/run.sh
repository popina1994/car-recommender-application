#!/bin/bash

BIN_DIR=$(dirname $0)
PROJ_DIR="${BIN_DIR}/../.."
echo -e $BIN_DIR
echo -e $PROJ_DIR
ENV="${BIN_DIR}/../env"

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
pip install -r ${BIN_DIR}/../requirements3.txt -U


export PYTHONPATH="$PYTHONPATH:/home/popina/six-pack/"
cd $PROJ_DIR
python3 ./web/api/main.py
