#!/usr/bin/python3
"""Fabric script that generates .tgz archive from web_static folder"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates .tgz archive from web_static"""
    local("mkdir versions")
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(time_now)
    if local("tar -czvf {} web_static/".format(path)).succeeded:
        return path
    else:
        return None
