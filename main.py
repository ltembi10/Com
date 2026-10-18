
class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        side = side.lower()

        if side not in ("left", "right"):
            print("Error: Side must be 'left' or 'right'.")
            return False

        if self.root is None:
            print("Error: Add a team lead first.")
            return False

        # Start searching from the root.
        if current_node is None:
            current_node = self.root

        # Find the manager.
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is not None:
                    print("Error: The left side is already occupied.")
                    return False
                current_node.left = EmployeeNode(employee_name)
            else:
                if current_node.right is not None:
                    print("Error: The right side is already occupied.")
                    return False
                current_node.right = EmployeeNode(employee_name)

            return True

        # Search the left subtree.
        if current_node.left is not None:
            if self.insert(manager_name, employee_name, side,
                           current_node.left):
                return True

        # Search the right subtree.
        if current_node.right is not None:
            if self.insert(manager_name, employee_name, side,
                           current_node.right):
                return True

        # Report a missing manager only once, at the root.
        if current_node is self.root:
            print(f"Error: Manager '{manager_name}' was not found.")

        return False

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        if node is None:
            print("The team is empty.")
            return

        print("  " * level + "- " + node.name)

        if node.left is not None:
            self.print_tree(node.left, level + 1)

        if node.right is not None:
            self.print_tree(node.right, level + 1)


def company_directory():
    company = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")

        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            if company.root is not None:
                print("Error: A team lead already exists.")
            else:
                name = input("Enter team lead's name: ").strip()
                if name:
                    company.root = EmployeeNode(name)
                    print(f"✅ {name} added as the team lead.")
                else:
                    print("Error: Name cannot be empty.")

        elif choice == "2":
            if company.root is None:
                print("Error: Add a team lead first.")
                continue

            manager = input("Enter the manager's name: ").strip()
            employee = input("Enter the new employee's name: ").strip()
            side = input(
                "Should this employee be on the LEFT or RIGHT "
                "of the manager? "
            ).strip().lower()

            if not manager or not employee:
                print("Error: Names cannot be empty.")
                continue

            if company.insert(manager, employee, side):
                print(
                    f"✅ {employee} added to the {side.upper()} "
                    f"of {manager}"
                )

        elif choice == "3":
            print("\n🌳 Current Team Structure:")
            company.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("Invalid option. Please choose 1–4.")


if __name__ == "__main__":
    company_directory()
