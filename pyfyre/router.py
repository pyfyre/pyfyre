from settings import ROUTES
from typing import Any, Dict, Callable, Optional
from browser import document, window, DOMEvent
from pyfyre.events import window_event_listener
from pyfyre.nodes import Node, Element, TextNode


class RouteManager:
    """A static class that enables navigation between various views in a PyFyre application."""

    _current_route: str
    _routes_builder: Dict[str, Callable[..., Node]] = {}
    _routes: Dict[str, Optional[Node]] = {}
    _root_node = document.select_one("#root")

    @staticmethod
    def initialize(routes: Dict[str, Callable[..., Node]]) -> None:
        """:meta private:"""
        RouteManager._current_route = RouteManager.parse_route(window.location.href)
        RouteManager._routes_builder = routes

        @window_event_listener("popstate")
        def onpopstate(event: DOMEvent) -> None:
            RouteManager.change_route(window.location.href)

    @staticmethod
    def parse_route(route_name: str) -> str:
        """Parse the ``route_name`` to turn it into a valid route name.

        Examples:
            | ``home`` -> ``/home``
            | ``contact/`` -> ``/contact``
            | ``about/this`` -> ``/about/this``
            | ``https://pyfyre.app/`` -> ``/``
            | ``https://pyfyre.app/about`` -> ``/about``
        """

        el = document.createElement("a")
        el.href = route_name
        route_name = str(el.pathname)

        if route_name == "/":
            return route_name

        return str(el.pathname).rstrip("/")

    @staticmethod
    def get_node(
        route_name: str,
        *,
        arg: Any = None,
        force_build: bool = False,
        parse_route: bool = True,
    ) -> Optional[Node]:
        """Call the corresponding route builder of the ``route_name``
        and return its ``Node``.

        Args:
            arg: The argument that will be passed in to the route builder.
            force_build: Whether to call the route builder even if it is already called before.
                By default, called route builders are cached.
            parse_route: Whether to call the
                ``RouteManager.parse_route`` method on the ``route_name``.

        Returns:
            The returned ``Node`` of the corresponding route builder of the ``route_name``.
            If the route doesn't exist, the default will be returned
            which has a 404 message.
        """

        if parse_route:
            route_name = RouteManager.parse_route(route_name)

        node = RouteManager._routes.get(route_name)

        if force_build or node is None:
            route_builder = RouteManager._routes_builder.get(route_name)

            if route_builder is not None:
                try:
                    node = route_builder(arg)
                except TypeError:
                    node = route_builder()
            else:
                node = None

            RouteManager._routes[route_name] = node

            if isinstance(node, Element):
                node.build_children()

        return node

    @staticmethod
    def render_route(
        route_name: str, *, arg: Any = None, force_build: bool = False
    ) -> None:
        """:meta private:"""
        node = RouteManager.get_node(
            route_name, arg=arg, force_build=force_build
        ) or TextNode("No route to render.")
        RouteManager._root_node.clear()
        RouteManager._root_node.attach(node.dom)

    @staticmethod
    def _update_page(
        route_data: Dict[str, Any], prev_route_data: Dict[str, Any]
    ) -> bool:
        if (route_data.get("head") or []) != (prev_route_data.get("head") or []):
            return False

        document.title = route_data.get("title")

        icon = document.select_one("link[rel~='icon']")
        if icon is not None:
            icon.href = route_data.get("icon")

        return True

    @staticmethod
    def change_route(
        route_name: str, *, arg: Any = None, force_build: bool = False
    ) -> None:
        """:meta private:"""
        prev_route = RouteManager._current_route

        if ROUTES.get(prev_route) is None:
            window.location.reload()
        else:
            route_name = RouteManager.parse_route(route_name)
            RouteManager._current_route = route_name
            route_data = ROUTES.get(route_name)

            if route_data is None:
                window.location.reload()
            else:
                has_same_head = RouteManager._update_page(
                    route_data, ROUTES[prev_route]
                )
                if has_same_head:
                    RouteManager.render_route(
                        route_name, arg=arg, force_build=force_build
                    )
                else:
                    window.location.reload()
