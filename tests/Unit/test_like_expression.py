
test_cases = [
    ["aBBBa","a*a", True, "a.*a"],
    ["F", "[A-Z]", True, "[A-Z]"],
    ["F", "[!A-Z]", False, "[^A-Z]"],
    ["a2a", "a#a", True, "a\da"],
    ["aM5b", "a[L-P]#[!c-e]", True, "a[L-P]\d[^c-e]"],
    ["BAT123khg", "B?T*", True, "B.T.*"],
    ["CAT123khg", "B?T*", False, "B.T.*"],
    ["ab", "a*b", True, "a.*b"],
    ["a*b", "a [*]b", False, "a \*b"],
    ["axxxxxb", "a [*]b", False, "a \*b"],
    ["a [xyz", "a [[]*", True, "a \[.*"]
]
# MyCheck = "a [xyz" Like "a [*"    ' Throws Error 93 (invalid pattern string).
