

def get_center_of_bbox(bbox):
    x1, y1, x2, y2 = bbox
    center = (x1 + x2) / 2, (y1 + y2) / 2
    return center

def get_bbox_width(bbox):
    x1, y1, x2, y2 = bbox
    width = x2 - x1
    return width
