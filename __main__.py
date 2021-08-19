"""A Python Pulumi program"""

import components.example as example

example.ExampleComponent(
    "some example",
    example_name="some example",
)
