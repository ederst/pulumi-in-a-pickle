# from abc import ABCMeta, abstractmethod
from typing import Any, Dict

import pulumi
import pulumi.dynamic as dynamic


class BaseProvider(dynamic.ResourceProvider):  # , metaclass=ABCMeta):
    _base_var = 'base value'

    # @abstractmethod
    @classmethod
    def on_create(self, inputs: Any) -> (str, Dict[str, Any]):
        raise NotImplementedError

    def create(self, inputs: Any) -> dynamic.CreateResult:
        pulumi.log.debug(f"{type(self).__name__}.create()")
        id, outputs = self.on_create(inputs)
        pulumi.log.warn(f'imma need the value of self._base_var: "{self._base_var}"')
        return dynamic.CreateResult(id, outs=outputs)


class BaseResourceProvider(BaseProvider):  # , metaclass=ABCMeta):
    _base_resource_var = 'base resource value'

    # @abstractmethod
    @classmethod
    def ensure_config(self, inputs: Any) -> (Any, str):
        raise NotImplementedError

    def on_create(self, inputs: Any) -> (str, Dict[str, Any]):
        pulumi.log.debug(f"{type(self).__name__}.on_create()")
        outputs, config = self.ensure_config(inputs)

        pulumi.log.warn(f'imma need the value of self._base_resource_var: "{self._base_resource_var}"')

        outputs.update({'config': config})
        return 'exampleID', outputs
