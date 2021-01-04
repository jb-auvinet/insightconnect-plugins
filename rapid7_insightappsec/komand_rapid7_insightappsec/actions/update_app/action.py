import insightconnect_plugin_runtime
from .schema import UpdateAppInput, UpdateAppOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Apps
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper

class UpdateApp(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_app',
                description=Component.DESCRIPTION,
                input=UpdateAppInput(),
                output=UpdateAppOutput())

    def run(self, params={}):
        # TODO: Implement run function
        app_id = params.get(Input.APP_ID)
        app_name = params.get(Input.APP_NAME)
        app_description = params.get(Input.APP_DESCRIPTION)
        request = ResourceHelper(self.connection.session, self.logger)

        url = Apps.update_app(self.connection.url,app_id)
        payload = {'name': app_name, 'description': app_description}

        response = request.resource_request(url, 'put', payload=payload)

        return {Output.STATUS: response['status']}
