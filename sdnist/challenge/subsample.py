import pandas as pd

from sdnist.challenge.submission import Model, run


class SubsampleModel(Model):
    def __init__(self, frac: float = .1):
        self.frac = frac

    def train(self, private_dataset: pd.DataFrame, schema: dict, eps: float = 0):
        self.dataset = private_dataset

    def generate(self, n: int, eps: float):
        return self.dataset.sample(frac=self.frac)


if __name__ == "__main__":
    model = SubsampleModel(frac=.7)
    run(submission=model,
        challenge="census",
        public=True)
