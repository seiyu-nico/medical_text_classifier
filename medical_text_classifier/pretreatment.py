import pandas as pd
from faker import Faker

fake = Faker("ja_JP")


def main():
    # テストデータの読み込み
    df = pd.read_csv("./dataset/labels.csv")

    children_df = df[df["parent"].notnull()]
    name_df = children_df["name"]

    # 日付を追加
    expanded_df = append_date(name_df)
    print(expanded_df.head())

    df = expanded_df.rename(columns={"name": "テキスト", "normalization": "カテゴリ"})
    df.to_csv("./dataset/train_labels.csv", index=False)


def append_date(df):
    # 各項目に対して5つの日付を生成する
    expanded_data = []
    for name in df:
        expanded_data.append({"name": name, "normalization": name})
        for _ in range(5):  # 各項目に5つの日付を追加
            random_date = fake.date_between(start_date="-2y", end_date="today")
            expanded_data.append(
                {"name": f"{random_date} {name}", "normalization": name}
            )

    return pd.DataFrame(expanded_data)


if __name__ == "__main__":
    main()
