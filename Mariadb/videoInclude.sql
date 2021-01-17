
-- 删除
drop table if exists tb_emp;
drop table if exists tb_dept;

-- 创建表
create table tb_dept
(
    dno   int         not null comment '编号',
    dname varchar(10) not null comment '名称',
    dloc  varchar(20) not null comment '所在地',
    primary key (dno)
);
-- 批量插入
insert into tb_dept
values (10, '会计部', '北京'),
       (20, '研发部', '成都'),
       (30, '销售部', '重庆'),
       (40, '运维部', '深圳');

create table tb_emp
(
    eno   int         not null comment '员工编号',
    ename varchar(20) not null comment '员工姓名',
    job   varchar(20) not null comment '员工职位',
    mgr   int comment '主管编号',
    sal   int         not null comment '员工月薪',
    comm  int comment '每月补贴',
    dno   int comment '所在部门编号',
    primary key (eno)
);

-- 外键自参照
alter table tb_emp
    add constraint fk_emp_mgr foreign key (mgr) references tb_emp (eno);

-- 外键添加
alter table tb_emp
    add constraint fk_emp_dno foreign key (dno) references tb_dept (dno);


-- 增加列到指定位置

-- 批量添加
insert into tb_emp
values (7800, '张三丰', '总裁', null, 9000, 1200, 20),
       (2056, '乔峰', '分析师', 7800, 5000, 1500, 20),
       (3088, '李莫愁', '设计师', 2056, 3500, 800, 20),
       (3211, '张无忌', '程序员', 2056, 3500, 800, 20),
       (3233, '丘处机', '程序员', 2056, 3200, null, 20),
       (3251, '张翠山', '程序员', 2056, 4000, null, 20),
       (5566, '宋远桥', '会计师', 7800, 4000, 1000, 10),
       (5234, '郭靖', '出纳', 5566, 2000, null, 10),
       (3344, '黄蓉', '销售主管', 7800, 3000, 800, 30),
       (1359, '胡一刀', '销售员', 3344, 1800, 200, 30),
       (4466, '苗人凤', '销售员', 3344, 2500, null, 30),
       (3244, '欧阳锋', '程序员', 3088, 3200, null, 20),
       (3577, '杨过', '会计', 5566, 2200, null, 10),
       (3588, '朱九真', '会计', 5566, 250, null, 10);

select * from tb_emp;
select * from tb_dept;

-- 查询薪资做高的员工姓名和工资
select ename,sal,max(sal) as 最高工资 from tb_emp order by ename,sal;

-- 查询员工的姓名和年薪((月薪+补贴)*12) 处理空值问题
-- ifnull(total[别名],0) count(dno) as total

-- 查询有员工的部门的编号和人数


-- 查询所有部门的名称和人数

-- 查询有员工的部门的编号和人数

-- 查询所有部门的名称和人数

-- 查询薪资最高的员工(Boss除外)的姓名和工资

--  查询主管的姓名和职位
-- 通常不推荐使用 in 或者 not in 集合运算和 distinct 去重操作
-- 可以考虑用 exists 或者 not exists 替代集合运算和去重操作


-- 查询月薪排名 4~6 的员工新名和工资


### 执行计划
-- 生成执行计划
explain select ename,eno from tb_emp where eno=7800;
explain select ename,eno from tb_emp where ename ='张三丰';



-- index 索引
-- 创建索引
/*
索引可以加速查询索引应该在经常用于查询筛选条件的列上建立索引
索引会使用额外的存储空间而且会让增删改变得更慢(因为要更新索引)

所以不能滥用索引
*/
-- create index index-name on table-name(key);
create index idx_emp_ename on tb_emp(ename);
-- 删除索引
drop index idx_emp_ename on tb_emp;


-- 视图
-- 创建视图
create view view_emp_dept as select ename,t1.dno from tb_emp t1 inner join tb_dept td on t1.dno = td.dno;

-- 使用视图  访问控制
select * from view_emp_dept;

-- 删除视图
drop view view_emp_dept;


-- 存储过程
delimiter $$

-- 创建存储过程
create procedure  sp_dept_avg_Sal(deptno int,out avgsal float)
begin
        select  avg(sal) into  avgsal from tb_emp where dno=deptno;
end $$

-- 将定界符还原回;
delimiter ;
-- 删除存储过程
drop procedure sp_dept_avg_Sal;


-- 调用存储过程
select @a;
call sp_dept_avg_Sal(20,@a);

-- 触发器
-- 在执行增删改查的操作是可以触发其他联级操作,但是有可能导致“锁表”现象,实际开发中应该尽量避免使用触发器


-- DCL: 授予权限(grant to) 和召回权限(revoke from)
-- 创建用户

/*
-- 登陆方式: 3
    1. localhost 登录: create  user 'UserName'@'localhost' identified by 'yourpassword';
    2. 指定服务器(修改为自己服务器公网 IP) : create  user 'UserName'@'127.0.0.1' identified by 'yourpassword';
    3. 任意地方登录: create  user 'UserName'@'%' identified by 'yourpassword';
*/
-- 创建用户
    create  user 'UserName'@'localhost' identified by 'yourpassword';
    create  user 'UserName'@'127.0.0.1' identified by 'yourpassword';
    create  user 'UserName'@'%' identified by 'yourpassword';
-- 删除用户 一一对应
    drop user 'UserName'@'localhost';

-- 权限 Oracle--> dba 权限
-- 授予数据库所有的权限 给用户 ···
grant all privileges on databases-name.* to 'user-name'@'address';
-- 权限收回
-- revoke  收回什么权限 on 在那个数据 to 的哪个用户;
-- 收回增删改的权限 'user-name'@'address';
revoke select,update,delete on database-name.* to 'user-name'@'address';

-- 事务 (transaction) - 把多个增删改查的操作做成不可分割的原子性操作
-- 要么全部都做,要么全部做
-- 开启事务两种方法:
    -- 1.begin ;
    -- 2. start transaction;

-- 插入测试数据
insert into tb_emp(eno, ename,job,sal) values (7900,'张三','吃瓜群众',1200);
-- 查询测试数据
select * from tb_emp;
-- 开启事务
start transaction;
-- 删除数据
delete from tb_emp where eno=7900;

-- 再次查询
select * from tb_emp;
-- 提交(事务中的所有操作全都不生效)
commit;
-- 回滚(事务中的所有操作全部撤销)
rollback;
