USE DB_TESTE;

CREATE TABLE TB_USUARIOS(
		ID 				INT				AUTO_INCREMENT	PRIMARY KEY
	,	NOME			VARCHAR(100)	NOT NULL
	,	EMAIL			VARCHAR(250)	NOT NULL
	,	LOGIN			VARCHAR(40)		NOT NULL
	,	SENHA			VARCHAR(30)		NOT	NULL
	,	NIVEL_USUARIO	SMALLINT		NOT NULL
)
	