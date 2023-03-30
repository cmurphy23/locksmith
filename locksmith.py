import threading
from decorator import decorator


class LockSmith:

    master_lock = threading.RLock()
    singleton = None

    def __init__(self):
        LockSmith.master_lock.acquire()
        try:
            if LockSmith.singleton is None:
                LockSmith.singleton = self
            else:
                raise Exception("Duplicate instantiation of singleton")
            self.static_master_lock = threading.RLock()
            self.static_locks = {}
            self.method_master_lock = threading.RLock()
            self.method_locks = {}
            self.managed_objects = {}
        finally:
            LockSmith.master_lock.release()

    @staticmethod
    def get_singleton():
        if LockSmith.singleton is None:
            LockSmith()
        return LockSmith.singleton

    def locked_method(self, name, *args, **kwargs):
        @decorator
        def locked(func, *args, **kwargs):
            calling_object = args[0]
            if not hasattr(calling_object, "method_lock_dictionary_variable_3fm9874h291n3c0s"):
                self.method_master_lock.acquire()
                try:
                    if not hasattr(calling_object, "method_lock_dictionary_variable_3fm9874h291n3c0s"):
                        calling_object.method_lock_dictionary_variable_3fm9874h291n3c0s = {}
                finally:
                    self.method_master_lock.release()
            if name not in calling_object.method_lock_dictionary_variable_3fm9874h291n3c0s:
                self.method_master_lock.acquire()
                try:
                    if name not in calling_object.method_lock_dictionary_variable_3fm9874h291n3c0s:
                        calling_object.method_lock_dictionary_variable_3fm9874h291n3c0s[name] = threading.RLock()
                finally:
                    self.method_master_lock.release()
            calling_object.method_lock_dictionary_variable_3fm9874h291n3c0s[name].acquire()
            try:
                return func(*args, **kwargs)
            finally:
                calling_object.method_lock_dictionary_variable_3fm9874h291n3c0s[name].release()
        return locked

    def locked_function(self, name):
        self.static_master_lock.acquire()
        try:
            if name not in self.static_locks:
                self.static_locks[name] = threading.RLock()

            @decorator
            def locked(func, *args, **kwargs):
                self.static_locks[name].acquire()
                try:
                    func(*args, **kwargs)
                finally:
                    self.static_locks[name].release()

            return locked_function
        finally:
            self.static_master_lock.release()


def locked_method(*args, **kwargs):
    return LockSmith.get_singleton().locked_method(*args, **kwargs)


def locked_function(name):
    return LockSmith.get_singleton().locked_function(name)
