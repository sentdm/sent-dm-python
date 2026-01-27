from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `sent_dm.resources` module.

    This is used so that we can lazily import `sent_dm.resources` only when
    needed *and* so that users can just import `sent_dm` and reference `sent_dm.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("sent_dm.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
