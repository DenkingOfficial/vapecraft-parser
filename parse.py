import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def check_availability(id: int) -> bool:
    r = requests.head(f"https://vapecraft.org/e-liquid-recipe/{id}/")
    return r.status_code == 200


def construct_link_col():
    valid_url_df = pd.DataFrame([], columns=["id", "link"])

    def process_id(id):
        if check_availability(id):
            return {"id": id, "link": f"https://vapecraft.org/e-liquid-recipe/{id}/"}
        return None

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = list(tqdm(executor.map(process_id, range(1, 53001)), total=53000))

    for result in results:
        if result is not None:
            valid_url_df = valid_url_df.append(result, ignore_index=True)

    return valid_url_df


if __name__ == "__main__":
    df = construct_link_col()
    df.to_parquet("valid_url_df.parquet")
