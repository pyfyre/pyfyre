from pyfyre.nodes import Element
from pyfyre.exceptions import (
	FutureNoResult, FutureCancelled, FutureAlreadyDone
)


class FutureElement(Element):
	def __init__(
		self,
		tag_name: str,
		children,
		*,
		attrs = None,
	) -> None:
		self._is_done = False
		self._is_cancelled = False
		self._result = None
		self._exception = None
		self._done_callbacks = []
		super().__init__(tag_name, lambda: self._process_result(), attrs=attrs)
		
		def build_children(children) -> None:
			res = children
			successful = self.set_result(res, ignore_done=True)
			
			if successful:
				self.update_dom()
		
		build_children(children)
	
	def _process_result(self):
		try:
			return self.result()
		except FutureNoResult:
			return self.while_no_result()
	
	def while_no_result(self):
		return [Element(
			"div",
			lambda: [Element("div") for _ in range(12)],
			attrs={"class": "lds"}
		)]
	
	def result(self):
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
		self, result, *, ignore_done: bool = False
	) -> bool:
		if self.is_done():
			if ignore_done:
				return False
			
			raise FutureAlreadyDone()
		
		self._result = result
		self._mark_as_done()
		return True
	
	def set_exception(self, exception: BaseException) -> None:
		if self.is_done():
			raise FutureAlreadyDone()
		
		self._exception = exception
		self._mark_as_done()
	
	def is_done(self) -> bool:
		return self.is_cancelled() or self._is_done
	
	def is_cancelled(self) -> bool:
		return self._is_cancelled
	
	def add_done_callback(
		self, callback
	) -> None:
		self._done_callbacks.append(callback)
		
		if self.is_done():
			callback(self)
	
	def remove_done_callback(
		self, callback
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
	
	def exception(self):
		return self._exception
