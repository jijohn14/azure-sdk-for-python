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


class Filters(Model):
    """May be used to filter budgets by resource group, resource, or meter.

    :param resource_groups: The list of filters on resource groups, allowed at
     subscription level only.
    :type resource_groups: list[str]
    :param resources: The list of filters on resources.
    :type resources: list[str]
    :param meters: The list of filters on meters, mandatory for budgets of
     usage category.
    :type meters: list[str]
    :param tags: The dictionary of filters on tags.
    :type tags: dict[str, list[str]]
    """

    _validation = {
        'resource_groups': {'max_items': 10, 'min_items': 0},
        'resources': {'max_items': 10, 'min_items': 0},
        'meters': {'max_items': 10, 'min_items': 0},
    }

    _attribute_map = {
        'resource_groups': {'key': 'resourceGroups', 'type': '[str]'},
        'resources': {'key': 'resources', 'type': '[str]'},
        'meters': {'key': 'meters', 'type': '[str]'},
        'tags': {'key': 'tags', 'type': '{[str]}'},
    }

    def __init__(self, resource_groups=None, resources=None, meters=None, tags=None):
        super(Filters, self).__init__()
        self.resource_groups = resource_groups
        self.resources = resources
        self.meters = meters
        self.tags = tags
