from pkg1.base_pipeline import BasePipeline


class Pipeline(BasePipeline):
    def __init__(self):
        super().__init__()

    def run(self):
        print("Running pipeline A")

    def preprocess(self):
        pass

    def feature_extraction(self):
        pass

    def train(self):
        pass
