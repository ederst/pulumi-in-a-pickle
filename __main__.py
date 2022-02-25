"""A Python Pulumi program showing that pulumi.export() will not allow the same instances/objects twice"""

from copy import deepcopy
import pulumi


class SomeClass:
    def __init__(self, some_member) -> None:
        self.some_member = some_member


my_obj = SomeClass("some value")
my_list = ["1", "2", my_obj]

# This will show the whole list (as expected)
pulumi.export("expected_output", {"key": my_list})

# This will show "actual_whole_list_gone.key == null" in "pulumi stack output"
pulumi.export("actual_whole_list_gone", {"key": my_list})

# This will show "actual_obj_gone.key == [1, 2, null]"
pulumi.export("actual_obj_gone", {"key": my_list.copy()})

# This will show the whole list again
pulumi.export(
    "actual_whole_list_with_deepcopy", {"key": deepcopy(my_list)}
)
