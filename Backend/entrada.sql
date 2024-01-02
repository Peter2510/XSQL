CREATE TABLE fact (
 iddetallefac int PRIMARY KEY,
  product_no int REFERENCE products (product_no),
 price decimal NOT NULL,
 cantidad decimal, 
 cantidad decimal NOT NULL 
);

CREATE TABLE tbdetallefactura (
 iddetallefac int PRIMARY KEY,
 idfactura int REFERENCE tbfactura(idfactura),
 product_no int REFERENCE products (product_no),
 price decimal NOT NULL,
 cantidad decimal NOT NULL 
);

--CREAR FUNCION
CREATE FUNCTION Retornasuma(@ProductID int) 
RETURNS int 
AS 
BEGIN 
 DECLARE @ret int;
 IF (@ret == 1) BEGIN
 SET @ret = 0; 
 RETURN 2;
 END;
END;


--Simple
CREATE FUNCTION Retornasuma()
RETURNS int 
AS 
-- Returns the stock level for the product. 
BEGIN 
 DECLARE @ret int; 
 
 IF (@ret == NULL) BEGIN
 SET @ret = 0; 
 RETURN 2; 
 END
END;

-- case
CASE 
    WHEN 1==1 
        THEN 'UNO IGUAL 1'
    WHEN 1==2 
        THEN 'UNO IGUAL 2'
    WHEN 1==3 
        THEN 'UNO IGUAL 3'
    WHEN 1==4 
        THEN 'UNO IGUAL 4'
    END validacion

    CASE
        WHEN @cuota > 1000 && @cuota <  1500
        THEN     SET @ajuste = 75;
        
        WHEN @cuota >= 1500 && @cuota <  2000   
            THEN SET @ajuste = 125;	
                
        WHEN @cuota > 0 &&  @cuota < 1000
            THEN SET @ajuste = 25;
        
        WHEN @cuota >=  2000
            THEN SET @ajuste = 150;					
        ELSE 
            THEN SET @ajuste = 0;
    END;


--simple
CREATE PROCEDURE proc ()
as BEGIN 
    DECLARE @id int;
END;
    

CREATE PROCEDURE proc (@PROD as int, @CANT int)
as BEGIN 
    DECLARE @id int;
END;
    

Create Procedure JD ( @id as int, @nombre varchar(20), @apellido varchar(20), @edad int) as
Begin
Declare @SumaProducto decimal;
Set @SumaProducto = retornaSuma(1);
end;

Create Procedure JD () as
Begin
Declare @SumaProducto decimal;
Set @SumaProducto = retornaSuma(1);
end;

CREATE PROCEDURE sp_nuevoprocedimiento(@MONTO AS 
DECIMAL,
@IDFACTURA INT)
AS
BEGIN 
DECLARE @IVA DECIMAL;
 DECLARE @ISR DECIMAL;
  SET @IVA = @MONTO - @MONTO/1.12;
 IF @MONTO > 2000 THEN 
 SET @ISR = @MONTO *0.07;
ELSE
 SET @ISR = @MONTO *0.10;
 END IF;
END;

alter Procedure JD ( @id int, @nombre varchar(20), @apellido varchar(20), @edad int) as
Begin
Declare @SumaProducto decimal;
Set @SumaProducto = retornaSuma(1);
end;


Alter table tbfactura drop column tipotarjeta ;
DROP TABLE tbproducts;

Truncate table tbfactura ;
Truncate table tbdetallefactura;

Alter table products add column inventario decimal;
Alter table tbfactura add column formapago int;
Alter table tbfactura add column tipotarjeta int;

Alter table products add column inventario decimal;
Alter table tbfactura add column formapago int;
Alter table tbfactura add column tipotarjeta int;

Truncate table tbfactura;
Truncate table tbdetallefactura;

Alter table tbfactura drop column tipotarjeta ;
DROP TABLE tbproducts;

SELECT 1+2*3+"hola"*'2023-12-20'*'2025-12-11';

SELECT 1+2*3+"hola";

SELECT '2023-12-15'/"2023-12-15";

SELECT ((5 + 3) * 2 > 10) && ((8 * 2 / 4) == 4) || ((7 - 3) != 4);
--    true                        true              4!=4 false  

--- error por procedencia
SELECT '2023-12-10'>='2023-12-10'*5;

-- si funciona
SELECT ('2023-12-10'>='2023-12-10')*5;

                -- MARCA ERROR ENTRE LAS OPERACIONES

USAR HOLA;
--CREAR FUNCION 
CREATE FUNCTION Retornasuma(@ProductID int,@ProductIDs decimal) 
RETURNS int 
AS 
BEGIN 
 DECLARE @ret int;
