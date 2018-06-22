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

from msrest.serialization import Model


class ClusterMonitoringRequest(Model):
    """The Operations Management Suite (OMS) parameters.

    :param workspace_id: The Operations Management Suite (OMS) workspace ID.
    :type workspace_id: str
    :param primary_key: The Operations Management Suite (OMS) workspace key.
    :type primary_key: str
    """

    _attribute_map = {
        'workspace_id': {'key': 'workspaceId', 'type': 'str'},
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
    }

    def __init__(self, workspace_id=None, primary_key=None):
        super(ClusterMonitoringRequest, self).__init__()
        self.workspace_id = workspace_id
        self.primary_key = primary_key