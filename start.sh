#!/bin/bash
source venv/bin/activate
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
python3 manage.py runserver 0.0.0.0:9001