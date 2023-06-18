from typing import Any, Optional

import pulumi
import pulumi.dynamic as dynamic

from .base import BaseResourceProvider


class ExampleArgs(object):
    def __init__(self, name: str):
        self.name = name


class ExampleProvider(BaseResourceProvider):
    def __init__(self):
        # super().__init__()
        self._example_config = None

    def ensure_config(self, inputs: Any) -> (Any, str):
        self._example_config = inputs["config"]["name"]
        return inputs, f'name: {self._example_config}'


class Example(dynamic.Resource):
    def __init__(
        self,
        name: str,
        config: ExampleArgs,
        opts: Optional[pulumi.ResourceOptions] = None,
    ):
        self.config = config

        super().__init__(
            ExampleProvider(),
            name,
            {
                "config": {**vars(config)},
            },
            opts,
        )
