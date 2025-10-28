def towers_of_hanoi(n, source, auxiliary, target):
    """
    Solve the Towers of Hanoi problem recursively.

    Parameters:
    n : int
        Number of disks
    source : str
        The peg where disks start (e.g., 'A')
    auxiliary : str
        The peg used for temporary storage (e.g., 'B')
    target : str
        The peg where disks need to go (e.g., 'C')
    """
    if n == 1:
        print(f"Move disk 1 from {source} → {target}")
        return
    towers_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} → {target}")
    towers_of_hanoi(n - 1, auxiliary, source, target)


# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    print("\nSteps to solve the Towers of Hanoi:\n")
    towers_of_hanoi(n, 'A', 'B', 'C')
