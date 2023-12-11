CREATE TABLE Persona (
ID int NOT NULL PRIMARY KEY,
PrimerNombre varchar(150) NOT NULL,
SegundoNombre varchar(150) NULL,
FechaNacimiento datetime,
Identificacion int,
order int references per
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

CREATE PROCEDURE proc (@PROD id)
BEGIN   
    DECLARE @id int
END;
    

Create Procedure JD ( @id int, @nombre varchar(20), @apellido varchar(20), @edad int) as
Begin
Declare @SumaProducto decimal(10,2);
Set @SumaProducto = retornaSuma(1);
end;

alter Procedure JD ( @id int, @nombre varchar(20), @apellido varchar(20), @edad int) as
Begin
Declare @SumaProducto decimal(10,2);
Set @SumaProducto = retornaSuma(1);
end;


Alter table tbfactura drop column tipotarjeta ;
DROP TABLE tbproducts;

Truncate table tbfactura ;
Truncate table tbdetallefactura;

Alter table products add column inventario decimal(10,2);
Alter table tbfactura add column formapago int;
Alter table tbfactura add column tipotarjeta int;
