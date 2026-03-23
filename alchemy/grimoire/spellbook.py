from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    if validate_ingredients(ingredients).__contains__("- VALID"):
        return f"Spell recorded: {spell_name} \
            ({validate_ingredients(ingredients)})"
    else:
        return f"Spell rejected: {spell_name} \
            ({validate_ingredients(ingredients)})"
