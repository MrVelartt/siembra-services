from sqlalchemy import func

def normalize(col):
    return func.lower(
        func.replace(
            func.replace(
                func.replace(
                    func.replace(
                        func.replace(col, "á", "a"),
                    "é", "e"),
                "í", "i"),
            "ó", "o"),
        "ú", "u")
    )
