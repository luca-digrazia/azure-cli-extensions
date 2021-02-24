# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_healthbot_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_healthbot.vendored_sdks.healthbot import HealthbotClient
    return get_mgmt_service_client(cli_ctx,
                                   HealthbotClient)


def cf_bot(cli_ctx, *_):
    return cf_healthbot_cl(cli_ctx).bots