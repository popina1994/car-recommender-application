--
-- PostgreSQL database dump
--

-- Dumped from database version 10.2
-- Dumped by pg_dump version 10.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE db_cars; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE db_cars IS 'Contains definitions of car companies, car models and information to related sites ';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner:
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Company; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Company" (
    "IDCompany" integer NOT NULL,
    "Name" character varying NOT NULL
);


ALTER TABLE "Company" OWNER TO postgres;

--
-- Name: Company_IDCompany_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Company_IDCompany_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Company_IDCompany_seq" OWNER TO postgres;

--
-- Name: Company_IDCompany_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Company_IDCompany_seq" OWNED BY "Company"."IDCompany";


--
-- Name: FullModel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "FullModel" (
    "IDFullModel" integer NOT NULL,
    "IDCompany" integer NOT NULL,
    "IDModel" integer NOT NULL,
    "IDVersion" integer,
    "IDLabel" integer NOT NULL
);


ALTER TABLE "FullModel" OWNER TO postgres;

--
-- Name: TABLE "FullModel"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE "FullModel" IS 'IDLabel represents IDLabel in text document';


--
-- Name: COLUMN "FullModel"."IDLabel"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "FullModel"."IDLabel" IS 'Defines index of a label in labels.txt ';


--
-- Name: FullModel_IDFullModel_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "FullModel_IDFullModel_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "FullModel_IDFullModel_seq" OWNER TO postgres;

--
-- Name: FullModel_IDFullModel_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "FullModel_IDFullModel_seq" OWNED BY "FullModel"."IDFullModel";


--
-- Name: Model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Model" (
    "IDModel" integer NOT NULL,
    "Name" character varying NOT NULL
);


ALTER TABLE "Model" OWNER TO postgres;

--
-- Name: Model_IDMod_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Model_IDMod_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Model_IDMod_seq" OWNER TO postgres;

--
-- Name: Model_IDMod_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Model_IDMod_seq" OWNED BY "Model"."IDModel";


--
-- Name: Version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Version" (
    "IDVersion" integer NOT NULL,
    "Name" character varying NOT NULL
);


ALTER TABLE "Version" OWNER TO postgres;

--
-- Name: Version_IDVer_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Version_IDVer_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Version_IDVer_seq" OWNER TO postgres;

--
-- Name: Version_IDVer_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Version_IDVer_seq" OWNED BY "Version"."IDVersion";


--
-- Name: WebSite; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "WebSite" (
    "IDWebSite" integer NOT NULL,
    "Name" character varying NOT NULL,
    "URL" character varying NOT NULL,
    "ParameterModel" character varying NOT NULL,
    "ParameterCompany" character varying NOT NULL,
    "ParameterVersion" character varying NOT NULL
);


ALTER TABLE "WebSite" OWNER TO postgres;

--
-- Name: WebSiteCompany; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "WebSiteCompany" (
    "IDWebSiteCompany" integer NOT NULL,
    "IDWebSite" integer NOT NULL,
    "IDCompany" integer NOT NULL,
    "Parameter" character varying NOT NULL
);


ALTER TABLE "WebSiteCompany" OWNER TO postgres;

--
-- Name: WebSiteCompany_IDWebSiteCompany_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "WebSiteCompany_IDWebSiteCompany_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "WebSiteCompany_IDWebSiteCompany_seq" OWNER TO postgres;

--
-- Name: WebSiteCompany_IDWebSiteCompany_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "WebSiteCompany_IDWebSiteCompany_seq" OWNED BY "WebSiteCompany"."IDWebSiteCompany";


--
-- Name: WebSiteModel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "WebSiteModel" (
    "IDWebSiteModel" integer NOT NULL,
    "IDWebSite" integer NOT NULL,
    "IDModel" integer NOT NULL,
    "Parameter" character varying NOT NULL
);


ALTER TABLE "WebSiteModel" OWNER TO postgres;

--
-- Name: WebSiteModel_IDWebSiteModel_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "WebSiteModel_IDWebSiteModel_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "WebSiteModel_IDWebSiteModel_seq" OWNER TO postgres;

--
-- Name: WebSiteModel_IDWebSiteModel_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "WebSiteModel_IDWebSiteModel_seq" OWNED BY "WebSiteModel"."IDWebSiteModel";


--
-- Name: WebSiteVersion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "WebSiteVersion" (
    "IDWebSiteVersion" integer NOT NULL,
    "IDWebSite" integer NOT NULL,
    "IDVersion" integer NOT NULL,
    "Parameter" character varying NOT NULL
);


