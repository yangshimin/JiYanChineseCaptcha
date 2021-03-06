## 免责声明
**本项目仅供学习交流使用，请勿用于非法用途，不得在任何商业使用，本人不承担任何法律责任。**
### 极验点选文字验证码训练
![](https://github.com/yangshimin/markdown-img/raw/master/2a4ac8b8da8166609ce70ef8a6d1dd2c.jpg) 
 
### 思路
+ 先采集一批足量的验证码原图, 等待标注
+ 考虑到人工标注太慢, 可以考虑找一个准确率还行的模型就行自动标注. 自动标注的结果可能会有异常，所以还需要大体瞄一眼纠错
+ 每张原图可以标注为三种结果:
     + 原图左下角区域的切割, 左下角区域的大小都是固定的
     + 复制一份原图以 坐标1_坐标2_坐标3_哈希值.jpg的方式保存
     + 对原图识别的文字切割, 按文字种类/xxx.jpg的方式保存 
+ 如果上一步得到的文字种类有点少, 考虑增加样本量; 如果是某个文字类下的样本数量少, 可以用PIL的ImageFont生成样本
+ 对上一步所得到的数据集分别进行训练, 得到三种训练模型 
+ 套娃使用 

### 参考 
+ 采集图片可以参考: [JiYanChineseSelect](https://github.com/yangshimin/JiYanChineseSelect) 
