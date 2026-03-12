#!/usr/bin/env python3
import aws_cdk as cdk
from hello_tasks_stack import HelloTasksStack
import json
import os

app = cdk.App()

# determine which environment to deploy; priority: context value, ENV var, default to dev
env_name = app.node.try_get_context("env") or os.environ.get("CDK_ENV", "dev")
env_name = env_name.lower()

# load configuration JSON for the selected environment
config_file = os.path.join(os.path.dirname(__file__), f"config_{env_name}.json")
if not os.path.exists(config_file):
    raise RuntimeError(f"Configuration file for environment '{env_name}' not found: {config_file}")

with open(config_file) as f:
    cfg = json.load(f)

# debug output
print(f"Loading config file: {config_file}, contents: {cfg}")

env = cdk.Environment(account=cfg["account"], region=cfg["region"])
stack_suffix = cfg.get("stack_suffix", env_name.capitalize())

# create a single stack for the chosen environment
HelloTasksStack(app, f"HelloTasksStack-{stack_suffix}", env=env)

app.synth()