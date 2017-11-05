# coding: utf-8
import colorlog
import logging
ch = logging.StreamHandler()
cf = colorlog.ColorFormatter()
ch.setFormatter(cf)
log = logging.getLogger()
log.addHandler(ch)
log.setLevel(logging.DEBUG)
log.warning('test warning message')
