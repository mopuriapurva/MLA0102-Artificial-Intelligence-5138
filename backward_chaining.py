# Backward Chaining in Python

def backward_chaining(kb, goal, derived=None):
    if derived is None:
        derived = set()

    if goal in derived:
        return True
    derived.add(goal)

    # If goal is a known fact
    if goal in kb["facts"]:
        return True

    # Search through rules
    for rule in kb["rules"]:
        head, body = rule
        if head == goal:
            if all(backward_chaining(kb, subgoal, derived) for subgoal in body):
                return True

    return False


if __name__ == "__main__":
    # Knowledge Base
    kb = {
        "facts": {
            'vertebrate("duck")',
            'flying("duck")',
            'mammal("cat")'
        },
        "rules": [
            ('vertebrate(A)', ['mammal(A)']),
            ('animal(A)', ['vertebrate(A)']),
            ('bird(A)', ['vertebrate(A)', 'flying(A)'])
        ]
    }

    goal = input("Enter the goal (e.g., animal(\"duck\")): ").strip()

    if backward_chaining(kb, goal):
        print(f"\n✅ The goal {goal} can be derived from the knowledge base.")
    else:
        print(f"\n❌ The goal {goal} cannot be derived from the knowledge base.")
