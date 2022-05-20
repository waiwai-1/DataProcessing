# DataProcessing



### 数据处理的原则

对于txt文件，文件的第一行和第一列分别为列名和行名

对于R语言，我们使用如下的命令

```R
data = read.table('2/M_uyg_dmp.txt', header = TRUE, encoding = 'utf8', sep = '\t', row.names = 1, check.names = FALSE)
```

对于python，我们使用如下命令：

```python
data = pd.read_table('M_uyg_dmp.txt', sep='\t', index_col=0)
```

这两种语言对于默认参数的设置有一些不同，但是通性都是忽略了最左上角的元素。
