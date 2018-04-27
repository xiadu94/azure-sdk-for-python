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


class RollbackStatusInfo(Model):
    """Information about rollback on failed VM instances after a OS Upgrade
    operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar successfully_rolledback_instance_count: The number of instances
     which have been successfully rolled back.
    :vartype successfully_rolledback_instance_count: int
    :ivar failed_rolledback_instance_count: The number of instances which
     failed to rollback.
    :vartype failed_rolledback_instance_count: int
    :ivar rollback_error: Error Details if OS rollback failed.
    :vartype rollback_error: ~azure.mgmt.compute.v2017_12_01.models.ApiError
    """

    _validation = {
        'successfully_rolledback_instance_count': {'readonly': True},
        'failed_rolledback_instance_count': {'readonly': True},
        'rollback_error': {'readonly': True},
    }

    _attribute_map = {
        'successfully_rolledback_instance_count': {'key': 'successfullyRolledbackInstanceCount', 'type': 'int'},
        'failed_rolledback_instance_count': {'key': 'failedRolledbackInstanceCount', 'type': 'int'},
        'rollback_error': {'key': 'rollbackError', 'type': 'ApiError'},
    }

    def __init__(self, **kwargs) -> None:
        super(RollbackStatusInfo, self).__init__(**kwargs)
        self.successfully_rolledback_instance_count = None
        self.failed_rolledback_instance_count = None
        self.rollback_error = None
