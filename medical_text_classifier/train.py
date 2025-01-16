import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def train(file_path: str, model_path: str, vectorizer_path: str):
    """
    ロジスティック回帰モデルを学習し、モデルとベクトライザを保存する。

    Args:
        file_path (str): 入力データのCSVファイルパス。
        model_path (str): 学習済みモデルの保存先パス。
        vectorizer_path (str): ベクトライザの保存先パス。
    """
    # CSVファイルを読み込む
    data = pd.read_csv(file_path)

    # テキストとラベルを分割
    texts = data["テキスト"]
    labels = data["カテゴリ"]

    # テキストのベクトル化
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    # ロジスティック回帰で学習
    print("学習開始")
    clf = LogisticRegression(random_state=0, class_weight="balanced")
    clf.fit(X, labels)
    print("学習完了")

    # モデルとベクトライザを保存
    joblib.dump(clf, model_path)
    joblib.dump(vectorizer, vectorizer_path)

    print("モデルとベクトライザの保存が完了しました！")


if __name__ == "__main__":
    train("dataset/train_labels.csv", "model/model.pkl", "model/vectorizer.pkl")
