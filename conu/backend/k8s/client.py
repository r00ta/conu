# -*- coding: utf-8 -*-
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
singleton instances of kubernetes client
"""

from kubernetes import client, config
from kubernetes.client.api_client import ApiClient


core_api = None
apps_api = None


def get_core_api():
    """
    Create instance of Core V1 API of kubernetes:
    https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md
    :return: instance of client
    """
    global core_api

    if core_api is None:
        api_client = ApiClient(header_name="Authorization",
                               header_value="Bearer luqIZzSJ8RT33yIi_lo3aNRZlA34wfftYTR0r9zRtw4")
        config.load_kube_config()
        core_api = client.CoreV1Api(api_client=api_client)

    return core_api


def get_apps_api():
    """
    Create instance of Apps V1 API of kubernetes:
    https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/AppsV1Api.md
    :return: instance of client
    """
    global apps_api

    if apps_api is None:
        config.load_kube_config()
        apps_api = client.AppsV1Api()

    return apps_api
