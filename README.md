# file_batch_rename
python按编号规则批量重命名文件


这个脚本主要是为了针对python脚本按文件名排序时的顺序异常问题

例：有这样一组文件

1.png,2.png,...,12.png.13.png

正常理解排序应该是按1.png,2.png,...,12.png.13.png进行排序,然而python因为字符排序优先级的问题会变成这样：1.png,12.png,13.png,2.png,...（把文件名首位为1的文件排在了2的文件的前面）

使用此脚本处理可以按照一定规格、缺位往前补零的方法进行重命名，例：

0001.png

0002.png

0003.png

...

0011.png

0012.png

0013.png
