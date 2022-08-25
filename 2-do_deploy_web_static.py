#!/usr/bin/python3
from fabric.api import run, put, env
from os.path import exists
"""Implements a fabric script"""

env.hosts = ['18.212.96.209', '54.91.216.10']
env.user = 'ubuntu'


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
    print('New version deployed!')
    return True
