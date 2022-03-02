# pulumi-no-doubles-stack-output

This demonstrates that Pulumi (at least the Python SDK) does not allow the same class instance/object twice in stack output.

Issue: TBD

## Pulumi version

```shell
❯ pulumi version
v3.25.0

❯ .venv/bin/pip list | grep pulumi
pulumi            3.25.0
```

Also reproduced with `v3.24.1`.

## How to reproduce

```shell
p up --yes
p stack output --json
```

### Expected

Every output should (probably) be like like the `expected_output`.

```json
  "expected_output": {
    "key": [
      "1",
      "2",
      {
        "some_member": "some value"
      }
    ]
  }
```

### Actual

Same class instances/objects are not showing up.

```json
{
  "expected_output": {
    "key": [
      "1",
      "2",
      {
        "some_member": "some value"
      }
    ]
  },
  "actual_obj_gone": {
    "key": [
      "1",
      "2",
      null
    ]
  },
  "actual_whole_list_gone": {
    "key": null
  },
  "actual_whole_list_with_deepcopy": {
    "key": [
      "1",
      "2",
      {
        "some_member": "some value"
      }
    ]
  }
}
```
