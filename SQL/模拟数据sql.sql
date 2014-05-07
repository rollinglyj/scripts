
/*先清空carflow中的数据,用delete from table删除几十万条数据会非常的慢，因为要写日志文件*/
truncate table [saveenergy].[dbo].[carflow]
      
declare @collectorid1 int
select @collectorid1=collectorid from [saveenergy].[dbo].[collector] where position='1.成双大道商都路交叉口'

declare @collectorid2 int
select @collectorid2=collectorid from [saveenergy].[dbo].[collector] where position='2.成双大道商都路交叉口'

declare @collectorid3 int
select @collectorid3=collectorid from [saveenergy].[dbo].[collector] where position='藏卫路北三段五岔路口'

declare @collectorid4 int
select @collectorid4=collectorid from [saveenergy].[dbo].[collector] where position='丛桂街县政府路口 '

declare @collectorid5 int
select @collectorid5=collectorid from [saveenergy].[dbo].[collector] where position='双九路双楠大道交叉路口'

declare @collectorid6 int
select @collectorid6=collectorid from [saveenergy].[dbo].[collector] where position='白衣中街迎春路交叉路口'

declare @collectorid7 int
select @collectorid7=collectorid from [saveenergy].[dbo].[collector] where position='藏卫南路白河路一段交叉路口'

declare @collectorid8 int
select @collectorid8=collectorid from [saveenergy].[dbo].[collector] where position='三强西路蓄联大饭店路口'

declare @collectorid9 int
select @collectorid9=collectorid from [saveenergy].[dbo].[collector] where position='三强东路东升街路口'

declare @collectorid10 int
select @collectorid10=collectorid from [saveenergy].[dbo].[collector] where position='金河路洪江路口'


/*设置数据库各列变量*/
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
