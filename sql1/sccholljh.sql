--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

-- Started on 2019-12-14 09:44:02

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 205 (class 1259 OID 16446)
-- Name: class; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.class (
    class_id integer,
    number integer,
    number_pupils integer
);


ALTER TABLE public.class OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16437)
-- Name: lesson; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lesson (
    lesson_id integer,
    title character varying,
    themes character varying,
    cabinet integer,
    day character varying,
    class_id integer
);


ALTER TABLE public.lesson OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16443)
-- Name: lesson_teacher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lesson_teacher (
    teacher_id integer,
    lesson_id integer
);


ALTER TABLE public.lesson_teacher OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16431)
-- Name: teacher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teacher (
    teacher_id integer,
    first_name character varying,
    last_name character varying,
    old integer,
    salary integer,
    home_address character varying
);


ALTER TABLE public.teacher OWNER TO postgres;

--
-- TOC entry 2828 (class 0 OID 16446)
-- Dependencies: 205
-- Data for Name: class; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.class (class_id, number, number_pupils) FROM stdin;
1	1	22
2	2	27
3	3	32
4	4	33
5	2	25
\.


--
-- TOC entry 2826 (class 0 OID 16437)
-- Dependencies: 203
-- Data for Name: lesson; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lesson (lesson_id, title, themes, cabinet, day, class_id) FROM stdin;
1	Muzic	...	67	monday	4
2	Painting	...	25	tuesday	3
3	Math	...	84	friday	3
\.


--
-- TOC entry 2827 (class 0 OID 16443)
-- Dependencies: 204
-- Data for Name: lesson_teacher; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lesson_teacher (teacher_id, lesson_id) FROM stdin;
1	2
2	3
3	1
\.


--
-- TOC entry 2825 (class 0 OID 16431)
-- Dependencies: 202
-- Data for Name: teacher; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teacher (teacher_id, first_name, last_name, old, salary, home_address) FROM stdin;
1	Peter	Karr	34	400	kharkiv, peremohy street
2	Sarah	Li	56	800	kharkiv, sumska street, 15
3	Richard	Torn	23	250	kharkiv, gimnaziyna naberezhna, 3
\.


-- Completed on 2019-12-14 09:44:02

--
-- PostgreSQL database dump complete
--

