#!/usr/bin/python3
from fabric.api import local, run, put, env
from datetime import datetime
from os.path import exists
"""Implements fabric scripts"""


env.hosts = ['18.212.96.209', '54.91.216.10']
env.user = 'ubuntu'


def do_pack():
    """Script to compress a folder locally"""
    d = datetime.now()
    local('mkdir -p versions')
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz"\
                .format(d.year, d.month, d.day, d.hour, d.minute, d.second)
    local('tar -czvf {} web_static'.format(file_name))

    return file_name


def do_deploy(archive_path):
    """Script to send files to deploy servers an arrange them"""
    if not(exists(archive_path)):
        return False
    file_name = archive_path.split('/')[-1]
    new_name = file_name.strip('.tgz')
    dir_name = "/data/web_static/releases/" + new_name

    put(archive_path, '/tmp')
    run('mkdir -p {}'.format(dir_name))
    run('tar -zvxf /tmp/{} -C {}'.format(file_name, dir_name))
    run('sudo rm /tmp/{}'.format(file_name))
    run('rm /data/web_static/current')
    run('ln -sf {} /data/web_static/current'.format(dir_name))
    run('mv {}/web_static/* {}'.format(dir_name, dir_name))
    run('rm -r {}/web_static/'.format(dir_name))
    return True


def deploy():
    """Script to execute the complete deploy to the servers"""
    file_name = do_pack()
    print(file_name)
    if (file_name):
        return do_deploy(file_name)
    return False
