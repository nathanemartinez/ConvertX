from .exceptions import MissingArgumentsError


def check_args(required, **kwargs):
	need = []
	for arg in required:
		if arg not in kwargs:
			need.append(arg)
	if (not need) == False:
		raise MissingArgumentsError(f"Missing required arguments: {need}")
