# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_resource import ProxyResource


class ApplicationTypeVersionResource(ProxyResource):
    """An application type version resource for the specified application type
    name resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource identifier.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Azure resource location.
    :type location: str
    :ivar provisioning_state: The current deployment or provisioning state,
     which only appears in the response
    :vartype provisioning_state: str
    :param app_package_url: The URL to the application package
    :type app_package_url: str
    :ivar default_parameter_list: List of application type parameters that can
     be overridden when creating or updating the application.
    :vartype default_parameter_list: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'app_package_url': {'required': True},
        'default_parameter_list': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'app_package_url': {'key': 'properties.appPackageUrl', 'type': 'str'},
        'default_parameter_list': {'key': 'properties.defaultParameterList', 'type': '{str}'},
    }

    def __init__(self, app_package_url, location=None):
        super(ApplicationTypeVersionResource, self).__init__(location=location)
        self.provisioning_state = None
        self.app_package_url = app_package_url
        self.default_parameter_list = None