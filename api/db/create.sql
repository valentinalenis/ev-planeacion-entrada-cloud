CREATE TABLE entradas (
  id INT(11) NOT NULL AUTO_INCREMENT,
  parametros VARCHAR(45) NOT NULL,
  dataset VARCHAR(45) NOT NULL,
  tipo_entrada VARCHAR(45) NOT NULL,
  archivo VARCHAR(200) NOT NULL,
  descripcion VARCHAR(200) NOT NULL,
  tipo_producto VARCHAR(45) NOT NULL,
  nombre_producto VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
)