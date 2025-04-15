from municipality_lookup.instance import get_db

def main():
    db = get_db()
    
    print("🔍 Exact match:")
    print(db.get_by_name("ABANO TERME"))

    print("\n🔍 Fuzzy match with typo:")
    print(db.get_by_name("abno term"))

    print("\n🔍 Fuzzy match with typo:")
    print(db.get_by_name("A L E S S A N D R I A"))

    print("\n🔍 Fuzzy match with typo:")
    print(db.get_by_name("Ponte San Nicolò"))
    
    print("\n🔍 Fuzzy match with typo:")
    print(db.get_by_name("Er- . bezzo,"))

    print("\n🔍empty")
    print(db.get_by_name("P0Nt S GIOVAN"))


    # Get all provinces
    print(db.get_all_provinces())

    # Get all land registries
    print(db.get_all_land_registries())

if __name__ == "__main__":
    main()
