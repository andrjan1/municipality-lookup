# 🏛️ Municipality Lookup

**Municipality Lookup** is a Python library to search for Italian municipality information based on a structured CSV file.  
It supports exact and fuzzy search, name normalization, automatic caching, and easy data updates.

---

## ⚙️ Installation

### 🔹 Option 1 — Standard installation

```bash
pip install .
```

> Use this mode if you **don't need to modify the library code**.

---

### 🔹 Option 2 — Editable/development installation

```bash
pip install -e .
```

> Recommended if you're actively **developing or testing** the library.

---

## 🚀 Basic usage

```python
from municipality_lookup.instance import get_db

db = get_db()
print(db.get_by_name("abno terme"))               # Fuzzy search
print(db.get_all_provinces())                     # Unique provinces
print(db.get_all_land_registries())               # Unique land registries
```

---

## 🧪 Running tests

```bash
pytest
```

---

## 📄 Data format and source

The expected CSV format is:

```
Comune,Provincia,Conservatoria di Competenza,Codice Nazionale,Codice Catastale
```

The current dataset is based on publicly available data from the following source:

🔗 [https://www.visurasi.it/elenco-conservatorie-e-comuni](https://www.visurasi.it/elenco-conservatorie-e-comuni)

---

## 📜 License

MIT – © Andrea Iannazzo
