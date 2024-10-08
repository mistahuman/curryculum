#! /bin/sh
## sudo apt install texlive texlive-latex-extra texlive-lang-italian

python3 -m venv venv --without-pip
. ./venv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
python3 /tmp/get-pip.py
# install webserver fastapi jinja2
pip install fastapi uvicorn[standard] Jinja2
deactivate

cd ui
npm i 
npm run build
cd -
