LabelImg
========

.. image:: https://img.shields.io/pypi/v/labelimg.svg
        :target: https://pypi.python.org/pypi/labelimg

.. image:: https://img.shields.io/badge/lang-en-blue.svg
        :target: https://github.com/ez4bk/labelImg-bkcn

.. image:: https://img.shields.io/badge/lang-zh-green.svg
        :target: https://github.com/ez4bk/labelImg-bkcn/readme/README.zh.rst

LabelImg 是图形标注工具，用python和PyQt写成。

作为原LabelImg的分支，这个版本进行了更多私人化的定制，此README文件也进行了相应的更改。

此版本的LabelImg支持对 fcakyon/YOLOv5 模型的训练，使用中选择YAML文件和权重PT文件后即可进行训练。
请将YAML文件和权重文件放在跟目录 data 文件夹内。
YAML文件会根据图片和标注文件自动修改/生成。

支持的存储文件包括 PASCAL VOC、YOLO、createML。

.. image:: https://raw.githubusercontent.com/tzutalin/labelImg/master/demo/demo3.jpg
     :alt: Demo Image

.. image:: https://raw.githubusercontent.com/tzutalin/labelImg/master/demo/demo.jpg
     :alt: Demo Image


安装
------------------


从源代码进行Build
~~~~~~~~~~~~~~~~~

Linux/Ubuntu/Mac 需要 Python 和 `PyQt <https://pypi.org/project/PyQt5/>`__

macOS (M1 - 此分支在此环境中开发)
^^^^^
Python 3 + Qt5

.. code:: shell

    # 右击终端，选择"使用Rosetta打开"后，重启终端
    /usr/bin/python -m venv venv # 创建虚拟环境 env
    source env/bin/activate # 激活虚拟环境
    pip install pyqt5 lxml # 通过pip安装qt和lxml
    # 必须使用通过Rosetta打开的终端安装pyqt5，否则M1平台的Mac会默认使用arm64架构的python进行安装，而pyqt5目前不支持arm64架构
    # 目前只能通过类似办法使用PyQt5，PyQt6已经支持arm64架构，但是labelImg目前不支持PyQt6

    make qt5py3
    python3 labelImg.py
    python3 labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

macOS (Intel)
^^^^^

Python 3 + Qt5

.. code:: shell

    pip3 install pyqt5 lxml

    make qt5py3
    python3 labelImg.py
    python3 labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

配置完环境后，进入项目根目录，执行以下命令即可启动labelImg

.. code:: shell

    pyrcc5 -o libs/resources.py resources.qrc

    python labelImg.py
    python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

若要打包成可执行EXE文件，执行以下命令

.. code:: shell

    Install pyinstaller and execute:

    pip install pyinstaller
    pyinstaller --hidden-import=pyqt5 --hidden-import=lxml -F -n "labelImg" -c labelImg.py -p ./libs -p ./


使用方法
-----

打标签
~~~~~~~~~~~~~~~~~~~~~~~~~~

修改此档案
`data/predefined\_classes.txt <https://github.com/tzutalin/labelImg/blob/master/data/predefined_classes.txt>`__

快捷键
~~~~~~~

+--------------------+--------------------------------------------+
| Ctrl + u           | 从目录读取所有图片                            |
+--------------------+--------------------------------------------+
| Ctrl + r           | 更改标签文件的保存路径                         |
+--------------------+--------------------------------------------+
| Ctrl + s           | 保存                                       |
+--------------------+--------------------------------------------+
| Ctrl + d           | 复制当前标签和方框                            |
+--------------------+--------------------------------------------+
| Ctrl + Shift + d   | 刪除当前图片                                 |
+--------------------+--------------------------------------------+
| Space              | 标注当前图片为已认证                           |
+--------------------+--------------------------------------------+
| w                  | 创建新的方框                                 |
+--------------------+--------------------------------------------+
| d                  | 下一张图片                                   |
+--------------------+--------------------------------------------+
| a                  | 上一张图片                                   |
+--------------------+--------------------------------------------+
| del                | 刪除所选方框                                 |
+--------------------+--------------------------------------------+
| Ctrl++             | 放大图片                                    |
+--------------------+--------------------------------------------+
| Ctrl--             | 缩小图片                                    |
+--------------------+--------------------------------------------+
| ↑→↓←               | 移动所选方框                                 |
+--------------------+--------------------------------------------+