Set @ret = 456+1;
set @ProductIDs = 1.2+1&&4>2;

END;

                --Marcar error varchar y char
USAR HOLA;
--CREAR FUNCION 
CREATE FUNCTION Retornasuma(@ProductID Nchar(10)) 
RETURNS int 
AS 
BEGIN 
 
Set @ProductID = "";


END;

-- TODO OK

USAR HOLA;
CREATE FUNCTION Retornasuma(@ProductID BIT) 
RETURNS int 
AS 
BEGIN 
 
Set @ProductID = (1>0)+(0>0);


END;


----

CREATE FUNCTION Retornasuma()
RETURNS int 
AS 
-- Returns the stock level for the product. 
BEGIN 
 DECLARE @ret int; 
 SET @ret = 45; 
     
     IF (@ret == 0) BEGIN
         SET @ret = 123; 
         DECLARE @ret1 int;
         select @ret;
     END;
     
      ELSEIF (@ret == 0) BEGIN
         SET @ret = 145; 
         
         RETURN 2; 
     END;
     
      ELSEIF (@ret + 0) BEGIN
         SET @ret = 145; 
         DECLARE @ret int; 
         RETURN 2; 
     END;
     
     ELSE begin 
     SET @ret = 689; 
     DECLARE @ret1 int;
     end;
     
END;
----

-------PROBANDO FUNCIONES

CREATE FUNCTION Retornasuma()
RETURNS int 
AS 

 BEGIN 
    DECLARE @ret int; 
    SET @ret = 45; 
    RETURN @ret;    
         
END;


CREATE FUNCTION llamado()
RETURNS int 
AS 

 BEGIN 
    DECLARE @enLlamado int; 
    SET @enLlamado = retornaSuma();
         
END;



------------------------------- LLAMADO DE FUNCIONES SIMPLES-------------------

CREATE FUNCTION sp_calculacuota ()
RETURNs decimal
AS
BEGIN
		DECLARE @cuota decimal,@saldo decimal, @plazo int, @diasmora int;
		DECLARE @ajuste decimal;
        set @cuota = 2.2;
        set @saldo = 1.2;
        set @plazo = 1;
        set @diasmora = 45;
        set @ajuste = 2.3;
        
        set @cuota = (@saldo/@plazo)*0.45;
		
			
		RETURN @cuota;	
		
		
END;


CREATE FUNCTION llamado()
RETURNS int 
AS 

 BEGIN 
    DECLARE @enLlamado decimal; 
    SET @enLlamado = sp_calculacuota();
         
END;

---------------------------ERROR POR EL TAMAÑO DE LA CADENA----------------------------------------------

CREATE FUNCTION fn_retornaalturamora ()
RETURNs nchar(1500)
AS
BEGIN
	DECLARE @alturamora nvarchar(100);
    
    set @alturamora = "asaaaaaaaaaaa";
	RETURN @alturamora;
    
    end ;
    
CREATE FUNCTION llamado()
RETURNS int 
AS 

 BEGIN 
    DECLARE @enLlamado nvarchar(3); 
    SET @enLlamado = fn_retornaalturamora();
         
END;    


--------------------------------------------

----- ERROR EN EL TAMAÑO DE LOS LAS CADENAS----------
CREATE FUNCTION a (@hola nvarchar(1))
RETURNs int
AS
BEGIN
    declare @alturamora int;
	RETURN @alturamora;
end ;

CREATE FUNCTION b ()
RETURNs decimal
AS
BEGIN
    declare @llamada int;
    set @llamada = a("aaa");
	RETURN @llamada;
end ;

-----------------------------------------------------

--------------------if-------------------------------
CREATE FUNCTION fn_retornaalturamora ()
RETURNs nvarchar(15)
AS
BEGIN
	DECLARE @alturamora nvarchar(100);
    declare @diasmora int;
    set @diasmora = 5;
    SET @alturamora = "entre0 y 29";

		IF ((@diasmora > 0 && @diasmora < 30)+(1>1)) 
		BEGIN
			SET @alturamora = "entre0 y 29";
		END;
        	
		ELSEIF (@diasmora >= 30 && @diasmora < 60) 
		BEGIN 
			SET @alturamora = "entre 30 y 59";
		END;
        
        ELSE
        BEGIN
            SET @alturamora = "Nada de nada";
        END;
	
		
	
		
	RETURN @alturamora;
    
    end ;
    
CREATE FUNCTION llamado()
RETURNS int 
AS 

 BEGIN 
    DECLARE @enLlamado nvarchar(20); 
    SET @enLlamado = fn_retornaalturamora();
         
