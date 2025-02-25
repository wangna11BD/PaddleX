[简体中文](layout_parsing.md) | English

# 通用版面解析产线使用教程

## 1. 通用版面解析产线介绍
版面解析是一种从文档图像中提取结构化信息的技术，主要用于将复杂的文档版面转换为机器可读的数据格式。这项技术在文档管理、信息提取和数据数字化等领域具有广泛的应用。版面解析通过结合光学字符识别（OCR）、图像处理和机器学习算法，能够识别和提取文档中的文本块、标题、段落、图片、表格以及其他版面元素。此过程通常包括版面分析、元素分析和数据格式化三个主要步骤，最终生成结构化的文档数据，提升数据处理的效率和准确性。

**通用****版面解析****产线中包含表格结构识别模块、版面区域分析模块、文本检测模块、文本识别模块、公式识别模块、印章文本检测模块、文本图像矫正模块和文档图像方向分类模块**。

**如您更考虑模型精度，请选择精度较高的模型，如您更考虑模型推理速度，请选择推理速度较快的模型，如您更考虑模型存储大小，请选择存储大小较小的模型**。

<details>
   <summary> 👉模型列表详情</summary>

**表格结构识别模块模型：**

<table>
  <tr>
    <th>模型</th>
    <th>精度（%）</th>
    <th>GPU推理耗时 (ms)</th>
    <th>CPU推理耗时（ms）</th>
    <th>模型存储大小 (M)</th>
    <th>介绍</th>
  </tr>
  <tr>
    <td>SLANet</td>
    <td>59.52</td>
    <td>522.536</td>
    <td>1845.37</td>
    <td>6.9 M</td>
    <td>SLANet 是百度飞桨视觉团队自研的表格结构识别模型。该模型通过采用CPU 友好型轻量级骨干网络PP-LCNet、高低层特征融合模块CSP-PAN、结构与位置信息对齐的特征解码模块SLA Head，大幅提升了表格结构识别的精度和推理速度。</td>
  </tr>
   <tr>
    <td>SLANet_plus</td>
    <td>63.69</td>
    <td>522.536</td>
    <td>1845.37</td>
    <td>6.9 M</td>
    <td>SLANet_plus 是百度飞桨视觉团队自研的表格结构识别模型SLANet的增强版。相较于SLANet，SLANet_plus 对无线表、复杂表格的识别能力得到了大幅提升，并降低了模型对表格定位准确性的敏感度，即使表格定位出现偏移，也能够较准确地进行识别。</td>
  </tr>
</table>

**注：以上精度指标测量PaddleX 内部自建英文表格识别数据集。所有模型 GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为8，精度类型为 FP32。**


**版面区域检测模块模型：**

|模型|mAP(0.5)（%）|GPU推理耗时（ms）|CPU推理耗时 (ms)|模型存储大小（M）|介绍|
|-|-|-|-|-|-|
|PicoDet_layout_1x|86.8|13.0|91.3|7.4|基于PicoDet-1x在PubLayNet数据集训练的高效率版面区域定位模型，可定位包含文字、标题、表格、图片以及列表这5类区域|
|RT-DETR-H_layout_17cls|92.6|115.1|3827.2|470.2|基于RT-DETR-H在中英文论文、杂志和研报等场景上自建数据集训练的高精度版面区域定位模型，包含17个版面常见类别，分别是：段落标题、图片、文本、数字、摘要、内容、图表标题、公式、表格、表格标题、参考文献、文档标题、脚注、页眉、算法、页脚、印章|


**注：以上精度指标的评估集是 PaddleOCR 自建的版面区域分析数据集，包含中英文论文、杂志和研报等常见的 1w 张文档类型图片。GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为 8，精度类型为 FP32。**

**文本检测模块模型：**

|模型|检测Hmean（%）|GPU推理耗时（ms）|CPU推理耗时 (ms)|模型存储大小（M)|介绍|
|-|-|-|-|-|-|
|PP-OCRv4_server_det|82.69|83.3501|2434.01|109|PP-OCRv4 的服务端文本检测模型，精度更高，适合在性能较好的服务器上部署|
|PP-OCRv4_mobile_det|77.79|10.6923|120.177|4.7|PP-OCRv4 的移动端文本检测模型，效率更高，适合在端侧设备部署|

