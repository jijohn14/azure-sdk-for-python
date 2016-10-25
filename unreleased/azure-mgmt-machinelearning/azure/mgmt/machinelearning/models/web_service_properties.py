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


class WebServiceProperties(Model):
    """The set of properties specific to the Azure ML web service resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param title: The title of the Azure ML web service.
    :type title: str
    :param description: The description of the Azure ML web service.
    :type description: str
    :ivar created_on: The moment of time the Azure ML web service was created.
    :vartype created_on: datetime
    :ivar modified_on: The moment of time the web service was last modified.
    :vartype modified_on: datetime
    :ivar provisioning_state: The web service resource's provisioning state.
     Possible values include: 'Unknown', 'Provisioning', 'Succeeded',
     'Failed', 'Canceled'
    :vartype provisioning_state: str or :class:`ProvisioningState
     <azure.mgmt.machinelearning.models.ProvisioningState>`
    :param keys: The set of access keys for the web service. If not specified
     at creation time (PUT), they will be generated automatically by the
     resource provider.
    :type keys: :class:`WebServiceKeys
     <azure.mgmt.machinelearning.models.WebServiceKeys>`
    :param read_only: If true, the web service can no longer be updated /
     patched, only removed. Otherwise, the service resource supports changes.
    :type read_only: bool
    :ivar swagger_location: The uri for the swagger spec associated with this
     web service.
    :vartype swagger_location: str
    :param expose_sample_data: Flag that controls whether to expose sample
     data or not in the web service's swagger definition.
    :type expose_sample_data: bool
    :param realtime_configuration: Configuration for the service's realtime
     endpoint.
    :type realtime_configuration: :class:`RealtimeConfiguration
     <azure.mgmt.machinelearning.models.RealtimeConfiguration>`
    :param diagnostics: Settings controlling the diagnostics traces
     collection for the web service.
    :type diagnostics: :class:`DiagnosticsConfiguration
     <azure.mgmt.machinelearning.models.DiagnosticsConfiguration>`
    :param storage_account: The storage account associated with the service.
     This is used to store both datasets and diagnostic traces. This
     information is required at creation time (PUT) and only the key is
     updateable after that. The account credentials are hidden on a GET web
     service call.
    :type storage_account: :class:`StorageAccount
     <azure.mgmt.machinelearning.models.StorageAccount>`
    :param machine_learning_workspace: This is only populated at creation
     time (PUT) for web services originating from an AzureML Studio
     experiment.
    :type machine_learning_workspace: :class:`MachineLearningWorkspace
     <azure.mgmt.machinelearning.models.MachineLearningWorkspace>`
    :param commitment_plan: The commitment plan associated with this web
     service. This is required to be specified at creation time (PUT) and is
     not updateable afterwards.
    :type commitment_plan: :class:`CommitmentPlan
     <azure.mgmt.machinelearning.models.CommitmentPlan>`
    :param input: Swagger schema for the service's input(s), as applicable.
    :type input: :class:`ServiceInputOutputSpecification
     <azure.mgmt.machinelearning.models.ServiceInputOutputSpecification>`
    :param output: Swagger schema for the service's output(s), as applicable.
    :type output: :class:`ServiceInputOutputSpecification
     <azure.mgmt.machinelearning.models.ServiceInputOutputSpecification>`
    :param example_request: Sample request data for each of the service's
     inputs, as applicable.
    :type example_request: :class:`ExampleRequest
     <azure.mgmt.machinelearning.models.ExampleRequest>`
    :param assets: Set of assets associated with the web service.
    :type assets: dict
    :param parameters: The set of global parameters values defined for the
     web service, given as a global parameter name to default value map. If
     no default value is specified, the parameter is considered to be
     required.
    :type parameters: dict
    :param packageType: Polymorphic Discriminator
    :type packageType: str
    """ 

    _validation = {
        'created_on': {'readonly': True},
        'modified_on': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'swagger_location': {'readonly': True},
        'packageType': {'required': True},
    }

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'keys': {'key': 'keys', 'type': 'WebServiceKeys'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'swagger_location': {'key': 'swaggerLocation', 'type': 'str'},
        'expose_sample_data': {'key': 'exposeSampleData', 'type': 'bool'},
        'realtime_configuration': {'key': 'realtimeConfiguration', 'type': 'RealtimeConfiguration'},
        'diagnostics': {'key': 'diagnostics', 'type': 'DiagnosticsConfiguration'},
        'storage_account': {'key': 'storageAccount', 'type': 'StorageAccount'},
        'machine_learning_workspace': {'key': 'machineLearningWorkspace', 'type': 'MachineLearningWorkspace'},
        'commitment_plan': {'key': 'commitmentPlan', 'type': 'CommitmentPlan'},
        'input': {'key': 'input', 'type': 'ServiceInputOutputSpecification'},
        'output': {'key': 'output', 'type': 'ServiceInputOutputSpecification'},
        'example_request': {'key': 'exampleRequest', 'type': 'ExampleRequest'},
        'assets': {'key': 'assets', 'type': '{AssetItem}'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'packageType': {'key': 'packageType', 'type': 'str'},
    }

    _subtype_map = {
        'packageType': {'Graph': 'WebServicePropertiesForGraph'}
    }

    def __init__(self, title=None, description=None, keys=None, read_only=None, expose_sample_data=None, realtime_configuration=None, diagnostics=None, storage_account=None, machine_learning_workspace=None, commitment_plan=None, input=None, output=None, example_request=None, assets=None, parameters=None):
        self.title = title
        self.description = description
        self.created_on = None
        self.modified_on = None
        self.provisioning_state = None
        self.keys = keys
        self.read_only = read_only
        self.swagger_location = None
        self.expose_sample_data = expose_sample_data
        self.realtime_configuration = realtime_configuration
        self.diagnostics = diagnostics
        self.storage_account = storage_account
        self.machine_learning_workspace = machine_learning_workspace
        self.commitment_plan = commitment_plan
        self.input = input
        self.output = output
        self.example_request = example_request
        self.assets = assets
        self.parameters = parameters
        self.packageType = None