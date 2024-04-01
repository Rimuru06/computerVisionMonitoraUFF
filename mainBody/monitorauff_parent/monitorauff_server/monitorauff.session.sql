INSERT INTO "TB_INDIVIDUO"(nome, criado_em, atualizado_em)
VALUES ('individuo_01', now(), now()),
	('individuo_02', now(), now()),
	('individuo_03', now(), now()),
	('individuo_04', now(), now()),
	('individuo_05', now(), now());
--==========================================================
INSERT INTO "TB_OCORRENCIA_FACE"(
		camera_id,
		img_filename,
		data_md5,
		criado_em,
		atualizado_em,
		individuo_id
	)
VALUES (
		1,
		'of_01',
		'of_01',
		now(),
		now(),
		1
	),
	(
		1,
		'of_02',
		'of_02',
		now(),
		now(),
		2
	),
	(
		2,
		'of_03',
		'of_03',
		now(),
		now(),
		1
	),
	(
		1,
		'of_04',
		'of_04',
		now(),
		now(),
		3
	),
	(
		2,
		'of_05',
		'of_05',
		now(),
		now(),
		3
	),
	(
		2,
		'of_06',
		'of_06',
		now(),
		now(),
		3
	),
	(
		1,
		'of_07',
		'of_07',
		now(),
		now(),
		null
	),
	(
		1,
		'of_08',
		'of_08',
		now(),
		now(),
		null
	),
	(
		1,
		'of_09',
		'of_09',
		now(),
		now(),
		null
	),
	(
		1,
		'of_10',
		'of_10',
		now(),
		now(),
		4
	),
	(
		2,
		'of_11',
		'of_11',
		now(),
		now(),
		4
	),
	(
		2,
		'of_12',
		'of_12',
		now(),
		now(),
		2
	),
	(
		2,
		'of_13',
		'of_13',
		now(),
		now(),
		null
	),
	(
		1,
		'of_14',
		'of_14',
		now(),
		now(),
		null
	),
	(
		2,
		'of_15',
		'of_15',
		now(),
		now(),
		null
	),
	(
		1,
		'of_16',
		'of_16',
		now(),
		now(),
		null
	),
	(
		1,
		'of_17',
		'of_17',
		now(),
		now(),
		null
	),
	(
		1,
		'of_18',
		'of_18',
		now(),
		now(),
		5
	),
	(
		2,
		'of_19',
		'of_19',
		now(),
		now(),
		5
	),
	(
		1,
		'of_20',
		'of_20',
		now(),
		now(),
		null
	);
--==========================================================
INSERT INTO "TB_ETIQUETA_INDIVIDUO"(nome, descricao, criado_em, atualizado_em)
VALUES ('etiqueta_01', 'descricao_01', now(), now()),
	('etiqueta_02', 'descricao_02', now(), now()),
	('etiqueta_03', 'descricao_03', now(), now()),
	('etiqueta_04', 'descricao_04', now(), now()),
	('etiqueta_05', 'descricao_05', now(), now());
--==========================================================
INSERT INTO "RL_INDIVIDUO_ETIQUETA"(
		individuo_id,
		etiqueta_individuo_id,
		criado_em,
		atualizado_em
	)
VALUES (1, 1, now(), now()),
	(1, 3, now(), now()),
	(2, 5, now(), now()),
	(5, 2, now(), now()),
	(5, 4, now(), now());
--==========================================================
INSERT INTO "TB_PERMISSAO_INDIVIDUO"(
		nome,
		descricao,
		criado_em,
		atualizado_em
	)
VALUES ('permissao_01', 'descricao_01', now(), now()),
	('permissao_02', 'descricao_02', now(), now()),
	('permissao_03', 'descricao_03', now(), now()),
	('permissao_04', 'descricao_04', now(), now()),
	('permissao_05', 'descricao_05', now(), now());
--==========================================================
INSERT INTO "RL_ETIQUETA_PERMISSAO_INDIVIDUO"(
		etiqueta_individuo_id,
		permissao_individuo_id,
		criado_em,
		atualizado_em
	)
VALUES (1, 1, now(), now()),
	(2, 2, now(), now()),
	(3, 3, now(), now()),
	(4, 4, now(), now()),
	(5, 5, now(), now());
--==========================================================
INSERT INTO "RL_PERMISSAO_INDIVIDUO_GRUPO"(permissao_id, grupo_id, criado_em, atualizado_em)
VALUES (1, 2, now(), now()),
	(2, 2, now(), now()),
	(3, 3, now(), now()),
	(4, 3, now(), now()),
	(5, 4, now(), now());
--==========================================================
INSERT INTO "TB_TIPO_SERVICO"(nome, descricao, criado_em, atualizado_em)
VALUES (
		'Detecção de Placa',
		'Serviço de Detecção de Placas Veiculares',
		now(),
		now()
	),
	(
		'Detecção de Face',
		'Serviço de Detecção de Rostos',
		now(),
		now()
	);
INSERT INTO "RL_TIPO_SERVICO_MONITOR"(monitor_id, servico_id, criado_em, atualizado_em)
VALUES (1, 1, now(), now()),
	(1, 2, now(), now()),
	(2, 1, now(), now());