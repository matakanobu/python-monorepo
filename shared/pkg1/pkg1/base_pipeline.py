from abc import ABC, abstractmethod


class BasePipeline(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError

    @abstractmethod
    def preprocess(self):
        raise NotImplementedError

    @abstractmethod
    def feature_extraction(self):
        raise NotImplementedError

    @abstractmethod
    def train(self):
        raise NotImplementedError
