import io
import time
from io import StringIO
from typing import List
from functools import wraps
from pathlib import Path
import json
import pandas as pd
import numpy as np
import psycopg2
import psycopg2.extras
import normalized_tags.config as config
import normalized_tags.queries as queries
from normalized_tags.utils import profile

@profile
def get_metrics():
    """Get metrics
    """  

    query_1 = queries.calculate_metrics(
        group_by=["lead_time", "nwm_feature_id", "geom"],
        order_by=["lead_time"],
        filters=[
            {
                "column": "nwm_feature_id",
                "operator": "in",
                "value": "('6731199','2441678','14586327','8573705','2567762','41002752','8268521','41026212','4709060','20957306')"
            }
        ]
    )

    query_2 = queries.calculate_metrics(
        group_by=["nwm_feature_id", "geom", "configuration"],
        order_by=["nwm_feature_id"],
        filters=[
            {
                "column": "configuration",
                "operator": "=",
                "value": "'medium_range_mem1'"
            }
        ]
    )

    df = pd.read_sql(query_1, config.CONNECTION)
    print(df.info(memory_usage="deep"))
    print(df)

    # with psycopg2.connect(config.CONNECTION) as conn:
    #     with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
    #         cursor.execute(query_1, ())
    #         results = cursor.fetchall()
    #         print(len(results))
    #         for row in results:
    #             print(json.dumps(row, indent=4, sort_keys=True, default=str))
    #         conn.commit()
    #     cursor.close()
    # conn.close()


if __name__ == "__main__":
    get_metrics()