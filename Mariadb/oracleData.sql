Oracle command:
    Oracle                                  MYSQL
    select table_name from user_tables;     show tables();


Oracle-EMP:
    EMPNO ENAME      JOB              MGR HIREDATE              SAL       COMM     DEPTNO
---------- ---------- --------- ---------- -------------- ---------- ---------- ----------
      7369 SMITH      CLERK           7902 17-12月-80            800                    20
      7499 ALLEN      SALESMAN        7698 20-2月 -81           1600        300         30
      7521 WARD       SALESMAN        7698 22-2月 -81           1250        500         30
      7566 JONES      MANAGER         7839 02-4月 -81           2975                    20
      7654 MARTIN     SALESMAN        7698 28-9月 -81           1250       1400         30
      7698 BLAKE      MANAGER         7839 01-5月 -81           2850                    30
      7782 CLARK      MANAGER         7839 09-6月 -81           2450                    10
      7788 SCOTT      ANALYST         7566 19-4月 -87           3000                    20
      7839 KING       PRESIDENT            17-11月-81           5000                    10
      7844 TURNER     SALESMAN        7698 08-9月 -81           1500          0         30
      7876 ADAMS      CLERK           7788 23-5月 -87           1100                    20
      7900 JAMES      CLERK           7698 03-12月-81            950                    30
      7902 FORD       ANALYST         7566 03-12月-81           3000                    20
      7934 MILLER     CLERK           7782 23-1月 -82           1300                    10

Oracle-DEPT:
        DEPTNO DNAME          LOC
    ---------- -------------- -------------
        10 ACCOUNTING     NEW YORK
        20 RESEARCH       DALLAS
        30 SALES          CHICAGO
        40 OPERATIONS     BOSTON

Oracle-SALGRADE:
         GRADE      LOSAL      HISAL
---------- ---------- ----------
         1        700       1200
         2       1201       1400
         3       1401       2000
         4       2001       3000
         5       3001       9999

-------------------------------------   EMP ----------------------------------------------
 EMPNO                                                                               NOT NULL NUMBER(4)
 ENAME                                                                                        VARCHAR2(10)
 JOB                                                                                          VARCHAR2(9)
 MGR                                                                                          NUMBER(4)
 HIREDATE                                                                                     DATE
 SAL                                                                                          NUMBER(7,2)
 COMM                                                                                         NUMBER(7,2)
 DEPTNO                                                                                       NUMBER(2)


create table emp
(
    empno    int(20) primary key not null comment '员工编号',
    ename    varchar(10) comment '员工姓名',
    job      varchar(9) comment '员工职位',
    mgr      int(4),
    hiredate date,
    sal      int(10),
    comm     int(10),
    deptno   int(2)
);

insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7369,'SMITH','CLERK',7902,'2021-01-16', 800 ,null,20);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7499,'ALLEN','SALESMAN',7698,'2021-01-16', 1600 ,300,30);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7521,'WARD','SALESMAN',7698,'2021-01-16', 1250 ,500,30);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7566,'JONES','MANAGER',7839,'2021-01-16', 2975 ,null,20);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7654,'MARTIN','SALESMAN',7698,'2021-01-16', 1250 ,1400,30);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7698,'BLAKE','MANAGER',7839,'2021-01-16', 2850 ,null,30);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7782,'CLARK','MANAGER',7839,'2021-01-16', 2450 ,null,10);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7788,'SCOTT','ANALYST',7566,'2021-01-16', 3000 ,null,20);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7839,'KING','PRESIDENT',null,'2021-01-16', 5000 ,null,10);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7844,'TURNER','SALESMAN',7698,'2021-01-16', 1500 ,0,30);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7876,'ADAMS','CLERK',7788,'2021-01-16', 1100 ,null,20);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7900,'JAMES','CLERK',7698,'2021-01-16', 950 ,null,30);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7902,'FORD','ANALYST',7566,'2021-01-16', 3000 ,null,20);
insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(7934,'MILLER','CLERK',7782,'2021-01-16', 1300 ,null,10);

-- dept

create table dept(
    deptno int primary key not null,
    dname varchar(14),
    loc varchar(13)
);

insert into dept(deptno, dname, loc) values(10,'ACCOUNTING','NEW YORK');
insert into dept(deptno, dname, loc) values(20,'RESEARCH','DALLAS');
insert into dept(deptno, dname, loc) values(30,'SALES','CHICAGO');
insert into dept(deptno, dname, loc) values(40,'OPERATIONS','BOSTON');

-- salgrade
create table salgrade
(
    grade int(10),
    losal int(10),
    hisal int(10)
);

insert into salgrade(grade, losal, hisal) values(1, 700, 1200);
insert into salgrade(grade, losal, hisal) values(2, 1201, 1400);
insert into salgrade(grade, losal, hisal) values(3, 1401, 2000);
insert into salgrade(grade, losal, hisal) values(4, 2001, 3000);
insert into salgrade(grade, losal, hisal) values(5, 3001, 9999);


-- 添加外键
-- 添加外键约束，使两个表有关联
alter table
    table-name [表名称] add constraint fk_tablename_foreignKeyName[外键名称]
    foreign key (keyname[关联表的主键]) references
    table-name (keyname[关联表的主键])

-- 使用 deptno 作为外键关联两个表
alter table emp add constraint fk_dept_foreigndeptno foreign key(deptno) references dept(deptno);

