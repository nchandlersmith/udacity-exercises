

from abc import abstractmethod, ABC


class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self, indent=0):
        pass

    @abstractmethod
    def get_size(self):
        pass


class File(FileSystemComponent):
    def __init__(self, name, size):
        super().__init__()
        self._name = name
        self._size = size

    def show_details(self, indent=0):
        return f"{' ' * indent}{self._name} {self._size} kB"

    def get_size(self):
        return self._size


class Directory(FileSystemComponent):
    def __init__(self, name, size):
        super().__init__()
        self._name = name
        self._size = size
        self._components = []

    def add_component(self, component):
        self._components.append(component)
        self._size += component.get_size()

    def show_details(self, indent=0):
        return f"{' ' * indent}{self._name} {self._size} kB\n" + \
               "\n".join([component.show_details(indent + 2) for component in self._components])

    def get_size(self):
        return self._size
