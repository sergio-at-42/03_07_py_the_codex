#!/usr/bin/env python3

from alchemy.grimoire import validate_ingredients, record_spell


def ft_circular_curse() -> None:
    print("=== Circular Curse Breaking ===")
    print("")
    print("Testing ingredient validation:")
    print(f"validate_ingredients(\"fire\"): {validate_ingredients("fire")}")
    print(f"validate_ingredients(\"dragon scales\"): {validate_ingredients("dragon scales")}")
    print("")
    print("Testing spell recording with validation:")
    print(f"record_spell(\"Fireball\", \"fire\"): {record_spell("Fireball", "fire")}")
    print(f"record_spell(\"Dark Magic\", \"shadow\"): {record_spell("Dark Magic", "shadow")}")
    print("")
    print("Testing late import technique:")
    print(f"record_spell(\"Lightning\", \"air\"): {record_spell("Lightning", "air")}")
    print("")
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    ft_circular_curse()