**注：以上精度指标的评估集是 PaddleOCR 自建的中文数据集，覆盖街景、网图、文档、手写多个场景，其中检测包含 500 张图片。以上所有模型 GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为8，精度类型为 FP32。**

**文本识别模块模型：**

<table >
    <tr>
        <th>模型</th>
        <th>识别 Avg Accuracy(%)</th>
        <th>GPU推理耗时（ms）</th>
        <th>CPU推理耗时 (ms)</th>
        <th>模型存储大小（M）</th>
        <th>介绍</th>
    </tr>
    <tr>
        <td>PP-OCRv4_mobile_rec</td>
        <td>78.20</td>
        <td>7.95018</td>
        <td>46.7868</td>
        <td>10.6 M</td>
        <td rowspan="2">PP-OCRv4是百度飞桨视觉团队自研的文本识别模型PP-OCRv3的下一个版本，通过引入数据增强方案、GTC-NRTR指导分支等策略，在模型推理速度不变的情况下，进一步提升了文本识别精度。该模型提供了服务端（server）和移动端（mobile）两个不同版本，来满足不同场景下的工业需求。</td>
    </tr>
    <tr>
        <td>PP-OCRv4_server_rec </td>
        <td>79.20</td>
        <td>7.19439</td>
        <td>140.179</td>
        <td>71.2 M</td>
    </tr>
</table>

**注：以上精度指标的评估集是 PaddleOCR 自建的中文数据集，覆盖街景、网图、文档、手写多个场景，其中文本识别包含 1.1w 张图片。所有模型 GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为8，精度类型为 FP32。**


<table >
    <tr>
        <th>模型</th>
        <th>识别 Avg Accuracy(%)</th>
        <th>GPU推理耗时（ms）</th>
        <th>CPU推理耗时（ms）</th>
        <th>模型存储大小（M）</th>
        <th>介绍</th>
    </tr>
    <tr>
        <td>ch_SVTRv2_rec</td>
        <td>68.81</td>
        <td>8.36801</td>
        <td>165.706</td>
        <td>73.9 M</td>
        <td rowspan="1">
        SVTRv2 是一种由复旦大学视觉与学习实验室（FVL）的OpenOCR团队研发的服务端文本识别模型，其在PaddleOCR算法模型挑战赛 - 赛题一：OCR端到端识别任务中荣获一等奖，A榜端到端识别精度相比PP-OCRv4提升6%。
    </td>
    </tr>
</table>


