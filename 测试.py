# 对vgg16_bn先生成秩，再main.py训练，再测参数量，再测精度
python rank_generation.py --resume /Lun2/great99/HRank-master/pretrained_model/vgg_16_bn.pt --arch vgg_16_bn --limit 128 (秩只要生成一次！！！)
python main.py  --job_dir /Lun2/great99/HRank-master/rank_conv/vgg_16_bn --resume /Lun2/great99/HRank-master/pretrained_model/vgg_16_bn.pt --dataset cifar10  --arch vgg_16_bn --compress_rate [0.95]+[0.5]*6+[0.95]*6
python cal_flops_params.py --arch vgg_16_bn --compress_rate [0.95]+[0.5]*6+[0.95]*6
python evaluate.py --dataset cifar10  --test_model_dir /Lun2/great99/HRank-master/rank_conv/vgg_16_bn --arch vgg_16_bn


#不用生成秩了，秩只需要生成一次
#所以只有main.py,evaluate.py,cal_flops_params.py
python main.py  --job_dir /Lun2/great99/HRank-master/rank_conv/resnet_56_limit128 --resume /Lun2/great99/HRank-master/pretrained_model/resnet_56.pt.pt --dataset cifar10  --arch resnet_56 --compress_rate [0.1]+[0.60]*35+[0.2]+[0.6]+[0.8]*17
python evaluate.py --dataset cifar10 --data_dir /Lun2/great99/HRank-master/data --test_model_dir /Lun2/great99/HRank-master/rank_conv/resnet_56_limit128 --arch resnet_56
python cal_flops_params.py --arch resnet_56 --compress_rate [0.1]+[0.60]*35+[0.2]+[0.6]+[0.8]*17

#resnet_56最好的剪枝效果：[0.0]+[0.0]*18+[0.5]+[0.75]*17+[0.88]+[0.95]*17，一般resnet_56训8个半小时就行
python main.py  --job_dir /Lun2/great99/HRank-master/rank_conv/resnet_56_limit128 --resume /Lun2/great99/HRank-master/pretrained_model/resnet_56.pt.pt --dataset cifar10  --arch resnet_56 --compress_rate [0.0]+[0.0]*18+[0.5]+[0.75]*17+[0.88]+[0.95]*17
python evaluate.py --dataset cifar10 --data_dir /Lun2/great99/HRank-master/data --test_model_dir /Lun2/great99/HRank-master/rank_conv/resnet_56_limit128 --arch resnet_56
python cal_flops_params.py --arch resnet_56 --compress_rate [0.0]+[0.0]*18+[0.5]+[0.75]*17+[0.88]+[0.95]*17

#换个剪枝率再试
python cal_flops_params.py --arch resnet_110 --compress_rate [0.1]+[0.40]*36+[0.4]*36+[0.7]+[0.85]*35
python main.py  --job_dir /Lun2/great99/HRank-master/rank_conv/resnet_110_limit128 --resume /Lun2/great99/HRank-master/pretrained_model/resnet_110.pt --dataset cifar10  --arch resnet_110 --compress_rate [0.1]+[0.40]*36+[0.4]*36+[0.7]+[0.85]*35
python evaluate.py --dataset cifar10 --data_dir /Lun2/great99/HRank-master/data --test_model_dir /Lun2/great99/HRank-master/rank_conv/resnet_110_limit128 --arch resnet_110
