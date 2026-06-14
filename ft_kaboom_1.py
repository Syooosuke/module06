def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record

        result = dark_spell_record('Dark', 'bats, frogs and arsenic')
        print(result)

    except ImportError as e:
        print(f"DarkError: {e}")

if __name__ == "__main__":
    main()
