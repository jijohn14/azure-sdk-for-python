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


class ManagementGroup(Model):
    """A management group that is connected to a workspace.

    :param server_count: The number of servers connected to the management
     group.
    :type server_count: int
    :param is_gateway: Gets or sets a value indicating whether the management
     group is a gateway.
    :type is_gateway: bool
    :param name: The name of the management group.
    :type name: str
    :param id: The unique ID of the management group.
    :type id: str
    :param created: The datetime that the management group was created.
    :type created: datetime
    :param data_received: The last datetime that the management group received
     data.
    :type data_received: datetime
    :param version: The version of System Center that is managing the
     management group.
    :type version: str
    :param sku: The SKU of System Center that is managing the management
     group.
    :type sku: str
    """

    _attribute_map = {
        'server_count': {'key': 'properties.serverCount', 'type': 'int'},
        'is_gateway': {'key': 'properties.isGateway', 'type': 'bool'},
        'name': {'key': 'properties.name', 'type': 'str'},
        'id': {'key': 'properties.id', 'type': 'str'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'data_received': {'key': 'properties.dataReceived', 'type': 'iso-8601'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'str'},
    }

    def __init__(self, server_count=None, is_gateway=None, name=None, id=None, created=None, data_received=None, version=None, sku=None):
        self.server_count = server_count
        self.is_gateway = is_gateway
        self.name = name
        self.id = id
        self.created = created
        self.data_received = data_received
        self.version = version
        self.sku = sku