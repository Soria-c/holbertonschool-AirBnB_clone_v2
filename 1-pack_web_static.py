#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
"""Implements a fabric script"""


def do_pack():
    """Script to compress a folder locally"""
    d = datetime.now()
    local('mkdir -p versions')
    file_name = "web_static_{}{}{}{}{}{}.tgz"\
                .format(d.year, d.month, d.day, d.hour, d.minute, d.second)
    local('tar -czvf versions/{} web_static'.format(file_name))

    return file_name
