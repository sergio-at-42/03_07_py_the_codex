# from .validator import validate_ingredients


def record_spell(spell_name: str, ing: str) -> str:
    from .validator import validate_ingredients
    if validate_ingredients(ing).__contains__("- VALID"):
        return f"Spell recorded: {spell_name} ({validate_ingredients(ing)})"
    else:
        return f"Spell rejected: {spell_name} ({validate_ingredients(ing)})"