**注：以上精度指标的评估集是 [PaddleOCR算法模型挑战赛 - 赛题一：OCR端到端识别任务](https://aistudio.baidu.com/competition/detail/1131/0/introduction)A榜。 所有模型 GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为8，精度类型为 FP32。**

<table >
    <tr>
        <th>模型</th>
        <th>识别 Avg Accuracy(%)</th>
        <th>GPU推理耗时（ms）</th>
        <th>CPU推理耗时（ms）</th>
        <th>模型存储大小（M）</th>
        <th>介绍</th>
    </tr>
    <tr>
        <td>ch_RepSVTR_rec</td>
        <td>65.07</td>
        <td>10.5047</td>
        <td>51.5647</td>
        <td>22.1 M</td>
        <td rowspan="1">    RepSVTR 文本识别模型是一种基于SVTRv2 的移动端文本识别模型，其在PaddleOCR算法模型挑战赛 - 赛题一：OCR端到端识别任务中荣获一等奖，B榜端到端识别精度相比PP-OCRv4提升2.5%，推理速度持平。</td>
    </tr>
</table>

**注：以上精度指标的评估集是 [PaddleOCR算法模型挑战赛 - 赛题一：OCR端到端识别任务](https://aistudio.baidu.com/competition/detail/1131/0/introduction)B榜。 所有模型 GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为8，精度类型为 FP32。**

**公式识别模块模型：**
|模型名称|BLEU score|normed edit distance|ExpRate （%）|GPU推理耗时（ms）|CPU推理耗时（ms）|模型存储大小|
|-|-|-|-|-|-|-|
|LaTeX_OCR_rec|0.8821|0.0823|40.01|-|-|89.7 M|

**注：以上精度指标测量自 [LaTeX-OCR公式识别测试集](https://drive.google.com/drive/folders/13CA4vAmOmD_I_dSbvLp-Lf0s6KiaNfuO)。以上所有模型 GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为8，精度类型为 FP32。**


**印章文本检测模块模型：**

|模型|检测Hmean（%）|GPU推理耗时（ms）|CPU推理耗时 (ms)|模型存储大小（M)|介绍|
|-|-|-|-|-|-|
|PP-OCRv4_server_seal_det|98.21|84.341|2425.06|109|PP-OCRv4的服务端印章文本检测模型，精度更高，适合在较好的服务器上部署|
|PP-OCRv4_mobile_seal_det|96.47|10.5878|131.813|4.6|PP-OCRv4的移动端印章文本检测模型，效率更高，适合在端侧部署|

**注：以上精度指标的评估集是自建的数据集，包含500张圆形印章图像。GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为 8，精度类型为 FP32。**

**文本图像矫正模块模型：**

|模型|MS-SSIM （%）|模型存储大小（M)|介绍|
|-|-|-|-|
|UVDoc|54.40|30.3 M|高精度文本图像矫正模型|

**模型的精度指标测量自 [DocUNet benchmark](https://www3.cs.stonybrook.edu/~cvl/docunet.html)。**

**文档图像方向分类模块模型：**

|模型|Top-1 Acc（%）|GPU推理耗时（ms）|CPU推理耗时 (ms)|模型存储大小（M)|介绍|
|-|-|-|-|-|-|
|PP-LCNet_x1_0_doc_ori|99.06|3.84845|9.23735|7|基于PP-LCNet_x1_0的文档图像分类模型，含有四个类别，即0度，90度，180度，270度|

**注：以上精度指标的评估集是自建的数据集，覆盖证件和文档等多个场景，包含 1000 张图片。GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为 8，精度类型为 FP32。**

</details>

****

## 2. 快速开始
PaddleX 所提供的预训练的模型产线均可以快速体验效果，你可以在线体验通用图像分类产线的效果，也可以在本地使用命令行或 Python 体验通用图像分类产线的效果。

在本地使用通用版面解析产线前，请确保您已经按照[PaddleX本地安装教程](../../../installation/installation.md)完成了PaddleX的wheel包安装。

### 2.1 命令行方式体验
一行命令即可快速体验版面解析产线效果，使用 [测试文件](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/demo_paper.png)，并将 `--input` 替换为本地路径，进行预测

```
paddlex --pipeline layout_parsing --input demo_paper.png --device gpu:0
```
参数说明：

```
--pipeline：产线名称，此处为版面解析产线
--input：待处理的输入图片的本地路径或URL
--device 使用的GPU序号（例如gpu:0表示使用第0块GPU，gpu:1,2表示使用第1、2块GPU），也可选择使用CPU（--device cpu）
```

在执行上述 Python 脚本时，加载的是默认的版面解析产线配置文件，若您需要自定义配置文件，可执行如下命令获取：

<details>
   <summary> 👉点击展开</summary>

```
paddlex --get_pipeline_config layout_parsing
```
执行后，版面解析产线配置文件将被保存在当前路径。若您希望自定义保存位置，可执行如下命令（假设自定义保存位置为 `./my_path` ）：

```
paddlex --get_pipeline_config layout_parsing --save_path ./my_path
```

获取产线配置文件后，可将 `--pipeline` 替换为配置文件保存路径，即可使配置文件生效。例如，若配置文件保存路径为 `./layout_parsing.yaml`，只需执行：

```
paddlex --pipeline ./layout_parsing.yaml --input layout_parsing.jpg
```
其中，`--model`、`--device` 等参数无需指定，将使用配置文件中的参数。若依然指定了参数，将以指定的参数为准。

</details>

运行后，得到的结果为：

<details>
   <summary> 👉点击展开</summary>

```
{'input_path': PosixPath('/root/.paddlex/temp/tmp5jmloefs.png'), 'parsing_result': [{'input_path': PosixPath('/root/.paddlex/temp/tmpshsq8_w0.png'), 'layout_bbox': [51.46833, 74.22329, 542.4082, 232.77504], 'image': {'img': array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [213, 221, 238],
        [217, 223, 240],
        [233, 234, 241]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]]], dtype=uint8), 'image_text': ''}, 'layout': 'single'}, {'input_path': PosixPath('/root/.paddlex/temp/tmpcd2q9uyu.png'), 'layout_bbox': [47.68295, 243.08054, 546.28253, 295.71045], 'figure_title': 'Overview of RT-DETR, We feed th', 'layout': 'single'}, {'input_path': PosixPath('/root/.paddlex/temp/tmpr_iqa8b3.png'), 'layout_bbox': [58.416977, 304.1531, 275.9134, 400.07513], 'image': {'img': array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]]], dtype=uint8), 'image_text': ''}, 'layout': 'left'}, {'input_path': PosixPath('/root/.paddlex/temp/tmphpblxl3p.png'), 'layout_bbox': [100.62961, 405.97458, 234.79774, 414.77414], 'figure_title': 'Figure 5. The fusion block in CCFF.', 'layout': 'left'}, {'input_path': PosixPath('/root/.paddlex/temp/tmplgnczrsf.png'), 'layout_bbox': [47.81724, 421.9041, 288.01566, 550.538], 'text': 'D, Ds, not only significantly reduces latency (35% faster),\nRut\nnproves accuracy (0.4% AP higher), CCFF is opti\nased on the cross-scale fusion module, which\nnsisting of convolutional lavers intc\npath.\nThe role of the fusion block is t\n into a new feature, and its\nFigure 5. The f\nblock contains tw\n1 x1\nchannels, /V RepBlock\n. anc\n: two-path outputs are fused by element-wise add. We\ntormulate the calculation ot the hvbrid encoder as:', 'layout': 'left'}, {'input_path': PosixPath('/root/.paddlex/temp/tmpsq0ey9md.png'), 'layout_bbox': [94.60716, 558.703, 288.04193, 600.19434], 'formula': '\\begin{array}{l}{{\\Theta=K=\\mathrm{p.s.sp{\\pm}}\\mathrm{i.s.s.}(\\mathrm{l.s.}(\\mathrm{l.s.}(\\mathrm{l.s.}}),{\\qquad\\mathrm{{a.s.}}\\mathrm{s.}}}\\\\ {{\\tau_{\\mathrm{{s.s.s.s.s.}}(\\mathrm{l.s.},\\mathrm{l.s.},\\mathrm{s.s.}}\\mathrm{s.}\\mathrm{s.}}\\end{array}),}}\\\\ {{\\bar{\\mathrm{e-c.c.s.s.}(\\mathrm{s.},\\mathrm{s.s.},\\ s_{s}}\\mathrm{s.s.},\\tau),}}\\end{array}', 'layout': 'left'}, {'input_path': PosixPath('/root/.paddlex/temp/tmpv30qy0v4.png'), 'layout_bbox': [47.975555, 607.12024, 288.5776, 629.1252], 'text': 'tened feature to the same shape as Ss.\nwhere Re shape represents restoring the shape of the flat-', 'layout': 'left'}, {'input_path': PosixPath('/root/.paddlex/temp/tmp0jejzwwv.png'), 'layout_bbox': [48.383354, 637.581, 245.96404, 648.20496], 'paragraph_title': '4.3. Uncertainty-minimal Query Selection', 'layout': 'left'}, {'input_path': PosixPath('/root/.paddlex/temp/tmpushex416.png'), 'layout_bbox': [47.80134, 656.002, 288.50192, 713.24994], 'text': 'To reduce the difficulty of optimizing object queries in\nDETR, several subsequent works [42, 44, 45] propose query\nselection schemes, which have in common that they use the\nconfidence score to select the top K’ features from the en-\ncoder to initialize object queries (or just position queries).', 'layout': 'left'}, {'input_path': PosixPath('/root/.paddlex/temp/tmpki7e_6wc.png'), 'layout_bbox': [306.6371, 302.1026, 546.3772, 419.76724], 'text': 'The confidence score represents the likelihood that the fea\nture includes foreground objects. Nevertheless, the \nare required to simultaneously model the category\nojects, both of which determine the quality of the\npertor\ncore of the fes\nBased on the analysis, the current query\n considerable level of uncertainty in the\nresulting in sub-optimal initialization for\nand hindering the performance of the detector.', 'layout': 'right'}, {'input_path': PosixPath('/root/.paddlex/temp/tmppbxrfehp.png'), 'layout_bbox': [306.0642, 422.7347, 546.9216, 539.45734], 'text': 'To address this problem, we propose the uncertainty mini\nmal query selection scheme, which explicitly const\noptim\n the epistemic uncertainty to model the\nfeatures, thereby providing \nhigh-quality\nr the decoder. Specifically,\n the discrepancy between i\nalization P\nand classificat\n.(2\ntunction for the gradie', 'layout': 'right'}, {'input_path': PosixPath('/root/.paddlex/temp/tmp1mgiyd21.png'), 'layout_bbox': [331.52808, 549.32635, 546.5229, 586.15546], 'formula': '\\begin{array}{c c c}{{}}&{{}}&{{\\begin{array}{c}{{i\\langle X\\rangle=({\\bar{Y}}({\\bar{X}})+{\\bar{Z}}({\\bar{X}})\\mid X\\in{\\bar{\\pi}}^{\\prime}}}&{{}}\\\\ {{}}&{{}}&{{}}\\end{array}}}&{{\\emptyset}}\\\\ {{}}&{{}}&{{C(\\bar{X},{\\bar{X}})=C..\\scriptstyle(\\bar{0},{\\bar{Y}})+{\\mathcal{L}}_{{\\mathrm{s}}}({\\bar{X}}),\\ 6)}}&{{}}\\end{array}', 'layout': 'right'}, {'input_path': PosixPath('/root/.paddlex/temp/tmp8t73dpym.png'), 'layout_bbox': [306.44016, 592.8762, 546.84314, 630.60126], 'text': 'where  and y denote the prediction and ground truth,\n= (c, b), c and b represent the category and bounding\nbox respectively, X represent the encoder feature.', 'layout': 'right'}, {'input_path': PosixPath('/root/.paddlex/temp/tmpftnxeyjm.png'), 'layout_bbox': [306.15652, 632.3142, 546.2463, 713.19073], 'text': 'Effectiveness analysis. To analyze the effectiveness of the\nuncertainty-minimal query selection, we visualize the clas-\nsificatior\nscores and IoU scores of the selected fe\nCOCO\na 12017, Figure 6. We draw the scatterplo\nt with\ndots\nrepresent the selected features from the model trained\nwith uncertainty-minimal query selection and vanilla query', 'layout': 'right'}]}
```
</details>

版面解析暂不支持保存解析后可视化图片，相关功能支持中，您可以通过 `--save_path` 自定义保存路径，随后结构化的json结果将被保存在指定路径下。

### 2.2 Python脚本方式集成
几行代码即可完成产线的快速推理，以通用版面解析产线为例：

```python
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="layout_parsing")

output = pipeline.predict("demo_paper.png")
for res in output:
    res.print() ## 打印预测的结构化输出
    res.save_to_img("./output/") ## 保存img格式结果
    res.save_to_xlsx("./output/") ## 保存表格格式结果
    res.save_to_html("./output/") ## 保存html结果
```
得到的结果与命令行方式相同。

在上述 Python 脚本中，执行了如下几个步骤：

（1）实例化 `create_pipeline` 实例化产线对象：具体参数说明如下：

|参数|参数说明|参数类型|默认值|
|-|-|-|-|
|`pipeline`|产线名称或是产线配置文件路径。如为产线名称，则必须为 PaddleX 所支持的产线。|`str`|无|
|`device`|产线模型推理设备。支持：“gpu”，“cpu”。|`str`|`gpu`|
|`use_hpip`|是否启用高性能推理，仅当该产线支持高性能推理时可用。|`bool`|`False`|

（2）调用产线对象的 `predict` 方法进行推理预测：`predict` 方法参数为`x`，用于输入待预测数据，支持多种输入方式，具体示例如下：

| 参数类型      | 参数说明                                                                                                  |
|---------------|-----------------------------------------------------------------------------------------------------------|
| Python Var    | 支持直接传入Python变量，如numpy.ndarray表示的图像数据。                                               |
| str         | 支持传入待预测数据文件路径，如图像文件的本地路径：`/root/data/img.jpg`。                                   |
| str           | 支持传入待预测数据文件URL，如图像文件的网络URL：[示例](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/demo_paper.png)。|
| str           | 支持传入本地目录，该目录下需包含待预测数据文件，如本地路径：`/root/data/`。                               |
| dict          | 支持传入字典类型，字典的key需与具体任务对应，如图像分类任务对应\"img\"，字典的val支持上述类型数据，例如：`{\"img\": \"/root/data1\"}`。|
| list          | 支持传入列表，列表元素需为上述类型数据，如`[numpy.ndarray, numpy.ndarray]，[\"/root/data/img1.jpg\", \"/root/data/img2.jpg\"]`，`[\"/root/data1\", \"/root/data2\"]`，`[{\"img\": \"/root/data1\"}, {\"img\": \"/root/data2/img.jpg\"}]`。|

（3）调用`predict`方法获取预测结果：`predict` 方法为`generator`，因此需要通过调用获得预测结果，`predict`方法以batch为单位对数据进行预测，因此预测结果为list形式表示的一组预测结果。

（4）对预测结果进行处理：每个样本的预测结果均为`dict`类型，且支持打印，或保存为文件，支持保存的类型与具体产线相关，如：


|方法|说明|方法参数|
|-|-|-|
|save_to_img|将结果保存为img格式的文件|`- save_path`：str类型，保存的文件路径，当为目录时，保存文件命名与输入文件类型命名一致；|
|save_to_html|将结果保存为html格式的文件|`- save_path`：str类型，保存的文件路径，当为目录时，保存文件命名与输入文件类型命名一致；|
|save_to_xlsx|将结果保存为表格格式的文件|`- save_path`：str类型，保存的文件路径，当为目录时，保存文件命名与输入文件类型命名一致；|

其中，`save_to_img` 能够保存可视化结果（包括OCR结果图片、版面分析结果图片、表格结构识别结果图片）， `save_to_html` 能够将表格直接保存为html文件（包括文本和表格格式），`save_to_xlsx` 能够将表格保存为Excel格式文件（包括文本和格式）。

若您获取了配置文件，即可对版面解析产线各项配置进行自定义，只需要修改 `create_pipeline` 方法中的 `pipeline` 参数值为产线配置文件路径即可。

例如，若您的配置文件保存在 `./my_path/layout_parsing.yaml` ，则只需执行：

```python
from paddlex import create_pipeline
pipeline = create_pipeline(pipeline="./my_path/layout_parsing.yaml")
output = pipeline.predict("layout_parsing.jpg")
for res in output:
    res.print() ## 打印版面解析预测的结构化输出
    res.save_to_img("./output/") ## 保存产线各个子模块的img格式结果
    res.save_to_xlsx("./output/") ## 保存表格识别模块的的xlsx格式结果
    res.save_to_html("./output/") ## 保存表格识别模块的html结果
```
## 3. 开发集成/部署
如果产线可以达到您对产线推理速度和精度的要求，您可以直接进行开发集成/部署。

若您需要将产线直接应用在您的Python项目中，可以参考 [2.2 Python脚本方式](#22-python脚本方式集成)中的示例代码。

此外，PaddleX 也提供了其他三种部署方式，详细说明如下：

🚀 **高性能推理**：在实际生产环境中，许多应用对部署策略的性能指标（尤其是响应速度）有着较严苛的标准，以确保系统的高效运行与用户体验的流畅性。为此，PaddleX 提供高性能推理插件，旨在对模型推理及前后处理进行深度性能优化，实现端到端流程的显著提速，详细的高性能推理流程请参考[PaddleX高性能推理指南](../../../pipeline_deploy/high_performance_inference.md)。

☁️ **服务化部署**：服务化部署是实际生产环境中常见的一种部署形式。通过将推理功能封装为服务，客户端可以通过网络请求来访问这些服务，以获取推理结果。PaddleX 支持用户以低成本实现产线的服务化部署，详细的服务化部署流程请参考[PaddleX服务化部署指南](../../../pipeline_deploy/service_deploy.md)。

下面是API参考和多语言服务调用示例：

<details>
<summary>API参考</summary>

对于服务提供的所有操作：

- 响应体以及POST请求的请求体均为JSON数据（JSON对象）。
- 当请求处理成功时，响应状态码为`200`，响应体的属性如下：

    |名称|类型|含义|
    |-|-|-|
    |`errorCode`|`integer`|错误码。固定为`0`。|
    |`errorMsg`|`string`|错误说明。固定为`"Success"`。|

    响应体还可能有`result`属性，类型为`object`，其中存储操作结果信息。

- 当请求处理未成功时，响应体的属性如下：

    |名称|类型|含义|
    |-|-|-|
    |`errorCode`|`integer`|错误码。与响应状态码相同。|
    |`errorMsg`|`string`|错误说明。|

服务提供的操作如下：

- **`infer`**

    进行版面解析。

    `POST /layout-parsing`

    - 请求体的属性如下：

        |名称|类型|含义|是否必填|
        |-|-|-|-|
        |`file`|`string`|服务可访问的图像文件或PDF文件的URL，或上述类型文件内容的Base64编码结果。对于超过10页的PDF文件，只有前10页的内容会被使用。|是|
        |`fileType`|`integer`|文件类型。`0`表示PDF文件，`1`表示图像文件。若请求体无此属性，则服务将尝试根据URL自动推断文件类型。|否|
        |`useImgOrientationCls`|`boolean`|是否启用文档图像方向分类功能。默认启用该功能。|否|
        |`useImgUnwrapping`|`boolean`|是否启用文本图像矫正功能。默认启用该功能。|否|
        |`useSealTextDet`|`boolean`|是否启用印章文本检测功能。默认启用该功能。|否|
        |`inferenceParams`|`object`|推理参数。|否|

        `inferenceParams`的属性如下：

        |名称|类型|含义|是否必填|
        |-|-|-|-|
        |`maxLongSide`|`integer`|推理时，若文本检测模型的输入图像较长边的长度大于`maxLongSide`，则将对图像进行缩放，使其较长边的长度等于`maxLongSide`。|否|

    - 请求处理成功时，响应体的`result`具有如下属性：

        |名称|类型|含义|
        |-|-|-|
        |`layoutParsingResults`|`array`|版面解析结果。数组长度为1（对于图像输入）或文档页数与10中的较小者（对于PDF输入）。对于PDF输入，数组中的每个元素依次表示PDF文件中每一页的处理结果。|

        `layoutParsingResults`中的每个元素为一个`object`，具有如下属性：

        |名称|类型|含义|
        |-|-|-|
        |`layoutElements`|`array`|版面元素信息。|

        `layoutElements`中的每个元素为一个`object`，具有如下属性：

        |名称|类型|含义|
        |-|-|-|
        |`bbox`|`array`|版面元素位置。数组中元素依次为边界框左上角x坐标、左上角y坐标、右下角x坐标以及右下角y坐标。|
        |`label`|`string`|版面元素标签。|
        |`text`|`string`|版面元素包含的文本。|
        |`layoutType`|`string`|版面元素排列方式。|
        |`image`|`string`|版面元素图像，JPEG格式，使用Base64编码。|

</details>

<details>
<summary>多语言调用服务示例</summary>

<details>
<summary>Python</summary>

```python
import base64
import requests

API_URL = "http://localhost:8080/layout-parsing" # 服务URL

# 对本地图像进行Base64编码
with open(image_path, "rb") as file:
    image_bytes = file.read()
    image_data = base64.b64encode(image_bytes).decode("ascii")

payload = {
    "file": image_data, # Base64编码的文件内容或者文件URL
    "fileType": 1,
    "useImgOrientationCls": True,
    "useImgUnwrapping": True,
    "useSealTextDet": True,
}

# 调用API
response = requests.post(API_URL, json=payload)

# 处理接口返回数据
assert response.status_code == 200
result = response.json()["result"]
print("\nDetected layout elements:")
for res in result["layoutParsingResults"]:
    for ele in res["layoutElements"]:
        print("===============================")
        print("bbox:", ele["bbox"])
        print("label:", ele["label"])
        print("text:", repr(ele["text"]))
```

</details>
</details>
<br/>

📱 **端侧部署**：端侧部署是一种将计算和数据处理功能放在用户设备本身上的方式，设备可以直接处理数据，而不需要依赖远程的服务器。PaddleX 支持将模型部署在 Android 等端侧设备上，详细的端侧部署流程请参考[PaddleX端侧部署指南](../../../pipeline_deploy/edge_deploy.md)。
您可以根据需要选择合适的方式部署模型产线，进而进行后续的 AI 应用集成。

## 4. 二次开发
如果通用版面解析产线提供的默认模型权重在您的场景中，精度或速度不满意，您可以尝试利用**您自己拥有的特定领域或应用场景的数据**对现有模型进行进一步的**微调**，以提升通用版面解析产线的在您的场景中的识别效果。

### 4.1 模型微调
由于通用版面解析产线包含7个模块，模型产线的效果不及预期可能来自于其中任何一个模块。

您可以对识别效果差的图片进行分析，参考如下规则进行分析和模型微调：

* 检测到的表格结构错误（如行列识别错误、单元格位置错误），那么可能是表格结构识别模块存在不足，您需要参考[表格结构识别模块开发教程](../../../module_usage/tutorials/ocr_modules/table_structure_recognition.md)中的**二次开发**章节，使用您的私有数据集对表格结构识别模型进行微调。
* 版面中存在定位错误（例如对表格、印章的位置识别错误），那么可能是版面区域定位模块存在不足，您需要参考[版面区域检测模块开发教程](../../../module_usage/tutorials/ocr_modules/layout_detection.md)中的**二次开发**章节，使用您的私有数据集对版面区域定位模型进行微调。
* 有较多的文本未被检测出来（即文本漏检现象），那么可能是文本检测模型存在不足，您需要参考[文本检测模块开发教程](../../../module_usage/tutorials/ocr_modules/text_detection.md)中的**二次开发**章节，使用您的私有数据集对文本检测模型进行微调。
* 已检测到的文本中出现较多的识别错误（即识别出的文本内容与实际文本内容不符），这表明文本识别模型需要进一步改进，您需要参考[文本识别模块开发教程](../../../module_usage/tutorials/ocr_modules/text_recognition.md)中的**二次开发**章节对文本识别模型进行微调。
* 已检测到的印章文本出现较多的识别错误，这表明印章文本检测模块模型需要进一步改进，您需要参考[印章文本检测模块开发教程](../../../module_usage/tutorials/ocr_modules/)中的**二次开发**章节对印章文本检测模型进行微调。
* 已检测到的公式中出现较多的识别错误（即识别出的公式内容与实际公式内容不符），这表明公式识别模型需要进一步改进，您需要参考[公式识别模块开发教程](../../../module_usage/tutorials/ocr_modules/formula_recognition.md)中的中的[二次开发](../../../module_usage/tutorials/ocr_modules/formula_recognition.md#四二次开发)章节,对公式识别模型进行微调。
* 含文字区域的文档或证件的方向存在较多的识别错误，这表明文档图像方向分类模型需要进一步改进，您需要参考[文档图像方向分类模块开发教程](../../../module_usage/tutorials/ocr_modules/doc_img_orientation_classification.md)中的**二次开发**章节对文档图像方向分类模型进行微调。

### 4.2 模型应用
当您使用私有数据集完成微调训练后，可获得本地模型权重文件。

若您需要使用微调后的模型权重，只需对产线配置文件做修改，将微调后模型权重的本地路径替换至产线配置文件中的对应位置即可：

```python
......
 Pipeline:
  layout_model: PicoDet_layout_1x  #可修改为微调后模型的本地路径
  table_model: SLANet_plus  #可修改为微调后模型的本地路径
  text_det_model: PP-OCRv4_server_det  #可修改为微调后模型的本地路径
  text_rec_model: PP-OCRv4_server_rec  #可修改为微调后模型的本地路径
  formula_rec_model: LaTeX_OCR_rec  #可修改为微调后模型的本地路径
  seal_text_det_model: PP-OCRv4_server_seal_det   #可修改为微调后模型的本地路径
  doc_image_unwarp_model: UVDoc  #可修改为微调后模型的本地路径
  doc_image_ori_cls_model: PP-LCNet_x1_0_doc_ori  #可修改为微调后模型的本地路径
  layout_batch_size: 1
  text_rec_batch_size: 1
  table_batch_size: 1
  device: "gpu:0"
......
```
随后， 参考本地体验中的命令行方式或 Python 脚本方式，加载修改后的产线配置文件即可。

##  5. 多硬件支持
PaddleX 支持英伟达 GPU、昆仑芯 XPU、昇腾 NPU和寒武纪 MLU 等多种主流硬件设备，**仅需修改 `--device` 参数**即可完成不同硬件之间的无缝切换。

例如，您使用英伟达 GPU 进行版面解析产线的推理，使用的 Python 命令为：

```
paddlex --pipeline layout_parsing --input layout_parsing.jpg --device gpu:0
```
此时，若您想将硬件切换为昇腾 NPU，仅需对 Python 命令中的 `--device` 修改为npu 即可：

```
paddlex --pipeline layout_parsing --input layout_parsing.jpg --device npu:0
```
若您想在更多种类的硬件上使用通用版面解析产线，请参考[PaddleX多硬件使用指南](../../../other_devices_support/multi_devices_use_guide.md)。
