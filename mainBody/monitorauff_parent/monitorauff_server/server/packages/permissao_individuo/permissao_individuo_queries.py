query_get_permissao_by_individuo = '''
SELECT 
	"TB_PERMISSAO_INDIVIDUO".id,
	"TB_PERMISSAO_INDIVIDUO".nome,
	"TB_PERMISSAO_INDIVIDUO".descricao,
	"TB_PERMISSAO_INDIVIDUO".criado_em,
	"TB_PERMISSAO_INDIVIDUO".atualizado_em
FROM "TB_PERMISSAO_INDIVIDUO"
INNER JOIN 
	"RL_ETIQUETA_PERMISSAO_INDIVIDUO"
		ON "TB_PERMISSAO_INDIVIDUO"."id" = "RL_ETIQUETA_PERMISSAO_INDIVIDUO"."permissao_individuo_id"
INNER JOIN
	"TB_ETIQUETA_INDIVIDUO"
		ON "TB_ETIQUETA_INDIVIDUO"."id" = "RL_ETIQUETA_PERMISSAO_INDIVIDUO"."etiqueta_individuo_id"
INNER JOIN
	"RL_INDIVIDUO_ETIQUETA"
		ON "RL_INDIVIDUO_ETIQUETA"."etiqueta_individuo_id" = "RL_ETIQUETA_PERMISSAO_INDIVIDUO"."etiqueta_individuo_id"
INNER JOIN
	"TB_INDIVIDUO"
		ON "TB_INDIVIDUO"."id" = "RL_INDIVIDUO_ETIQUETA"."individuo_id"
WHERE "TB_INDIVIDUO"."id" = %s;
'''

query_get_permissao_by_grupo = '''
SELECT 
	"TB_PERMISSAO_INDIVIDUO".id,
	"TB_PERMISSAO_INDIVIDUO".nome,
	"TB_PERMISSAO_INDIVIDUO".descricao,
	"TB_PERMISSAO_INDIVIDUO".criado_em,
	"TB_PERMISSAO_INDIVIDUO".atualizado_em
FROM "TB_PERMISSAO_INDIVIDUO"
INNER JOIN 
	"RL_PERMISSAO_INDIVIDUO_GRUPO"
		ON "TB_PERMISSAO_INDIVIDUO".id = "RL_PERMISSAO_INDIVIDUO_GRUPO".permissao_id
WHERE
	"RL_PERMISSAO_INDIVIDUO_GRUPO".grupo_id = %s;
'''