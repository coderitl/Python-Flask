/*

具体表象: 用二维表来保存数据
    ~ 行: 一条记录
    ~ 列: 一个字段(某个属性)
    ~ 主键列: 能够唯一标识一条记录的列

编程语言: SQL 结构化查询语言
    ~ DDL: 数据定义语言 create / drop / alter
    ~ DML: 数据操作语言 insert / delete / update / select
    ~ DCL: 数据控制语言 grant / revoke

*/

-- 创建名为 school 的数据库并指定默认的字符集为 utf8
create database school default charset utf8;


-- 查询当前用户
select user();

-- 如果存在名为 school 的数据库就删除它
drop database if exists school;


-- 创建表 student
-- ? / help 终端执行
-- 普通创建表加注释
create table student
(
    stu_id      int primary key not null, -- 学生学号
    stu_name    nvarchar(6)     not null, -- 学生姓名
    stu_email   nvarchar(20)    not null, -- 学生邮箱
    stu_address nvarchar(20)              -- 学生住址
);

-- 优化创建表
create table tb_student
(
    stuid      int(100) not null comment '学号',
    stuname    nvarchar(20) comment '姓名',
    stusex     bit default 1 comment '性别',
    stubirth   date,
    stuemail   nvarchar(20) comment '邮箱',
    stuaddress nvarchar(20) comment '住址',
    primary key (stuid)
);

-- 显示表结构
desc student;
desc tb_student;

-- 查询表 student
select *
from student;

-- 插入相关信息
insert into student value (20201, 'name-01', '202101name01@qq.com', 'name-a', 1);
insert into student value (20202, 'name-02', '202101name02@qq.com', 'name-b', 1);
insert into student value (20203, 'name-03', '202101name03@qq.com', 'name-c', 1);
insert into student value (20204, 'name-04', '202101name04@qq.com', 'name-d', 1);
insert into student value (20205, 'name-05', '202101name05@qq.com', 'name-e', 1);
insert into student value (20206, 'name-06', '202101name06@qq.com', 'name-f', 1);
insert into student value (20207, 'name-07', '202101name07@qq.com', 'name-g', 1);
insert into student value (20208, 'name-08', '202101name08@qq.com', 'name-h', 1);
insert into student value (20209, 'name-09', '202101name09@qq.com', 'name-i', 1);


-- 修改列的数据长度 (创建表时忘记字段长度)
alter table student
    modify column stu_id int(10);

alter table student
    modify column stu_name nvarchar(20);



-- 增加列
alter table student
    add column stu_sex bit default 1;

-- 如果存在就删除学生表
drop table if exists student;
drop table if exists tb_student;

-- 根据条件删除
delete
from student
where stu_id = 20201;



-- 删除列
alter table student
    drop column stu_sex;

-- 重命名列: 可以修改数据类型的大小
alter table student
    change column stu_name stu_name varchar(21);

-- 增删改查
insert into student
values ();
delete
from student
where stu_name = '';
-- 更新多个使用逗号分割
update student
set student.stu_name = ''
where student.stu_name = '';
select *
from student;

-- 添加外键约束，使两个表有关联
alter table
    table- name [表名称] add constraint fk_tablename_foreignKeyName[外键名称]
    foreign key (keyname[关联表的主键]) references
    table - name (keyname[关联表的主键])

-- 唯一性约束
alter table table- name [表名称] add constraint
    uni_tablename_value1_value2[唯一性约束名称,由那两个属性组成唯一]
    unique (value1,value2);

-- 投影和别名
-- 投影
select stu_id, stu_name, stu_id from student;
-- 别名
select stu_id as '学号',stu_name as '姓名' from student;


-- 添加列 stu_sex
    alter table student add column stu_sex bit default 1 comment '性别';

-- 更新数据  默认数据 bit 0--> 男  1--> 女
    update student set stu_sex=0 where stu_id = 20201;
    update student set stu_sex=1 where stu_id = 20202;
    update student set stu_sex=1 where stu_id = 20203;
    update student set stu_sex=0 where stu_id = 20204;
    update student set stu_sex=0 where stu_id = 20205;
    update student set stu_sex=0 where stu_id = 20206;
    update student set stu_sex=1 where stu_id = 20207;
    update student set stu_sex=0 where stu_id = 20208;
    update student set stu_sex=1 where stu_id = 20209;

-- case when end 使用
select stu_id,stu_name, case stu_sex  when 1 then  '男' else '女'  end as '性别'  from student;
-- 其他数据库不通用方法
select stu_id,stu_name,stu_address, if(stu_sex,'男','女') as 性别 from student;

-- and 和 between and
select stu_id,stu_name,if(stu_sex,'男','女') as 性别 from student where stu_id>'20201' and stu_id <'20206';
select stu_id,stu_name,if(stu_sex,'男','女') as 性别 from student where stu_id between 20202 and 20205;

-- 模糊查询
    select stu_id,stu_name from student where stu_name like 'name-%';
    select stu_id,stu_name from student where stu_name like 'name_';
    select stu_id,stu_name from student where stu_name like '%name%';

-- 查询空值
    insert into student(stu_id,stu_email,stu_name) values (20210,'20210@qq.com',null);
-- 空值
    select stu_id,stu_name,stu_email from student where stu_name is  null;
-- 不为空查询
    select stu_id,stu_name,stu_email from student where stu_name is  not null;

-- 去重操作
    insert into student(stu_id,stu_email,stu_name) values (20211,'20211@qq.com',null);
    insert into student(stu_id,stu_email,stu_name) values (20212,'20211@qq.com',null);
    insert into student(stu_id,stu_email,stu_name) values (20213,'20211@qq.com',null);
    insert into student(stu_id,stu_email,stu_name) values (20214,'20211@qq.com',null);
    insert into student(stu_id,stu_email,stu_name) values (20215,'20211@qq.com',null);

-- 查询邮箱重复学员信息 表不合理
select distinct(stu_email),stu_id,stu_name from student where stu_email='20211@qq.com';

-- 排序
    -- 升序
    select stu_id,stu_name,stu_address from student order by stu_id asc;
    -- 降序
    select stu_id,stu_name,stu_address from student  where stu_address is not null order by stu_id desc;


-- 聚合函数 忽略空值 = null
     max()      -- 最大值
     min()      -- 最小值
     average()  -- 平均值
     count()    -- 统计
     sum()      -- 求和

 -- 分组和聚合
    select count(stu_id) from student;
    -- 分组
        -- 统计男生和女生各有多少人
        select if(stu_sex,'男','女') as 性别,count(*) from student group by stu_sex;

-- 筛选 分组 排序
-- where group by order by

-- 什么时候写 having ？
/*
    分组以后的筛选 having
    分组前的筛选 where
*/

-- 子查询