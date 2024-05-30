#!/usr/bin/env python3
"""Read and filter data"""


def main() -> None:
    """Retrieve and display all rows in the users table."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]

    logger = get_logger()

    for row in cursor:
        message = "; ".join([f"{field}={value}" for field,
                             value in zip(fields, row)]) + ";"
        logger.info(message)

    cursor.close()
    db.close()
