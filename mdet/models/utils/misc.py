
# Copyright (c) OpenMMLab. All rights reserved.
from mdet.structures import SampleList
from mdet.structures.bbox import BaseBoxes

def samplelist_boxtype2tensor(batch_data_samples: SampleList) -> SampleList:
    for data_samples in batch_data_samples:
        if 'gt_instances' in data_samples:
            bboxes = data_samples.gt_instances.get('bboxes', None)
            if isinstance(bboxes, BaseBoxes):
                data_samples.gt_instances.bboxes = bboxes.tensor
        if 'pred_instances' in data_samples:
            bboxes = data_samples.pred_instances.get('bboxes', None)
            if isinstance(bboxes, BaseBoxes):
                data_samples.pred_instances.bboxes = bboxes.tensor
        if 'ignored_instances' in data_samples:
            bboxes = data_samples.ignored_instances.get('bboxes', None)
            if isinstance(bboxes, BaseBoxes):
                data_samples.ignored_instances.bboxes = bboxes.tensor