ALTER TABLE "WebSiteVersion" OWNER TO postgres;

--
-- Name: WebSiteVersion_IDWebSiteVersion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "WebSiteVersion_IDWebSiteVersion_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "WebSiteVersion_IDWebSiteVersion_seq" OWNER TO postgres;

--
-- Name: WebSiteVersion_IDWebSiteVersion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "WebSiteVersion_IDWebSiteVersion_seq" OWNED BY "WebSiteVersion"."IDWebSiteVersion";


--
-- Name: WebSite_IDWebSite_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "WebSite_IDWebSite_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "WebSite_IDWebSite_seq" OWNER TO postgres;

--
-- Name: WebSite_IDWebSite_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "WebSite_IDWebSite_seq" OWNED BY "WebSite"."IDWebSite";


--
-- Name: Company IDCompany; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Company" ALTER COLUMN "IDCompany" SET DEFAULT nextval('"Company_IDCompany_seq"'::regclass);


--
-- Name: FullModel IDFullModel; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "FullModel" ALTER COLUMN "IDFullModel" SET DEFAULT nextval('"FullModel_IDFullModel_seq"'::regclass);


--
-- Name: Model IDModel; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Model" ALTER COLUMN "IDModel" SET DEFAULT nextval('"Model_IDMod_seq"'::regclass);


--
-- Name: Version IDVersion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Version" ALTER COLUMN "IDVersion" SET DEFAULT nextval('"Version_IDVer_seq"'::regclass);


--
-- Name: WebSite IDWebSite; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSite" ALTER COLUMN "IDWebSite" SET DEFAULT nextval('"WebSite_IDWebSite_seq"'::regclass);


--
-- Name: WebSiteCompany IDWebSiteCompany; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSiteCompany" ALTER COLUMN "IDWebSiteCompany" SET DEFAULT nextval('"WebSiteCompany_IDWebSiteCompany_seq"'::regclass);


--
-- Name: WebSiteModel IDWebSiteModel; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSiteModel" ALTER COLUMN "IDWebSiteModel" SET DEFAULT nextval('"WebSiteModel_IDWebSiteModel_seq"'::regclass);


--
-- Name: WebSiteVersion IDWebSiteVersion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSiteVersion" ALTER COLUMN "IDWebSiteVersion" SET DEFAULT nextval('"WebSiteVersion_IDWebSiteVersion_seq"'::regclass);


--
-- Data for Name: Company; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Company" ("IDCompany", "Name") FROM stdin;
131	BMW
132	Audi
\.


--
-- Data for Name: FullModel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "FullModel" ("IDFullModel", "IDCompany", "IDModel", "IDVersion", "IDLabel") FROM stdin;
432	131	416	195	0
433	131	417	194	1
434	131	417	196	2
435	131	418	194	3
436	131	418	196	4
437	131	419	194	5
438	131	419	196	6
439	131	420	196	7
440	131	421	194	8
441	131	421	196	9
442	131	422	197	10
443	131	423	197	11
444	131	424	197	12
\.


--
-- Data for Name: Model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Model" ("IDModel", "Name") FROM stdin;
416	118d
417	316d
418	318
419	320d
420	325
421	520d
422	x1
423	x3
424	x5
\.


--
-- Data for Name: Version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Version" ("IDVersion", "Name") FROM stdin;
194	caravan
195	saloon
196	sedan
197	suv
\.


--
-- Data for Name: WebSite; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "WebSite" ("IDWebSite", "Name", "URL", "ParameterModel", "ParameterCompany", "ParameterVersion") FROM stdin;
4	Polovni automobili	https://www.polovniautomobili.com/putnicka-vozila/pretraga	model%5B%5D	brand	chassis%5B%5D
\.


--
-- Data for Name: WebSiteCompany; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "WebSiteCompany" ("IDWebSiteCompany", "IDWebSite", "IDCompany", "Parameter") FROM stdin;
\.


--
-- Data for Name: WebSiteModel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "WebSiteModel" ("IDWebSiteModel", "IDWebSite", "IDModel", "Parameter") FROM stdin;
\.


--
-- Data for Name: WebSiteVersion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "WebSiteVersion" ("IDWebSiteVersion", "IDWebSite", "IDVersion", "Parameter") FROM stdin;
\.


--
-- Name: Company_IDCompany_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"Company_IDCompany_seq"', 132, true);


--
-- Name: FullModel_IDFullModel_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"FullModel_IDFullModel_seq"', 444, true);


