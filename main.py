#!/usr/bin/env python

# Standard Library
from logging import DEBUG, getLogger
from logging.config import fileConfig

# Current project
from cli_args import get_args

args = get_args()

fileConfig("log.ini")

log = getLogger(__name__)

if args.debug:
    log.setLevel(DEBUG)

log.info("hello")
log.debug("world")
