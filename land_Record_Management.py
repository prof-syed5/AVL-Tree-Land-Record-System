from dataclasses import dataclass
from typing import Optional, List, Callable, Any
import sys

@dataclass
class PlotRecord:
    plot_number: int
    owner_name: str
    area_size: float
    location: str

    def __str__(self) -> str:
        return f"Plot#: {self.plot_number} | Owner: {self.owner_name} | Area: {self.area_size} | Location: {self.location}"


class _AVLNode:
    def __init__(self, record: PlotRecord):
        self.record = record
        self.left: Optional[_AVLNode] = None
        self.right: Optional[_AVLNode] = None
        self.height = 1


class AVLTree:
    def __init__(self, key_func: Callable[[PlotRecord], Any]):
        self.root: Optional[_AVLNode] = None
        self.key_func = key_func

    def _height(self, node: Optional[_AVLNode]) -> int:
        return node.height if node else 0

    def _update_height(self, node: _AVLNode):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance(self, node: Optional[_AVLNode]) -> int:
        return self._height(node.left) - self._height(node.right) if node else 0

    def _rotate_left(self, x: _AVLNode) -> _AVLNode:
        y = x.right
        x.right = y.left
        y.left = x
        self._update_height(x)
        self._update_height(y)
        return y

    def _rotate_right(self, y: _AVLNode) -> _AVLNode:
        x = y.left
        y.left = x.right
        x.right = y
        self._update_height(y)
        self._update_height(x)
        return x

    def _rebalance(self, node: _AVLNode) -> _AVLNode:
        balance = self._balance(node)
        if balance > 1:
            if self._balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def insert(self, record: PlotRecord):
        def _insert(node: Optional[_AVLNode], record: PlotRecord) -> _AVLNode:
            if not node:
                return _AVLNode(record)
            key = self.key_func(record)
            node_key = self.key_func(node.record)
            if key < node_key or (key == node_key and record.plot_number < node.record.plot_number):
                node.left = _insert(node.left, record)
            elif key > node_key or (key == node_key and record.plot_number > node.record.plot_number):
                node.right = _insert(node.right, record)
            else:
                raise ValueError(f"Duplicate plot: {record.plot_number}")
            self._update_height(node)
            return self._rebalance(node)
        self.root = _insert(self.root, record)

    def _inorder(self, node: Optional[_AVLNode], out: List[PlotRecord]):
        if node:
            self._inorder(node.left, out)
            out.append(node.record)
            self._inorder(node.right, out)

    def inorder(self) -> List[PlotRecord]:
        out: List[PlotRecord] = []
        self._inorder(self.root, out)
        return out

    def _find(self, node: Optional[_AVLNode], predicate: Callable[[PlotRecord], bool]) -> Optional[PlotRecord]:
        if node:
            if predicate(node.record):
                return node.record
            return self._find(node.left, predicate) or self._find(node.right, predicate)
        return None

    def find_by_plot(self, plot_number: int) -> Optional[PlotRecord]:
        return self._find(self.root, lambda r: r.plot_number == plot_number)

    def find_by_area(self, area: float) -> List[PlotRecord]:
        results: List[PlotRecord] = []
        def _collect(node: Optional[_AVLNode]):
            if node:
                _collect(node.left)
                if abs(node.record.area_size - area) < 1e-9:
                    results.append(node.record)
                _collect(node.right)
        _collect(self.root)
        return results

    def delete_by_key(self, key_value: Any, key_eq: Callable[[_AVLNode, Any], bool]):
        def _min(node: _AVLNode) -> _AVLNode:
            while node.left:
                node = node.left
            return node

        def _delete(node: Optional[_AVLNode], key_value: Any) -> Optional[_AVLNode]:
            if not node:
                raise KeyError("Not found")
            if key_eq(node, key_value):
                if not node.left: return node.right
                if not node.right: return node.left
                temp = _min(node.right)
                node.record = temp.record
                node.right = _delete(node.right, self.key_func(temp.record))
            elif self.key_func(node.record) > key_value:
                node.left = _delete(node.left, key_value)
            else:
                node.right = _delete(node.right, key_value)
            self._update_height(node)
            return self._rebalance(node)
        self.root = _delete(self.root, key_value)


class LandRecordsManager:
    def __init__(self, index_by='plot'):
        self.index_by = index_by
        self.tree = AVLTree(self._key_func())

    def _key_func(self):
        return (lambda r: r.plot_number) if self.index_by == 'plot' else (lambda r: r.area_size)

    def add_record(self, record: PlotRecord):
        if self.index_by == 'plot' and self.tree.find_by_plot(record.plot_number):
            raise ValueError(f"Plot {record.plot_number} exists")
        self.tree.insert(record)

    def search_by_plot(self, plot_number: int):
        return self.tree.find_by_plot(plot_number)

    def search_by_area(self, area: float):
        return self.tree.find_by_area(area)

    def delete_by_plot(self, plot_number: int):
        self.tree.delete_by_key(plot_number, lambda node, key: node.record.plot_number == key)

    def delete_by_area(self, area: float):
        self.tree.delete_by_key(area, lambda node, key: abs(node.record.area_size - key) < 1e-9)

    def list_all(self):
        return self.tree.inorder()


def get_int(prompt: str) -> int:
    while True:
        try: return int(input(prompt).strip())
        except: print("Enter valid integer.")

def get_float(prompt: str) -> float:
    while True:
        try: return float(input(prompt).strip())
        except: print("Enter valid number.")


def main_cli():
    print("\n Land Records Management System")
    mode = input("Index by: 1) Plot 2) Area: ").strip()
    mgr = LandRecordsManager('plot' if mode=='1' else 'area')

    while True:
        print("\n1) Add 2) Search Plot 3) Search Area 4) Delete Plot 5) Delete Area 6) List All 7) Exit")
        ch = input("Choice: ").strip()
        if ch=='1':
            try:
                mgr.add_record(PlotRecord(get_int("Plot#: "), input("Owner: "), get_float("Area: "), input("Location: ")))
                print("Added.")
            except ValueError as e: print("Error:", e)
        elif ch=='2': print(mgr.search_by_plot(get_int("Plot#: ")) or "Not found.")
        elif ch=='3':
            res = mgr.search_by_area(get_float("Area: "))
            print(*res, sep='\n') if res else print("Not found.")
        elif ch=='4':
            try: mgr.delete_by_plot(get_int("Plot#: ")); print("Deleted.")
            except KeyError: print("Not found.")
        elif ch=='5':
            try: mgr.delete_by_area(get_float("Area: ")); print("Deleted.")
            except KeyError: print("Not found.")
        elif ch=='6':
            print(*mgr.list_all(), sep='\n')
        elif ch=='7': break
        else: print("Invalid choice.")


if __name__ == '__main__':
    try: main_cli()
    except KeyboardInterrupt: print("\nExiting."); sys.exit(0)
