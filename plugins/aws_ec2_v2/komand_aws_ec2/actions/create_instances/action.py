import komand
from .schema import CreateInstancesInput, CreateInstancesOutput

# Custom imports below
from komand_aws_ec2.util.common import AWSAction, PaginationHelper


class CreateInstances(AWSAction):
    def __init__(self):
        super().__init__(
            name="create_instances",
            description="Create an instances",
            input=CreateInstancesInput(),
            output=CreateInstancesOutput(),
            aws_service="ec2",
            aws_command="create_instances",
            pagination_helper=PaginationHelper(
                input_token=["next_token"],
                output_token=["next_token"],
                result_key=["Reservations"],
                limit_key="max_results",
            ),
        )
