CREATE TABLE public.monitor_user (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    "tipoUser" character varying(150) NOT NULL,
    matricula character varying(150),
    name character varying(200) NOT NULL,
    status character varying(8) NOT NULL
);


CREATE TABLE public.monitor_layer (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    status character varying(8) NOT NULL
);


CREATE TABLE public.monitor_controlpoint (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    address character varying(200) NOT NULL,
    latitude double precision NOT NULL,
    longitude double precision NOT NULL,
    layer_id integer NOT NULL,
    status character varying(8) NOT NULL
);


CREATE TABLE public.monitor_camera (
    id integer NOT NULL,
    tag_slug character varying(50) NOT NULL,
    direction character varying(8) NOT NULL,
    model character varying(200) NOT NULL,
    rtsp_url character varying(200) NOT NULL,
    agent_user character varying(100) NOT NULL,
    agent_server inet NOT NULL,
    controlpoint_id integer NOT NULL,
    status character varying(8) NOT NULL
);


CREATE TABLE public.monitor_detectedlicenseplate (
    id integer NOT NULL,
    detection_date timestamp with time zone NOT NULL,
    license_plate character varying(7) NOT NULL,
    data_filename character varying(256) NOT NULL,
    data_password character varying(8) NOT NULL,
    data_md5 character varying(32) NOT NULL,
    camera_id integer NOT NULL,
    veiculo_id integer,
    img_filename character varying(256) NOT NULL
);


CREATE TABLE public.monitor_veiculo (
    id integer NOT NULL,
    marca character varying(200) NOT NULL,
    modelo character varying(200) NOT NULL,
    ano character varying(100) NOT NULL,
    cor character varying(200) NOT NULL
);


CREATE TABLE public.monitor_alertveiculo (
    id integer NOT NULL,
    license_plate character varying(7) NOT NULL,
    motivo text NOT NULL
);



CREATE TABLE public.monitor_historicoalert (
    id integer NOT NULL,
    evento character varying(200) NOT NULL,
    obs text NOT NULL,
    update_date timestamp with time zone NOT NULL,
    "alertVeiculo_id" integer NOT NULL,
    user_id bigint NOT NULL
);
