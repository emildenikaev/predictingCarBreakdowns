import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.calibration import CalibratedClassifierCV

from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier



def preprocess(data: list) -> pd.DataFrame:

    '''
    This function describes the process of prepearing data for model
    and making some new features.
    '''

    dislok, wag_prob, wag_param, freight_info, kti_izm, pr_rem, tr_rem, target = data

    target["month"] = pd.to_datetime(target["month"]) - pd.Timedelta("1day")
    target["m"] = target["month"].dt.month

    dislok["m"] = dislok["plan_date"].dt.month

    df = target.merge(
        dislok.drop_duplicates(["wagnum", "m"], keep="last"),
        on=["wagnum", "m"],
        how="left"
    )

    df = df.merge(
        wag_prob.drop_duplicates(["wagnum", "month"], keep="last").rename({"month":"m"}, axis=1).drop("ost_prob", axis=1),
        on=["wagnum", "m"],
        how="left"
    )

    df = df.merge(
        wag_param.drop_duplicates(subset='wagnum', keep='last').drop("rod_id", axis=1),
        on="wagnum",
        how="left"
    )

    tr_rem["m"] = tr_rem["rem_month"].dt.month

    tr_rem_features = tr_rem.groupby(["wagnum", "m"], as_index=False).agg(
        {
            "gr_probeg": ["last", "count"] ,
            "por_probeg": "last",
        }
    )

    tr_rem_features.columns = [f"{head}_{stat}" if stat != "" else head for head, stat in tr_rem_features.columns]

    df = df.merge(
        tr_rem_features,
        on=["wagnum", "m"],
        how="left"
    )


    df["days_from_dep"] = (df["month"] - df["date_dep"]).dt.days
    df["days_from_kap"] = (df["month"] - df["date_kap"]).dt.days
    df["days_from_build"] = (df["month"] - df["date_build"]).dt.days
    df["days_to_srok_sl"] = (df["srok_sl"] - df["month"]).dt.days
    df["days_to_pl_rem"] = (df["date_pl_rem"] - df["month"]).dt.days

    df = df.drop(
        ["m", "month", "plan_date", "date_kap", "date_dep", #"fr_id_y",
         "date_pl_rem", "repdate", "date_iskl", "srok_sl", "date_build"], axis=1)

    df["tipvozd"] = df["tipvozd"].astype("int")

    return df.fillna(-9999)


# ------------------------------Models----------------------------------------

def model_prediction():
    X_test = df_test.drop(["wagnum", "target_month", "target_day"], axis=1)

    preds_month = np.zeros(X_test.shape[0])
    preds_day = np.zeros(X_test.shape[0])

    for model_m, model_d in zip(models_month, models_day):
        preds_month += model_m.predict(X_test) / len(models_month)
        preds_day += model_d.predict(X_test) / len(models_month)



def model_predict(number_1, date, class_1, period):
    predictions = (number for number in range(number_1))
    print('predictions')
    return predictions
