#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['34.73.71.111', '3.91.201.53']


def do_pack():
    """generates .tgz archive from web_static"""
    local("mkdir versions")
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(time_now)
    if local("tar -czvf {} web_static/".format(path)).succeeded:
        return path
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to web servers"""
    if not path.exists(archive_path):
        return False
    put(archive_path, "/tmp/")
    name = archive_path.split('/')[-1][:-4]
    run("mkdir -p /data/web_static/releases/{}".format(name))
    run("tar -xzf /tmp/{}.tgz -C ".format(name) +
        "/data/web_static/releases/{}/".format(name))
    run("rm /tmp/{}.tgz".format(name))
    run("mv /data/web_static/releases/{}/web_static/* ".format(name) +
        "/data/web_static/releases/{}/".format(name))
    run("rm -rf /data/web_static/releases/{}/web_static".format(name))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ ".format(name) +
        "/data/web_static/current")
    return True


def deploy():
    """creates and distributes an archive to web servers"""
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
