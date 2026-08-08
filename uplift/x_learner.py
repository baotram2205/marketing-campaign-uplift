def construct_pseudo_effects(
    treatment_model,
    control_model,
    X_treated,
    y_treated,
    X_control,
    y_control,
):
    mu0_treated = control_model.predict_proba(X_treated)[:, 1]
    mu1_control = treatment_model.predict_proba(X_control)[:, 1]

    D1 = y_treated.to_numpy() - mu0_treated
    D0 = mu1_control - y_control.to_numpy()

    return D1, D0


from lightgbm import LGBMRegressor

def train_effect_models(
    X_treated,
    D1,
    X_control,
    D0,
    random_state=42,
):
    params = {
        "n_estimators": 100,
        "learning_rate": 0.1,
        "num_leaves": 31,
        "random_state": random_state,
        "verbosity": -1,
    }

    tau_model_treated = LGBMRegressor(**params)
    tau_model_control = LGBMRegressor(**params)

    tau_model_treated.fit(X_treated, D1)
    tau_model_control.fit(X_control, D0)

    return tau_model_treated, tau_model_control

def estimate_x_cate(
    tau_model_treated,
    tau_model_control,
    propensity_model,
    X,
):
    tau_treated_pred = tau_model_treated.predict(X)
    tau_control_pred = tau_model_control.predict(X)

    propensity = propensity_model.predict_proba(X)[:, 1]

    estimated_cate = (
        propensity * tau_control_pred
        + (1 - propensity) * tau_treated_pred
    )

    return estimated_cate, tau_treated_pred, tau_control_pred, propensity