#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers"""
from fabric.api import *
from os import path


env.hosts = ['34.73.71.111', '3.91.201.53']


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