END;    


------------------------------------------------------


---------------- IF ANIDADO ----------------------
CREATE FUNCTION fn_retornaalturamora ()
RETURNs nvarchar(15)
AS
BEGIN
	DECLARE @alturamora nvarchar(100);
    declare @diasmora int;
    set @diasmora = 10;

        IF ((@diasmora > 0 && @diasmora < 30)+(1>1)) 
		BEGIN
			IF (@diasmora == 1)
            BEGIN
                SET @alturamora = "es uno";
            END;
            ELSE
            BEGIN
                SET @alturamora = "es mayor a uno menor a 30";
            END;
		END;
        	
		ELSEIF (@diasmora >= 30 && @diasmora < 60) 
		BEGIN 
			SET @alturamora = "entre 30 y 59";
		END;
        
        ELSE
        BEGIN
            SET @alturamora = "Nada de nada";
        END;

		
	RETURN @alturamora;
    
    end ;
    
CREATE FUNCTION llamado()
RETURNS int 
AS 

 BEGIN 
    DECLARE @enLlamado nvarchar(20); 
    SET @enLlamado = fn_retornaalturamora();
         
END;    


-------------------------------------------------

---------------- WHEN ------------------------------
CREATE FUNCTION fn_retornaalturamora ()
RETURNs nvarchar(15)
AS
BEGIN
	DECLARE @alturamora nvarchar(100);
    declare @diasmora int;
    set @diasmora = 551;

    CASE 
    WHEN (@diasmora > 0 && @diasmora < 30)+(1>1)
	   THEN SET @alturamora = "entre0 y 29";
	WHEN (@diasmora >= 30 && @diasmora < 60) 
	   THEN SET @alturamora = "entre 30 y 59";
	ELSE 
	   THEN SET @alturamora = "Nada de nada";
	END;

		
	RETURN @alturamora;
    
    end ;
    
CREATE FUNCTION llamado()
RETURNS int 
AS 

 BEGIN 
    DECLARE @enLlamado nvarchar(20); 
    SET @enLlamado = fn_retornaalturamora();
         
END;    

------------------WHILE---------------------------
CREATE FUNCTION fn_retornaalturamora1 ()
RETURNs nvarchar(15)
AS
BEGIN
	DECLARE @alturamora nvarchar(100);
    declare @diasmora int;
    set @diasmora = 1;

    
    While (@diasmora > 0 && @diasmora < 30)
    begin
    
	   SET @alturamora = "termino" + @diasmora + "ejecu" ;
	   set @diasmora = @diasmora +1;
	END;

		
	RETURN @alturamora;
    
    end ;
    
CREATE FUNCTION llamado2()
RETURNS int 
AS 

 BEGIN 
    DECLARE @enLlamado nvarchar(20); 
    SET @enLlamado = fn_retornaalturamora1();
         
END;    


------------------------------------------------



    CREATE FUNCTION fn_retornaalturamora ()
    RETURNs nvarchar(15)
    AS
    BEGIN
        -- int
        declare @diasmora int;
        set @diasmora = 1800;
        
        -- varchar
        declare @app nvarchar(15);
        set @app = "es un varchar";
            
        -- char
        declare @char nchar(15);
        set @char = "es un char";
        
        -- date
        declare @date date;
        set @date = '2014-12-15';
        
        -- datetime
        declare @dt datetime;
        set @dt = '2014-12-15 14:14:14';
        
        -- decimal
        declare @dec decimal;
        set @dec = 14.12;
        -- bit
        declare @bit bit;
        set @bit = 1;
        
        declare @bit2 bit;
        set @bit2 = 1;
        
        declare @bit3 bit;
        set @bit3 = (@bit * @bit2);
        
        select @diasmora+1;
        
        
        
        RETURN @app;
        
        end ;
        
    CREATE FUNCTION llamado()
    RETURNS int 
    AS 

    BEGIN 
        DECLARE @enLlamado nvarchar(20); 
        SET @enLlamado = fn_retornaalturamora();
            
    END;    


--------------- invocacion de procedure ------------------

create procedure sp (@val nvarchar(4),@decimal bit)
AS
BEGIN

    DECLARE @alturamora int;
    select @val;
    select @decimal;
    
END;

exec sp @val = "123", @decimal = 1;

--------------------------
usar nuevo;

select * from ggg;

alter procedure a(@n nchar(12))  as begin

declare @nm int;
set @nm = 14;


update ggg set estado = @n  where idestado = 15;

end;

exec a "ab";

select * from ggg;