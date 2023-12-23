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
-- Returns the stock level for the product. 
BEGIN 
 DECLARE @ret int;
 IF @ret == NULL THEN
 SET @ret = 0; 
 RETURN 2;
 END IF;
END;

--Simple
CREATE FUNCTION Retornasuma()
RETURNS int 
AS 
-- Returns the stock level for the product. 
BEGIN 
 DECLARE @ret int; 
 
 IF @ret == NULL THEN
 SET @ret = 0; 
 RETURN 2; 
 END IF;
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


--simple
CREATE PROCEDURE proc ()
as BEGIN 
    DECLARE @id int;
END;
    

CREATE PROCEDURE proc (@PROD int, @CANT int)
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




