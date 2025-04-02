from municipality_lookup import MunicipalityDB

def main():
    db = MunicipalityDB("data/comuni.csv")

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

if __name__ == "__main__":
    main()
