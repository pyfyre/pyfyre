from browser import aio
from pyfyre.nodes import Node, Element
from typing import Dict, List, Optional, Callable, Awaitable
from pyfyre.exceptions import (
	FutureNoResult, FutureCancelled, FutureAlreadyDone
)


class FutureElement(Element):
	"""Error handling is not currently supported."""
	
	def __init__(
		self,
		tag_name: str,
		children: Callable[[], Awaitable[List[Node]]],
		*,
		attrs: Optional[Dict[str, str]] = None,
	) -> None:
		self._is_done = False
		self._is_cancelled = False
		self._result: Optional[List[Node]] = None
		self._exception: Optional[BaseException] = None
		self._done_callbacks: List[Callable[["FutureElement"], None]] = []
		super().__init__(tag_name, lambda: self._process_result(), attrs=attrs)
		
		async def build_children(
			children: Callable[[], Awaitable[List[Node]]]
		) -> None:
			res = await children()
			
			# Set [ignore_done] to `True` to not have an error when this
			# future is already done before it sets the result.
			is_successful = self.set_result(res, ignore_done=True)
			
			if is_successful:
				self.update_dom()
		
		aio.run(build_children(children))
	
	def _process_result(self) -> List[Node]:
		try:
			return self.result()
		except FutureNoResult:
			return self.while_no_result()
	
	def while_no_result(self) -> List[Node]:
		return [Element(
			"div",
			lambda: [Element("div") for _ in range(12)],
			attrs={"class": "lds"}
		)]
	
	def result(self) -> List[Node]:
		if self.is_done():
			if self._result is not None:
				return self._result
			
			if self._exception is not None:
				raise self._exception
		
		if self.is_cancelled():
			raise FutureCancelled()
		
		raise FutureNoResult()
	
	def _mark_as_done(self) -> None:
		self._is_done = True
		
		for callback in self._done_callbacks:
			callback(self)
	
	def set_result(
		self, result: List[Node], *, ignore_done: bool = False
	) -> bool:
		if self.is_done():
			if ignore_done:
				return False
			
			raise FutureAlreadyDone()
		
		self._result = result
		self._mark_as_done()
		return True
	
	def set_exception(
		self, exception: BaseException, *, ignore_done: bool = False
	) -> bool:
		if self.is_done():
			if ignore_done:
				return False
			
			raise FutureAlreadyDone()
		
		self._exception = exception
		self._mark_as_done()
		return True
	
	def is_done(self) -> bool:
		return self.is_cancelled() or self._is_done
	
	def is_cancelled(self) -> bool:
		return self._is_cancelled
	
	def add_done_callback(
		self, callback: Callable[["FutureElement"], None]
	) -> None:
		self._done_callbacks.append(callback)
		
		if self.is_done():
			callback(self)
	
	def remove_done_callback(
		self, callback: Callable[["FutureElement"], None]
	) -> int:
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
		if self.is_done():
			return False
		
		self._is_cancelled = True
		
		for callback in self._done_callbacks:
			callback(self)
		
		return True
	
	def exception(self) -> Optional[BaseException]:
		return self._exception
