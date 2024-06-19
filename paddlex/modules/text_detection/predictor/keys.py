# copyright (c) 2024 PaddlePaddle Authors. All Rights Reserve.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.




class TextDetKeys(object):
    """
    This class defines a set of keys used for communication of TextDet predictors
    and transforms. Both predictors and transforms accept a dict or a list of
    dicts as input, and they get the objects of their interest from the dict, or
    put the generated objects into the dict, all based on these keys.
    """

    # Common keys
    IMAGE = 'image'
    IM_PATH = 'input_path'
    IM_SIZE = 'original_image_size'
    ORI_IM = 'original_image'
    SHAPE = 'shape'
    PROB_MAP = 'prob_map'
    # Suite-specific keys
    DT_SCORES = 'dt_scores'
    DT_POLYS = 'dt_polys'
    SUB_IMGS = 'sub_imgs'