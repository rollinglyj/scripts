
/*�����carflow�е�����,��delete from tableɾ����ʮ�������ݻ�ǳ���������ΪҪд��־�ļ�*/
truncate table [saveenergy].[dbo].[carflow]
      
declare @collectorid1 int
select @collectorid1=collectorid from [saveenergy].[dbo].[collector] where position='1.��˫����̶�·�����'

declare @collectorid2 int
select @collectorid2=collectorid from [saveenergy].[dbo].[collector] where position='2.��˫����̶�·�����'

declare @collectorid3 int
select @collectorid3=collectorid from [saveenergy].[dbo].[collector] where position='����·���������·��'

declare @collectorid4 int
select @collectorid4=collectorid from [saveenergy].[dbo].[collector] where position='�Թ��������·�� '

declare @collectorid5 int
select @collectorid5=collectorid from [saveenergy].[dbo].[collector] where position='˫��·˫骴������·��'

declare @collectorid6 int
select @collectorid6=collectorid from [saveenergy].[dbo].[collector] where position='�����н�ӭ��·����·��'

declare @collectorid7 int
select @collectorid7=collectorid from [saveenergy].[dbo].[collector] where position='������·�׺�·һ�ν���·��'

declare @collectorid8 int
select @collectorid8=collectorid from [saveenergy].[dbo].[collector] where position='��ǿ��·�����󷹵�·��'

declare @collectorid9 int
select @collectorid9=collectorid from [saveenergy].[dbo].[collector] where position='��ǿ��·������·��'

declare @collectorid10 int
select @collectorid10=collectorid from [saveenergy].[dbo].[collector] where position='���·�齭·��'


/*�������ݿ���б���*/
declare @time datetime
set @time='2011-07-11 00:00:00'

declare @i int
set @i=1
declare @now datetime
set @now=(select GETDATE())

declare @maxi int
set @maxi=(select datediff(MINUTE,'2011-07-11 00:00:00',@now))

declare @densityleft float
declare @densityright float

declare @leftflow int
declare @rightflow int

declare @tmpdens float
declare @tmpflow int


while @i<@maxi
begin
 set @leftflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 set @rightflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 set @time=(select dateadd(MINUTE,1,@time))
 set @densityleft=(select ROUND(rand(),3))
 set @densityright=(select ROUND(rand(),3))
 

 
 if @leftflow<@rightflow 
 begin
  if @densityleft>@densityright
	begin
		
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
 
 if @leftflow>@rightflow
 begin
	if @densityleft<@densityright
	begin
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
  
INSERT INTO [saveenergy].[dbo].[carflow]
           ([collectorid]
           ,[leftflow]
           ,[rightflow]
           ,[flowtime]
           ,[trafficdensityleft]
           ,[trafficdensityright])
     VALUES
           (
           @collectorid1
           ,@leftflow
           ,@rightflow
           ,@time
           ,@densityleft
           ,@densityright)
    
    

 

 /*22222222222222222*/
 
 
 set @leftflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 set @rightflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 
 set @densityleft=(select ROUND(rand(),3))
 set @densityright=(select ROUND(rand(),3))
 
 if @leftflow<@rightflow 
 begin
  if @densityleft>@densityright
	begin
		
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
 
 if @leftflow>@rightflow
 begin
	if @densityleft<@densityright
	begin
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
           
   INSERT INTO [saveenergy].[dbo].[carflow]
           ([collectorid]
           ,[leftflow]
           ,[rightflow]
           ,[flowtime]
           ,[trafficdensityleft]
           ,[trafficdensityright])
     VALUES
           (
           @collectorid2
           ,@leftflow
           ,@rightflow
           ,@time
           ,@densityleft
           ,@densityright)


/**3333333333333333333*/

    set @leftflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 set @rightflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 
 set @densityleft=(select ROUND(rand(),3))
 set @densityright=(select ROUND(rand(),3))
 
if @leftflow<@rightflow 
 begin
  if @densityleft>@densityright
	begin
		
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
 
 if @leftflow>@rightflow
 begin
	if @densityleft<@densityright
	begin
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
           
   INSERT INTO [saveenergy].[dbo].[carflow]
           ([collectorid]
           ,[leftflow]
           ,[rightflow]
           ,[flowtime]
           ,[trafficdensityleft]
           ,[trafficdensityright])
     VALUES
           (
           @collectorid3
           ,@leftflow
           ,@rightflow
           ,@time
           ,@densityleft
           ,@densityright)






/*****44444444444444444*****/

    set @leftflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 set @rightflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 
 set @densityleft=(select ROUND(rand(),3))
 set @densityright=(select ROUND(rand(),3))

if @leftflow<@rightflow 
 begin
  if @densityleft>@densityright
	begin
		
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
 
 if @leftflow>@rightflow
 begin
	if @densityleft<@densityright
	begin
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
           
   INSERT INTO [saveenergy].[dbo].[carflow]
           ([collectorid]
           ,[leftflow]
           ,[rightflow]
           ,[flowtime]
           ,[trafficdensityleft]
           ,[trafficdensityright])
     VALUES
           (
           @collectorid4
           ,@leftflow
           ,@rightflow
           ,@time
           ,@densityleft
           ,@densityright)




