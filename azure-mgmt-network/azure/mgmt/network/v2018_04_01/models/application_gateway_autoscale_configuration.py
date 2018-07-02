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


class ApplicationGatewayAutoscaleConfiguration(Model):
    """Application Gateway autoscale configuration.

    All required parameters must be populated in order to send to Azure.

    :param bounds: Required. Autoscale bounds
    :type bounds:
     ~azure.mgmt.network.v2018_04_01.models.ApplicationGatewayAutoscaleBounds
    """

    _validation = {
        'bounds': {'required': True},
    }

    _attribute_map = {
        'bounds': {'key': 'bounds', 'type': 'ApplicationGatewayAutoscaleBounds'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGatewayAutoscaleConfiguration, self).__init__(**kwargs)
        self.bounds = kwargs.get('bounds', None)
