#!/usr/bin/env python3

from alchemy.grimoire import validate_ingredients, record_spell


def ft_circular_curse() -> None:
    print("=== Circular Curse Breaking ===")
    print("")
    print("Testing ingredient validation:")
    print(f"validate_ingredients(\"fire\"): {validate_ingredients("fire")}")
    print("validate_ingredients(\"dragon scales\"):", end=" ")
    print(f"{validate_ingredients("dragon scales")}")
    print("")
    print("Testing spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire\"):", end=" ")
    print(f"{record_spell("Fireball", "fire")}")
    print("record_spell(\"Dark Magic\", \"shadow\"):", end=" ")
    print(f"{record_spell("Dark Magic", "shadow")}")
    print("")
    print("Testing late import technique:")
    print("record_spell(\"Lightning\", \"air\"):", end=" ")
    print(f"{record_spell("Lightning", "air")}")
    print("")
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    ft_circular_curse()
