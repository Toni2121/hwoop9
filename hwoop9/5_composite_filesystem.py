import os


class Component:
    def draw(self, indent=0):
        raise NotImplementedError


class Leaf(Component):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def draw(self, indent=0):
        print(" " * indent + f"File: {self.name} ({self.size} bytes)")


class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def draw(self, indent=0):
        print(" " * indent + f"Directory: {self.name}")
        for child in self.children:
            child.draw(indent + 2)


def build_filesystem_tree(path):
    if os.path.isfile(path):
        size = os.path.getsize(path)
        return Leaf(os.path.basename(path), size)
    elif os.path.isdir(path):
        dir_comp = Composite(os.path.basename(path))
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            child_comp = build_filesystem_tree(full_path)
            dir_comp.add(child_comp)
        return dir_comp
    else:
        raise ValueError(f"Path {path} is neither file nor directory")


if __name__ == "__main__":
    root_path = "."
    root = build_filesystem_tree(root_path)
    root.draw()
