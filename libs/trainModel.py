import subprocess
import os
import yaml

from libs.constants import DEFAULT_BATCH_SIZE, DEFAULT_EPOCHS


class TrainModel(object):
    def __init__(self, parent=None, batch_size=DEFAULT_BATCH_SIZE, epochs=DEFAULT_EPOCHS, data=None, weights=None):
        self.parent = parent
        self.batch_size = str(batch_size)
        self.epochs = str(epochs)
        self.data = str(data)
        self.weights = str(weights)
        assert self.validate_params(), 'Invalid parameters!'

    @staticmethod
    def install_yolov5():
        try:
            subprocess.run(["pip", "install", "yolov5"], stdout=subprocess.PIPE, check=True)
            if subprocess.CompletedProcess.returncode == 0:
                return True
        except FileNotFoundError:
            print("请先安装python或添加pip至PATH!")
            return False
        except subprocess.CalledProcessError as err:
            print("安装yolov5时发生错误!" + str(err))
            return False

    def write_yaml_file(self):
        img_path = self.parent.default_save_dir
        assert os.path.exists(img_path), "数据不存在!"
        sample_path = img_path.split('/train/')[0]
        assert os.path.exists(sample_path), "样本数据不存在!"
        class_path = os.path.join(img_path, '../labels/classes.txt')
        assert os.path.exists(class_path), "类别数据不存在!"

        df = open(self.data, 'r')
        cf = open(class_path, 'r')
        data_yaml = yaml.safe_load(df)
        data_yaml['path'] = sample_path
        classes = cf.readlines()
        data_yaml['names'] = [''] * len(classes)
        for i in range(len(classes)):
            data_yaml['names'][i] = classes[i].strip()
        df.close()
        cf.close()
        df = open(self.data, 'w')
        yaml.dump(data_yaml, df)
        df.close()

    def validate_params(self):
        try:
            _ = int(self.batch_size)
        except ValueError:
            return False
        if not self.epochs.isnumeric():
            return False
        if int(self.epochs) < 1:
            return False
        if not os.path.exists(self.data):
            return False
        if not os.path.exists(self.weights):
            return False
        return True

    def run(self):
        if not self.validate_params():
            return
        try:
            res = subprocess.run(['python', '-m', 'yolov5.train', '--batch-size', self.batch_size, '--epochs', self.epochs,
                                  '--data', self.data, '--weights', self.weights], stdout=subprocess.PIPE, check=True)
        except FileNotFoundError:
            if self.install_yolov5():
                self.run()
            else:
                assert False, "Error! Cannot install yolov5!"
        except subprocess.CalledProcessError as err:
            # print(err.returncode)
            assert False, "Error occurred while training!"
            return


if __name__ == '__main__':
    a = TrainModel(epochs='-1', data='../data/data.yaml', weights='../data/yolov5s.pt')
    a.run()
