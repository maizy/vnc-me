# VNC-me

Запуск удалённого vnc клиента из web интерфейса.

Полезно для офисных демонстраций на проекторах или больших экранах.

## Требования

* python 3.2+
* tornado 3.1+
* pytils
* xtightvncviewer
* virtualenv
* протестировано только на Ubuntu 12.04 LTS

## Установка

* `sudo apt-get install python3.2 xtightvncviewer python-virtualenv`
* `git clone https://github.com/maizy/vnc-me.git`
* `virtualenv --python /usr/bin/python3.2 vnc-me/venv`
* `. vnc-me/venv/bin/activate`
* `pip install -r vnc-me/requirements.txt`

## Запуск

* `. vnc-me/venv/bin/activate`
* `vnc-me/bin/run_server.py`
 * для большего количества опций `vnc-me/bin/run_server.py --help`
 * для использования конфига `cp vnc-me/etc/vnc-me.conf.ex vnc-me/etc/vnc-me.conf`,
   `nano vnc-me/etc/vnc-me.conf`. Опции аналогичны тем, что доступны через `--help`.
