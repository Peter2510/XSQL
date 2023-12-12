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

CREATE PROCEDURE proc (@PROD int, @CANT int)
as BEGIN 
    DECLARE @id int;
END;
    

Create Procedure JD ( @id as int, @nombre varchar(20), @apellido varchar(20), @edad int) as
Begin
Declare @SumaProducto decimal;
Set @SumaProducto = retornaSuma(1);
end;

CREATE PROCEDURE sp_nuevoprocedimiento(@MONTO AS 
DECIMAL,@IDFACTURA INT)
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
Declare @SumaProducto decimal(10,2);
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

