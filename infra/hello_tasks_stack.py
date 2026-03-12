from aws_cdk import (
    Stack,
    Tags,
    aws_lambda as _lambda,
    aws_apigatewayv2 as apigw,
    aws_apigatewayv2_integrations as integrations,
    aws_resourcegroups as rg,
)
from constructs import Construct
import os

# tag key used to group all resources
GROUP_TAG_KEY = "ResourceGroup"
GROUP_TAG_VALUE = "python-practice"

class HelloTasksStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        lambda_fn = _lambda.Function(
            self,
            "HelloTasksFn",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="handler.handler",
            # reference src directory relative to this file
            code=_lambda.Code.from_asset(
                os.path.join(os.path.dirname(__file__), "..", "src")
            ),
        )

        api = apigw.HttpApi(
            self,
            "HelloTasksApi",
            default_integration=integrations.HttpLambdaIntegration(
                "LambdaIntegration",
                lambda_fn
            )
        )

        self.api_url = api.api_endpoint

        # Tag every resource in this stack so they all appear in the resource group
        Tags.of(self).add(GROUP_TAG_KEY, GROUP_TAG_VALUE)

        # Tag-based resource group – collects all resources tagged with the key/value above
        rg.CfnGroup(
            self,
            "PythonPracticeResourceGroup",
            name="python-practice",
            description="All resources belonging to the python-practice project",
            resource_query=rg.CfnGroup.ResourceQueryProperty(
                type="TAG_FILTERS_1_0",
                query=rg.CfnGroup.QueryProperty(
                    tag_filters=[
                        rg.CfnGroup.TagFilterProperty(
                            key=GROUP_TAG_KEY,
                            values=[GROUP_TAG_VALUE],
                        )
                    ],
                ),
            ),
        )