--
-- Name: Model_IDMod_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"Model_IDMod_seq"', 424, true);


--
-- Name: Version_IDVer_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"Version_IDVer_seq"', 197, true);


--
-- Name: WebSiteCompany_IDWebSiteCompany_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"WebSiteCompany_IDWebSiteCompany_seq"', 1, false);


--
-- Name: WebSiteModel_IDWebSiteModel_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"WebSiteModel_IDWebSiteModel_seq"', 1, false);


--
-- Name: WebSiteVersion_IDWebSiteVersion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"WebSiteVersion_IDWebSiteVersion_seq"', 1, false);


--
-- Name: WebSite_IDWebSite_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"WebSite_IDWebSite_seq"', 4, true);


--
-- Name: FullModel FullModel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "FullModel"
    ADD CONSTRAINT "FullModel_pkey" PRIMARY KEY ("IDFullModel");


--
-- Name: Model Model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Model"
    ADD CONSTRAINT "Model_pkey" PRIMARY KEY ("IDModel");


--
-- Name: Company PKCompany; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Company"
    ADD CONSTRAINT "PKCompany" PRIMARY KEY ("IDCompany");


--
-- Name: Version Version_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Version"
    ADD CONSTRAINT "Version_pkey" PRIMARY KEY ("IDVersion");


--
-- Name: WebSiteCompany WebSiteCompany_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSiteCompany"
    ADD CONSTRAINT "WebSiteCompany_pkey" PRIMARY KEY ("IDWebSiteCompany");


--
-- Name: WebSiteModel WebSiteModel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSiteModel"
    ADD CONSTRAINT "WebSiteModel_pkey" PRIMARY KEY ("IDWebSiteModel");


--
-- Name: WebSiteVersion WebSiteVersion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSiteVersion"
    ADD CONSTRAINT "WebSiteVersion_pkey" PRIMARY KEY ("IDWebSiteVersion");


--
-- Name: WebSite WebSite_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSite"
    ADD CONSTRAINT "WebSite_pkey" PRIMARY KEY ("IDWebSite");


--
-- Name: IDXPrimary; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "IDXPrimary" ON "Company" USING hash ("IDCompany");


--
-- Name: FullModel FKFullModelCompany; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "FullModel"
    ADD CONSTRAINT "FKFullModelCompany" FOREIGN KEY ("IDCompany") REFERENCES "Company"("IDCompany") ON UPDATE CASCADE;


--
-- Name: FullModel FKFullModelModel; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "FullModel"
    ADD CONSTRAINT "FKFullModelModel" FOREIGN KEY ("IDModel") REFERENCES "Model"("IDModel");


--
-- Name: FullModel FKFullModelVersion; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "FullModel"
    ADD CONSTRAINT "FKFullModelVersion" FOREIGN KEY ("IDVersion") REFERENCES "Version"("IDVersion");


--
-- Name: WebSiteCompany FKWebSiteCompanyCompany; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSiteCompany"
    ADD CONSTRAINT "FKWebSiteCompanyCompany" FOREIGN KEY ("IDCompany") REFERENCES "Company"("IDCompany");


--
-- Name: WebSiteCompany FKWebSiteCompanyWebSite; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSiteCompany"
    ADD CONSTRAINT "FKWebSiteCompanyWebSite" FOREIGN KEY ("IDWebSite") REFERENCES "WebSite"("IDWebSite");


--
-- Name: WebSiteModel FKWebSiteModelModel; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSiteModel"
    ADD CONSTRAINT "FKWebSiteModelModel" FOREIGN KEY ("IDModel") REFERENCES "Model"("IDModel");


--
-- Name: WebSiteModel FKWebSiteModelWebSite; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSiteModel"
    ADD CONSTRAINT "FKWebSiteModelWebSite" FOREIGN KEY ("IDWebSite") REFERENCES "WebSite"("IDWebSite");


--
-- Name: WebSiteVersion FKWebSiteVersionVersion; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSiteVersion"
    ADD CONSTRAINT "FKWebSiteVersionVersion" FOREIGN KEY ("IDVersion") REFERENCES "Version"("IDVersion");


--
-- Name: WebSiteVersion FKWebSiteVersionWebSite; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "WebSiteVersion"
    ADD CONSTRAINT "FKWebSiteVersionWebSite" FOREIGN KEY ("IDWebSite") REFERENCES "WebSite"("IDWebSite");


--
-- PostgreSQL database dump complete
--

