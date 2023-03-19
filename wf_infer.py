from mmocr.apis import MMOCRInferencer
ocr = MMOCRInferencer(det='DBNet', rec='SAR')  # Load models into memory
import sys
p_img = sys.argv[1]
ocr(p_img,  out_dir='outputs_wf_infer/', save_pred=True, save_vis=True)



