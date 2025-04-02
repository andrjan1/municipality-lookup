from municipality_lookup import MunicipalityDB

_db_instance = None

def get_db(csv_path: str = "data/comuni.csv") -> MunicipalityDB:
    global _db_instance
    if _db_instance is None:
        _db_instance = MunicipalityDB(csv_path)
    return _db_instance
