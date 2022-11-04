from browser import aio
from pyfyre.styles import Style
from pyfyre.states import State
from pyfyre.nodes import Node, Element
from typing import Dict, List, Optional, Callable, Awaitable, Any
from pyfyre.exceptions import FutureNoResult, FutureCancelled, FutureAlreadyDone


class FutureElement(Element):
    """Just like an ``Element``, but the ``children`` returns an awaitable.
    That means the children builder of this element is asynchronous.

    This class’s implementation is similar to ``asyncio.Future``.
    """

    def __init__(
        self,
        tag_name: str,
        children: Callable[[], Awaitable[List[Node]]],
        *,
        styles: Optional[List[Style]] = None,
        states: Optional[List[State[Any]]] = None,
        attrs: Optional[Dict[str, str]] = None
    ) -> None:
        self._is_done = False
        self._is_cancelled = False
        self._result: Optional[List[Node]] = None
        self._exception: Optional[Exception] = None
        self._done_callbacks: List[Callable[["FutureElement"], None]] = []

        def process_result() -> List[Node]:
            try:
                return self.result()
            except FutureNoResult:
                return self.while_no_result()

        super().__init__(
            tag_name,
            process_result,
            styles=styles,
            states=states,
            attrs=attrs,
        )

        async def build_children(children: Callable[[], Awaitable[List[Node]]]) -> None:
            res = await children()

            try:
                self.set_result(res)
                self.update_dom()
            except FutureAlreadyDone:
                pass

        aio.run(build_children(children))

    def while_no_result(self) -> List[Node]:
        """:meta private:"""
        from pyfyre.presets.loading import Loading

        return [Loading()]

    def result(self) -> List[Node]:
        """Return the result of the Future.

        If the Future is `done` and has a result set by the ``set_result()`` method,
        the result value is returned.

        Returns:
            The result will be the children nodes of this element.

        Raises:
            Exception: If the Future is `done` and has an exception set by the
                ``set_exception()`` method, this method raises the exception.
            FutureCancelled: If the Future has been `cancelled`.
            FutureNoResult: If the Future’s result isn’t yet available.
        """
        if self.is_done():
            if self._result is not None:
                return self._result

            if self._exception is not None:
                raise self._exception

        if self.is_cancelled():
            raise FutureCancelled()

        raise FutureNoResult()

    def _mark_as_done(self) -> None:
        """Mark the Future as done and call the callbacks."""
        self._is_done = True

        for callback in self._done_callbacks:
            callback(self)

    def set_result(self, result: List[Node]) -> None:
        """Mark the Future as `done` and set its result.

        Raises:
            FutureAlreadyDone: If the Future is already `done`.
        """
        if self.is_done():
            raise FutureAlreadyDone()

        self._result = result
        self._mark_as_done()

    def set_exception(self, exception: Exception) -> None:
        """Mark the Future as `done` and set an exception.

        Raises:
            FutureAlreadyDone: If the Future is already `done`.
        """
        if self.is_done():
            raise FutureAlreadyDone()

        self._exception = exception
        self._mark_as_done()

    def is_done(self) -> bool:
        """A Future is `done` if it was `cancelled` or if it has a result or
        an exception set with ``set_result()`` or ``set_exception()`` calls.

        Returns:
            True if the Future is `done`.
        """
        return self.is_cancelled() or self._is_done

    def is_cancelled(self) -> bool:
        """
        Returns:
            True if the Future was `cancelled`.
        """
        return self._is_cancelled

    def add_done_callback(self, callback: Callable[["FutureElement"], None]) -> None:
        """Add a callback to be run when the Future is `done`.

        The ``callback`` is called with the Future object as its only argument.

        If the Future is already `done` when this method is called,
        the ``callback`` is called immediately.
        """
        self._done_callbacks.append(callback)

        if self.is_done():
            callback(self)

    def remove_done_callback(self, callback: Callable[["FutureElement"], None]) -> int:
        """Remove the ``callback`` from the callbacks list.

        Returns:
            The number of callbacks removed, which is typically 1,
            unless a callback was added more than once.
        """
        remaining_callbacks = []
        removed = 0

        for c in self._done_callbacks:
            if c == callback:
                removed += 1
            else:
                remaining_callbacks.append(c)

        self._done_callbacks = remaining_callbacks
        return removed

    def cancel(self) -> bool:
        """Cancel the Future and call the callbacks.

        Returns:
            False, if the Future is already `done` or `cancelled`.
            Otherwise, change the Future’s state to `cancelled`,
            call the callbacks, and return True.
        """
        if self.is_done():
            return False

        self._is_cancelled = True

        for callback in self._done_callbacks:
            callback(self)

        return True

    def exception(self) -> Optional[Exception]:
        """Return the exception that was set on this Future.

        Returns:
            The exception (or None if no exception was set), only if the Future is `done`.

        Raises:
            FutureCancelled: If the Future has been `cancelled`.
            FutureNoResult: If the Future isn’t `done` yet.
        """
        if self.is_done():
            return self._exception

        if self.is_cancelled():
            raise FutureCancelled()

        raise FutureNoResult()
