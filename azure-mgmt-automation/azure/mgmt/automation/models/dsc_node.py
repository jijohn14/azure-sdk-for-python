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


class DscNode(ProxyResource):
    """Definition of a DscNode.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param last_seen: Gets or sets the last seen time of the node.
    :type last_seen: datetime
    :param registration_time: Gets or sets the registration time of the node.
    :type registration_time: datetime
    :param ip: Gets or sets the ip of the node.
    :type ip: str
    :param account_id: Gets or sets the account id of the node.
    :type account_id: str
    :param node_configuration: Gets or sets the configuration of the node.
    :type node_configuration:
     ~azure.mgmt.automation.models.DscNodeConfigurationAssociationProperty
    :param status: Gets or sets the status of the node.
    :type status: str
    :param node_id: Gets or sets the node id.
    :type node_id: str
    :param etag: Gets or sets the etag of the resource.
    :type etag: str
    :param extension_handler: Gets or sets the list of extensionHandler
     properties for a Node.
    :type extension_handler:
     list[~azure.mgmt.automation.models.DscNodeExtensionHandlerAssociationProperty]
    :param last_seen1: Gets or sets the last seen time of the node.
    :type last_seen1: datetime
    :param registration_time1: Gets or sets the registration time of the node.
    :type registration_time1: datetime
    :param ip1: Gets or sets the ip of the node.
    :type ip1: str
    :param account_id1: Gets or sets the account id of the node.
    :type account_id1: str
    :param node_configuration1: Gets or sets the configuration of the node.
    :type node_configuration1:
     ~azure.mgmt.automation.models.DscNodeConfigurationAssociationProperty
    :param status1: Gets or sets the status of the node.
    :type status1: str
    :param node_id1: Gets or sets the node id.
    :type node_id1: str
    :param etag1: Gets or sets the etag of the resource.
    :type etag1: str
    :param extension_handler1: Gets or sets the list of extensionHandler
     properties for a Node.
    :type extension_handler1:
     list[~azure.mgmt.automation.models.DscNodeExtensionHandlerAssociationProperty]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'last_seen': {'key': 'lastSeen', 'type': 'iso-8601'},
        'registration_time': {'key': 'registrationTime', 'type': 'iso-8601'},
        'ip': {'key': 'ip', 'type': 'str'},
        'account_id': {'key': 'accountId', 'type': 'str'},
        'node_configuration': {'key': 'nodeConfiguration', 'type': 'DscNodeConfigurationAssociationProperty'},
        'status': {'key': 'status', 'type': 'str'},
        'node_id': {'key': 'nodeId', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'extension_handler': {'key': 'extensionHandler', 'type': '[DscNodeExtensionHandlerAssociationProperty]'},
        'last_seen1': {'key': 'properties.lastSeen', 'type': 'iso-8601'},
        'registration_time1': {'key': 'properties.registrationTime', 'type': 'iso-8601'},
        'ip1': {'key': 'properties.ip', 'type': 'str'},
        'account_id1': {'key': 'properties.accountId', 'type': 'str'},
        'node_configuration1': {'key': 'properties.nodeConfiguration', 'type': 'DscNodeConfigurationAssociationProperty'},
        'status1': {'key': 'properties.status', 'type': 'str'},
        'node_id1': {'key': 'properties.nodeId', 'type': 'str'},
        'etag1': {'key': 'properties.etag', 'type': 'str'},
        'extension_handler1': {'key': 'properties.extensionHandler', 'type': '[DscNodeExtensionHandlerAssociationProperty]'},
    }

    def __init__(self, last_seen=None, registration_time=None, ip=None, account_id=None, node_configuration=None, status=None, node_id=None, etag=None, extension_handler=None, last_seen1=None, registration_time1=None, ip1=None, account_id1=None, node_configuration1=None, status1=None, node_id1=None, etag1=None, extension_handler1=None):
        super(DscNode, self).__init__()
        self.last_seen = last_seen
        self.registration_time = registration_time
        self.ip = ip
        self.account_id = account_id
        self.node_configuration = node_configuration
        self.status = status
        self.node_id = node_id
        self.etag = etag
        self.extension_handler = extension_handler
        self.last_seen1 = last_seen1
        self.registration_time1 = registration_time1
        self.ip1 = ip1
        self.account_id1 = account_id1
        self.node_configuration1 = node_configuration1
        self.status1 = status1
        self.node_id1 = node_id1
        self.etag1 = etag1
        self.extension_handler1 = extension_handler1
