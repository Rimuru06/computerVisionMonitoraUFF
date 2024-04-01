
INSERT INTO public.monitor_layer (id, name, status) VALUES (3, 'Valonguinho', 'Ativo');

INSERT INTO public.monitor_layer (id, name, status) VALUES (2, 'Gragoatá', 'Ativo');

INSERT INTO public.monitor_layer (id, name, status) VALUES (1, 'Praia Vermelha', 'Ativo');

INSERT INTO public.monitor_layer (id, name, status) VALUES (4, 'HUAP', 'Ativo');




INSERT INTO public.monitor_controlpoint (id, name, address, latitude, longitude, layer_id, status) VALUES (9, 'Entrada R. Passos da Pátria', 'R. Passo da Pátria, 150 - São Domingos, Niterói', -22.90379626097408, -43.13028199284894, 1, 'Ativo');

INSERT INTO public.monitor_controlpoint (id, name, address, latitude, longitude, layer_id, status) VALUES (10, 'Entrada Milton Tavares', 'Av. Milton Tavares de Souza, 380 - Gragoatá - Niterói - RJ', -22.9053894210166, -43.13468716871977, 1, 'Ativo');

INSERT INTO public.monitor_controlpoint (id, name, address, latitude, longitude, layer_id, status) VALUES (11, 'IC', 'Em frente ao IC', -22.906156728792965, -43.13293255271704, 1, 'Ativo');

INSERT INTO public.monitor_controlpoint (id, name, address, latitude, longitude, layer_id, status) VALUES (12, 'Entrada Gragoatá', 'R. Prof. Marcos Waldemar de Freitas Reis - São Domingos, Niterói - RJ', -22.898614297831163, -43.13166162851642, 2, 'Ativo');

INSERT INTO public.monitor_controlpoint (id, name, address, latitude, longitude, layer_id, status) VALUES (13, 'Letras', 'Letras Bloco B', -22.89935323812315, -43.13292956540841, 2, 'Ativo');

INSERT INTO public.monitor_controlpoint (id, name, address, latitude, longitude, layer_id, status) VALUES (14, 'Entrada Visconde do Rio Branco', 'Av. Visconde do Rio Branco, 592 - Centro, Niterói - RJ', -22.896589172976206, -43.12550340197665, 3, 'Ativo');

INSERT INTO public.monitor_controlpoint (id, name, address, latitude, longitude, layer_id, status) VALUES (15, 'Entrada Shopping', 'Av. Badger da Silveira, 128, Centro - Niterói - RJ', -22.897185583245335, -43.124951385449144, 3, 'Ativo');

INSERT INTO public.monitor_controlpoint (id, name, address, latitude, longitude, layer_id, status) VALUES (16, 'HUAP', 'R. Marquês de Paraná, 303 - Centro, Niterói - RJ', -22.895344777948864, -43.11262982219504, 4, 'Ativo');




INSERT INTO public.monitor_camera (id, tag_slug, direction, model, rtsp_url, agent_user, agent_server, controlpoint_id, status) VALUES (3, 'celular-cam1', 'in', 'P30', 'rtsp://192.168.1.2:8085/h264_ulaw.sdp', 'gleison', '127.0.0.1', 10, 'Ativo');

INSERT INTO public.monitor_camera (id, tag_slug, direction, model, rtsp_url, agent_user, agent_server, controlpoint_id, status) VALUES (1, 'celular-cam2', 'in', 'P30', 'rtsp://192.168.1.5:8085/h264_ulaw.sdp', 'gleison', '127.0.0.1', 9, 'Ativo');




INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2668, '2021-07-15 19:14:38.277895-03', 'OOO8343', 'e3523ebd-4303-4af2-b63d-45969e34bae3.zip', 'z2316YNi', 'ac42f01492ad06189318259709b69ac9', 1, NULL, 'celular-cam2-e8d9b7e0-3476-477d-b7a4-fb4056fc142f.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2669, '2021-07-15 19:14:38.348881-03', 'QQD8343', '65d9e204-2157-4c93-b0ab-5cee3a226bfe.zip', 'aiHqboDL', '35bd68343aecac05e789514c9ba7cdb4', 1, NULL, 'celular-cam2-6aff966c-a5b8-4f99-9ba6-0b6b7e9050d7.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2670, '2021-07-15 19:14:39.00067-03', 'OOD8343', '93dfcd98-231e-4502-96f2-b1c986b52d47.zip', 'UMyX99a9', '48d391246d8fec497b08bfeffe06c335', 1, NULL, 'celular-cam2-7e99aec3-4883-4dcc-aab5-19444fdd6c3a.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2671, '2021-07-15 19:14:38.58764-03', 'OOO8343', 'fff2f165-cee5-4981-9849-07dcc8336691.zip', 'YEWTTcjM', '07777f0731816e381dc1a664567ef817', 1, NULL, 'celular-cam2-a2fb1ce0-d74d-4a32-afa8-637f30b5cf3c.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2672, '2021-07-15 19:14:38.61395-03', 'OOO8343', '639ef621-5206-4957-b805-24f92b518b90.zip', 'fnvAMpSY', '79864288db8ea01ad89137c0e1d4ca31', 1, NULL, 'celular-cam2-54cb3974-0bdf-4589-956c-5c8399ef1988.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2673, '2021-07-15 19:14:38.792405-03', 'QQD8343', 'a5f283fc-7ff3-446b-b80a-6c21fae775cd.zip', 'SwKP4w8y', 'a4c109d7dd436934f59b84975a262642', 1, NULL, 'celular-cam2-8d2c20ae-1700-49c9-acff-213e96a004a6.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2674, '2021-07-15 19:14:39.189863-03', 'OOD8343', 'fbbf2ec7-e131-499a-bbe1-83c10f627c34.zip', 'MbqpSXFg', '4aaa60e943834904e919870a8ef964a8', 1, NULL, 'celular-cam2-b05fe3b8-3db8-43e5-8bee-2d18794d5d16.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2675, '2021-07-15 19:14:39.13822-03', '0OD8343', '4ecfade5-ba50-444e-aa2c-57d691d2433e.zip', 'msLQd4Y9', '6461c5fb02ab8dc9c77d192caaf8752c', 1, NULL, 'celular-cam2-1c77dfcd-47b1-41fa-9415-961e973739a4.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2676, '2021-07-15 19:14:39.439206-03', 'QOD8343', '06cdae73-e609-4878-b104-ad78f2d97892.zip', '2Znd3hry', 'aede5e5d834a4f042d9baa53269aecac', 1, NULL, 'celular-cam2-40b5ea4c-c314-4420-a35f-b9c0e8a9f16b.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2677, '2021-07-15 19:14:39.305355-03', 'OOD8343', 'de73976f-5611-4bc6-bd08-2f8f9742e42b.zip', 'jSAJoACl', 'd5432f1f9efa2335b0aace46d8b83abe', 1, NULL, 'celular-cam2-9ac7a684-1561-4a0f-b050-092fa753df36.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2678, '2021-07-15 19:14:39.62722-03', 'OQD8343', '2be67fa0-c3c7-4434-af88-72e81e243fa8.zip', 'cdKkoh6T', '70ad7356a3549682ae5dcc3f482866cb', 1, NULL, 'celular-cam2-be1dc116-d9a9-4274-8e2f-68cdce5c2513.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2679, '2021-07-15 19:14:39.839165-03', 'OQD8343', '066cebf3-d68a-42c6-909e-462acb31fb44.zip', 'j5jZR1pf', '248ffc8cd3c92aa1a3bbd02f53cdb5fb', 1, NULL, 'celular-cam2-a0e57736-8e0f-4aa0-94ce-ccb22e4e5844.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2680, '2021-07-15 19:14:40.370928-03', 'OQD8343', '78967f8d-4634-4683-b78b-e45ea6c6bf75.zip', '02smL2ab', '67d2c6c976cf76837b0eda60fcb5d2dd', 1, NULL, 'celular-cam2-cf2ab94a-6b30-426c-8938-21fe8aad4a06.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2681, '2021-07-15 19:14:40.335911-03', 'OQD8343', 'c1538a13-bdd1-4e07-84a6-77236f1b3b50.zip', 'kX6DLBlF', '568cb603ee9e1ee4c6c625a9f2b2f47f', 1, NULL, 'celular-cam2-6ba58154-994d-41d2-a270-3104d3dfc3e3.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2682, '2021-07-15 19:14:39.696317-03', 'OOD8343', 'd2584fd0-0401-4719-881c-a65246d8a3fd.zip', 'GwJWCm1I', '13fb399d1842aee3a9b894d6447a9f62', 1, NULL, 'celular-cam2-712c7175-217b-47c4-bfe9-080f567279c5.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2683, '2021-07-15 19:14:39.949984-03', 'OQD8343', 'fb9d5809-ef1a-41fe-a631-ba0d9b23f9a9.zip', 'vSq2Hup0', '1ab56ba45fc7289f4b0ae9f97b67ea2b', 1, NULL, 'celular-cam2-ebcb6177-2011-4c94-b48a-bba720c0af80.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2684, '2021-07-15 19:14:40.529089-03', 'QQO8343', '9473c018-59eb-4010-a5eb-9efdf56e5f12.zip', '0rSwwSeD', '8cb4dfff5edb8c2bba8bdbbd50e3f271', 1, NULL, 'celular-cam2-3a88987e-1948-4cdf-9c97-db0a6c69d686.png');
INSERT INTO public.monitor_detectedlicenseplate (id, detection_date, license_plate, data_filename, data_password, data_md5, camera_id, veiculo_id, img_filename) VALUES (2685, '2021-07-15 19:14:40.631748-03', 'OQD8343', '7564a9d4-f1d2-416a-839c-c8c6f88e3ccd.zip', 'm0K2ut2P', 'ad2fe609a0f1f52667187896bc3d5e5c', 1, NULL, 'celular-cam2-7fb49763-fcc8-4e88-bfbb-0b8a02a4ed40.png');

