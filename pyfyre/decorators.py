from typing import Dict, Callable
from pyfyre.nodes import Node
from pyfyre.states import State

class OnMountWatcher:
    _mounts: Dict[str, Callable[..., Node]] = {}
    _mounted: str = None

    @staticmethod
    def subscribe(component_id: str = None, func: Callable[..., Node] = None) -> None:
        OnMountWatcher._mounts[component_id] = func

    @staticmethod
    def mount(component_id: str):
        if not component_id in OnMountWatcher._mounts:
            return
            
        OnMountWatcher._mounts[component_id]()
        OnMountWatcher._mounted = component_id


def on_mount(component_id: str):
    
    def factory(func: Callable[..., Node] = None):

        def wrapper():
            OnMountWatcher.subscribe(component_id, func)

        return wrapper()

    return factory


def create_effect(deps: list[State]):
    
    def factory(func: Callable[..., Node] = None):

        def wrapper():
            
            for dep in deps:
                if isinstance(dep, State):
                    dep.add_listener(func)

        return wrapper()

    return factory