/****555555555******/

    set @leftflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 set @rightflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 
 set @densityleft=(select ROUND(rand(),3))
 set @densityright=(select ROUND(rand(),3))

if @leftflow<@rightflow 
 begin
  if @densityleft>@densityright
	begin
		
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
 
 if @leftflow>@rightflow
 begin
	if @densityleft<@densityright
	begin
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
           
   INSERT INTO [saveenergy].[dbo].[carflow]
           ([collectorid]
           ,[leftflow]
           ,[rightflow]
           ,[flowtime]
           ,[trafficdensityleft]
           ,[trafficdensityright])
     VALUES
           (
           @collectorid5
           ,@leftflow
           ,@rightflow
           ,@time
           ,@densityleft
           ,@densityright)


/****666666666666666******/

    set @leftflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 set @rightflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 
 set @densityleft=(select ROUND(rand(),3))
 set @densityright=(select ROUND(rand(),3))

if @leftflow<@rightflow 
 begin
  if @densityleft>@densityright
	begin
		
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
 
 if @leftflow>@rightflow
 begin
	if @densityleft<@densityright
	begin
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
           
   INSERT INTO [saveenergy].[dbo].[carflow]
           ([collectorid]
           ,[leftflow]
           ,[rightflow]
           ,[flowtime]
           ,[trafficdensityleft]
           ,[trafficdensityright])
     VALUES
           (
           @collectorid6
           ,@leftflow
           ,@rightflow
           ,@time
           ,@densityleft
           ,@densityright)

/*****777777777777777*****/

    set @leftflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 set @rightflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 
 set @densityleft=(select ROUND(rand(),3))
 set @densityright=(select ROUND(rand(),3))

if @leftflow<@rightflow 
 begin
  if @densityleft>@densityright
	begin
		
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
 
 if @leftflow>@rightflow
 begin
	if @densityleft<@densityright
	begin
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
           
   INSERT INTO [saveenergy].[dbo].[carflow]
           ([collectorid]
           ,[leftflow]
           ,[rightflow]
           ,[flowtime]
           ,[trafficdensityleft]
           ,[trafficdensityright])
     VALUES
           (
           @collectorid7
           ,@leftflow
           ,@rightflow
           ,@time
           ,@densityleft
           ,@densityright)



/*****88888888888888*****/


    set @leftflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 set @rightflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 
 set @densityleft=(select ROUND(rand(),3))
 set @densityright=(select ROUND(rand(),3))
 
if @leftflow<@rightflow 
 begin
  if @densityleft>@densityright
	begin
		
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
 
 if @leftflow>@rightflow
 begin
	if @densityleft<@densityright
	begin
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
           
   INSERT INTO [saveenergy].[dbo].[carflow]
           ([collectorid]
           ,[leftflow]
           ,[rightflow]
           ,[flowtime]
           ,[trafficdensityleft]
           ,[trafficdensityright])
     VALUES
           (
           @collectorid8
           ,@leftflow
           ,@rightflow
           ,@time
           ,@densityleft
           ,@densityright)



/****9999999999999999999******/

    set @leftflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 set @rightflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 
 set @densityleft=(select ROUND(rand(),3))
 set @densityright=(select ROUND(rand(),3))
 
if @leftflow<@rightflow 
 begin
  if @densityleft>@densityright
	begin
		
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
 
 if @leftflow>@rightflow
 begin
	if @densityleft<@densityright
	begin
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
           
   INSERT INTO [saveenergy].[dbo].[carflow]
           ([collectorid]
           ,[leftflow]
           ,[rightflow]
           ,[flowtime]
           ,[trafficdensityleft]
           ,[trafficdensityright])
     VALUES
           (
           @collectorid9
           ,@leftflow
           ,@rightflow
           ,@time
           ,@densityleft
           ,@densityright)


/***10**10**10****10****10***/

    set @leftflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 set @rightflow=(SELECT CAST( FLOOR(RAND()*50) AS INT) )
 
 set @densityleft=(select ROUND(rand(),3))
 set @densityright=(select ROUND(rand(),3))
if @leftflow<@rightflow 
 begin
  if @densityleft>@densityright
	begin
		
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
 
 if @leftflow>@rightflow
 begin
	if @densityleft<@densityright
	begin
		set @tmpdens=@densityleft
		set @densityleft=@densityright
		set @densityright=@tmpdens
	end
 end
           
   INSERT INTO [saveenergy].[dbo].[carflow]
           ([collectorid]
           ,[leftflow]
           ,[rightflow]
           ,[flowtime]
           ,[trafficdensityleft]
           ,[trafficdensityright])
     VALUES
           (
           @collectorid10
           ,@leftflow
           ,@rightflow
           ,@time
           ,@densityleft
           ,@densityright)


/**********/



   set @i=@i+1
end

GO
