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


class ConnectionResetSharedKey(Model):
    """The virtual network connection reset shared key.

    All required parameters must be populated in order to send to Azure.

    :param key_length: Required. The virtual network connection reset shared
     key length, should between 1 and 128.
    :type key_length: int
    """

    _validation = {
        'key_length': {'required': True, 'maximum': 128, 'minimum': 1},
    }

    _attribute_map = {
        'key_length': {'key': 'keyLength', 'type': 'int'},
    }

    def __init__(self, *, key_length: int, **kwargs) -> None:
        super(ConnectionResetSharedKey, self).__init__(**kwargs)
        self.key_length = key_length
