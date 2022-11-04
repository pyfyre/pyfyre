import sys
from pyfyre.styles import Style
from pyfyre.states import State
from browser import timer
from browser import DOMEvent
from pyfyre.nodes import Node, Element
from typing import Optional, Dict, List, Callable, Any


class ListBuilder(Element):
    """A scrollable list of nodes that are created on demand.

    This element is appropriate for lists with a large (or infinite) number of children
    because the builder is called only for those children that are actually visible.

    Args:
        item_builder: Builder for a child of this list.
            Called only with indices greater than or equal to zero and less than ``count``.
            None can be returned in the builder to skip the current index.
        count: Number of times this list will attempt to build a child.
            If None, infinite attempts will be made.
        max_height: Maximum height of this element.
            A ``max-height`` CSS property is required to make a scrollable element.
        render_batch: Number of children built at the same time when the user scrolls the list.
        render_interval: Time interval in seconds between each batch of children build.

    Attributes:
        item_builder (Callable[[int], Optional[~pyfyre.nodes.Node]]):
            Builder for a child of this list.
            Called only with indices greater than or equal to zero and less than ``count``.
            None can be returned in the builder to skip the current index.
        count (Optional[int]): Number of times this list will attempt to build a child.
            If None, infinite attempts will be made.
        max_height (str): Maximum height of this element.
            A ``max-height`` CSS property is required to make a scrollable element.
        render_batch (int): Number of children built at the same time when the user scrolls the list.
        render_interval (float): Time interval in seconds between each batch of children build.
        index (int): Current index of this list builder.
    """

    def __init__(
        self,
        item_builder: Callable[[int], Optional[Node]],
        *,
        count: Optional[int] = None,
        max_height: str = "300px",
        render_batch: int = 10,
        render_interval: float = 0,
        styles: Optional[List[Style]] = None,
        states: Optional[List[State[Any]]] = None,
        attrs: Optional[Dict[str, str]] = None
    ) -> None:
        styles = styles or []
        self.item_builder = item_builder
        self.count = count
        self.max_height = max_height
        self.render_batch = render_batch
        self.render_interval = render_interval

        self.index = 0
        self._rendered_children: List[Node] = []

        super().__init__(
            "div",
            lambda: self._rendered_children,
            attrs=attrs,
            styles=[
                Style(
                    overflow_y="scroll",
                    overflow_wrap="break-word",
                    max_height=max_height,
                )
            ]
            + styles,
            states=states,
        )

        def render_nodes(event: DOMEvent) -> None:
            el = event.target
            if el.scrollHeight - el.scrollTop - el.clientHeight < 1:
                rendered = self.render_next_children()
                if rendered:
                    render_nodes(event)

        self.add_event_listener("scroll", render_nodes)

    def render_next_children(self) -> bool:
        """Build the next batch of children of this list.

        Returns:
            True if a new child is built. Otherwise, False.
        """
        prev_index = self.index

        for _ in range(self.render_batch):
            if self.count is not None:
                if self.index >= self.count:
                    break

            try:
                child = self.item_builder(self.index)
            except Exception:
                error_children = self.on_build_error(*sys.exc_info())
                child = Element("div", lambda: error_children)

            if child is not None:
                self._rendered_children.append(child)

            self.index += 1

        if self.index > prev_index:
            self.update_dom()
            return True

        return False

    def build_children(self, *, propagate: bool = True) -> None:
        super().build_children(propagate=propagate)

        def render_next_children() -> None:
            if self.dom.scrollHeight == self.dom.clientHeight:
                self.render_next_children()
            else:
                timer.clear_interval(interval)

        interval = timer.set_interval(render_next_children, self.render_interval)
