import json

def diff_keys(a: dict, b: dict) -> dict:
    ka, kb = set(a.keys()), set(b.keys())
    return {"added": sorted(kb - ka), "removed": sorted(ka - kb)}
