# Commit Graph Neo4j数据库设计

## 一. Node

### 1. commit

commit( **sha**, complete, message, commit_date, committer_name， author_name)

sha:	commit结点sha

complete:	文件是否更新完毕

message：		commit提交文本信息

commit_date:	提交时间

committer_name:提交者时间

author_name:作者姓名

### 2. developer

developer(**id**, login, avatar_url, email)

id:	开发者id

login:	开发者昵称

avatar_url:开发者图片

email:开发者邮箱



### 3.tree

tree(**sha**, path_number)

sha:	tree唯一标识



### 4.blob

blob(**sha** , content, size)

sha:	blob唯一标识

content:	blob内容  ?

size:	blob大小



### 5.contribution

contribution(**sha**, addition, deletion, contribute)

sha:	对应commit的sha

addition:	增加的行数

deletion:	减少的行数

contribute:	贡献度（指标）



### 6.deletion

deletion(commit_sha, blob_sha, delete_line)

commit_sha:	删除行对应commit sha

blob_sha:	删除行对应blob sha

delete_beg：	删除对应行数开始

delete_end:	删除对应行数结束 



### 7.addition

addition(commit_sha, blob_sha, addition_line)

commit_sha:	增添对应commit

blob_sha:	增添对应blob

addition_beg:	增加对应行数开始

addition_end:	增加对应行数结束



### 8.line

line(sha, contain, author)

sha:对应blob sha

contain:	本行代码

author:	代码作者id



## 二. Relationship

### 1.parent

(commit1)-[parent]->(commit2)



### 2. child

(commit1)-[child]->(commit2)



### 3.commit2tree

(commit)-[commit2tree]->(tree)



### 4.tree2blob

(tree)-[tree2blob]->(blob)

tree2blob(path)

path:路径



### 5.commit2con

(commit)-[commit2con]->(contribution)



### 6.con2dele

(contribution)-[con2dele]->(deletion)



### 7.con2add

(contribution)-[con2add]->(addition)



### 8.blob2line

(blob)-[blob2line]->(line)

blob2line(line_num)

line_num:代码所在文件中的行数



### 9.line2blob

(line)-[line2blob]->(blob)

line2blob(line_num, blob_sha)

line_num:所在行数

blob_sha:对应blob的sha.



## 10. tree2tree

(tree)-[tree2tree]->(tree)

tree2tree(path)

path:路径

# Issue Neo4j数据库设计



