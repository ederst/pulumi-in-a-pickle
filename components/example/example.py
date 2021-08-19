from typing import Optional

import pulumi

import providers.example as example


class ExampleComponent(pulumi.ComponentResource):
    def __init__(
        self,
        name: str,
        example_name: str,
        opts: Optional[pulumi.ResourceOptions] = pulumi.ResourceOptions(),
    ):
        super().__init__(
            "tis:an:Example",
            name=name,
            props=None,
            opts=opts,
        )

        base_opts = pulumi.ResourceOptions(parent=self)

        example.Example(
            f"{name}-example",
            config=example.ExampleArgs(
                name=example_name,
            ),
            opts=base_opts,
        )
