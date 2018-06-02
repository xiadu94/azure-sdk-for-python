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


class GalleryDiskImage(Model):
    """This is the disk image base class.

    :param sized_in_gb: It indicates the size of the VHD to create.
    :type sized_in_gb: int
    :param host_caching: The host caching of the disk. Valid values are
     'None', 'ReadOnly', and 'ReadWrite'. Possible values include: 'None',
     'ReadOnly', 'ReadWrite'
    :type host_caching: str or
     ~azure.mgmt.compute.v2018_06_01.models.HostCaching
    """

    _attribute_map = {
        'sized_in_gb': {'key': 'sizedInGB', 'type': 'int'},
        'host_caching': {'key': 'hostCaching', 'type': 'HostCaching'},
    }

    def __init__(self, *, sized_in_gb: int=None, host_caching=None, **kwargs) -> None:
        super(GalleryDiskImage, self).__init__(**kwargs)
        self.sized_in_gb = sized_in_gb
        self.host_caching = host_caching