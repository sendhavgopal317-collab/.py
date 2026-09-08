"""
MODULE 1 SOLUTION: Foundations of Learning
"""

import numpy as np


class LinearRegressionGD:
    def __init__(self, lr=0.01, n_iters=1000, l2_lambda=0.0):
        self.lr = lr
        self.n_iters = n_iters
        self.l2_lambda = l2_lambda
        self.w = None
        self.b = None
        self.loss_history = []

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0.0

        for i in range(self.n_iters):
            y_pred = X @ self.w + self.b

            mse = np.mean((y_pred - y) ** 2)
            l2_penalty = self.l2_lambda * np.sum(self.w ** 2)
            loss = mse + l2_penalty
            self.loss_history.append(loss)

            dw = (2 / n_samples) * X.T @ (y_pred - y) + 2 * self.l2_lambda * self.w
            db = (2 / n_samples) * np.sum(y_pred - y)

            self.w -= self.lr * dw
            self.b -= self.lr * db

        return self

    def predict(self, X):
        return X @ self.w + self.b


def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))


class LogisticRegressionGD:
    def __init__(self, lr=0.1, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.w = None
        self.b = None
        self.loss_history = []

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0.0
        eps = 1e-9

        for i in range(self.n_iters):
            z = X @ self.w + self.b
            y_pred = sigmoid(z)

            y_pred_clipped = np.clip(y_pred, eps, 1 - eps)
            loss = -np.mean(y * np.log(y_pred_clipped) + (1 - y) * np.log(1 - y_pred_clipped))
            self.loss_history.append(loss)

            dw = (1 / n_samples) * X.T @ (y_pred - y)
            db = (1 / n_samples) * np.sum(y_pred - y)

            self.w -= self.lr * dw
            self.b -= self.lr * db

        return self

    def predict_proba(self, X):
        return sigmoid(X @ self.w + self.b)

    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)


if __name__ == "__main__":
    np.random.seed(0)

    X_lin = np.random.randn(200, 3)
    true_w = np.array([2.0, -1.0, 0.5])
    y_lin = X_lin @ true_w + 3.0 + np.random.randn(200) * 0.1

    model = LinearRegressionGD(lr=0.1, n_iters=500)
    model.fit(X_lin, y_lin)
    print("=== Linear Regression ===")
    print("Learned weights:", model.w, " (true:", true_w, ")")
    print("Learned bias:", model.b, " (true: 3.0)")
    print("Final loss:", model.loss_history[-1])
    print("Loss decreasing?", model.loss_history[0] > model.loss_history[-1])

    X_log = np.random.randn(200, 2)
    y_log = (X_log[:, 0] + X_log[:, 1] > 0).astype(int)

    clf = LogisticRegressionGD(lr=0.5, n_iters=500)
    clf.fit(X_log, y_log)
    preds = clf.predict(X_log)
    acc = (preds == y_log).mean()
    print("\n=== Logistic Regression ===")
    print("Final loss:", clf.loss_history[-1])
    print("Training accuracy:", acc)

    try:
        from sklearn.linear_model import LinearRegression
        sk_lin = LinearRegression().fit(X_lin, y_lin)
        print("\n=== sklearn comparison ===")
        print("sklearn linear weights:", sk_lin.coef_, " bias:", sk_lin.intercept_)
    except ImportError:
        print("\n(sklearn not installed here -- compare manually against true_w)")