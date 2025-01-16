import joblib


def main():
    """
    テキストのカテゴリを予測する。
    """
    texts = [
        "2025/10/11バファリン",
        "2025-10-11バファリン",
        "バファリン",
        "パファリシ",
        # "胸部CT",
        # "コンフォティス",
        # "ペッツケアーフォーム",
        # "レントゲンDVD(~10kg)"
    ]

    preds = predictions(texts)
    for text, pred in zip(texts, preds):
        print("======================")
        print("入力:", text)
        print("出力", pred)


def predictions(texts: list[str]) -> list[str]:
    """
    テキストのカテゴリを予測する。

    Args:
        text (str): テキストデータ。

    Returns:
        str: 予測されたカテゴリ。
    """
    model_path = "model/model.pkl"
    vectorizer_path = "model/vectorizer.pkl"

    # ロジスティック回帰モデルの読み込み
    clf = joblib.load(model_path)
    # TfidfVectorizerの読み込み
    vectorizer = joblib.load(vectorizer_path)

    # テキストの予測
    X = vectorizer.transform(texts)
    predictions = clf.predict(X)

    return predictions


if __name__ == "__main__":
    main()
