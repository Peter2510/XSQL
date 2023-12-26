
select * from tbproducto;

idproducto	nombre	price
65	Producto1	120.50
66	Producto2	95.75

select * from tbfactura;

idfactura	fechafactura	nit
1	        2023-01-05	   123456789
2	        2023-02-10	   987654321

select * from tbdetallefactura;

iddetalle	idfactura	idproducto	cantidad	price	fechafactura
1	            1	        65	        5	    120.50	   2023-01-05
2	            1	        66	        3	    95.75	    2023-01-05
3	            2	        65	        2	    120.50    2023-02-10



SELECT * from tbdetallefactura,tbproducto where (tbdetallefactura.cantidad*tbdetallefactura.price )/1.12 > 100
And tbproducto.idproducto = tbdetallefactura.tbproducto;



SELECT *
FROM tbdetallefactura
JOIN tbproducto ON tbproducto.idproducto = tbdetallefactura.idproducto
WHERE (tbdetallefactura.cantidad * tbdetallefactura.price) / 1.12 > 100;


RESULTADO

iddetalle	idfactura	idproducto	cantidad	price	fechafactura	idproducto	nombre	    price
1	            1	        65	        5	    120.50	2023-01-05      	65	    Producto1	120.50
3	            2	        65	        2	    120.50	2023-02-10      	65	    Producto1	120.50
2	            1	        66	        3	    95.75	2023-01-05      	66	    Producto2	95.75