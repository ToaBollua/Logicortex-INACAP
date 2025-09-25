BEGIN;
--
-- Create model Reto
--
CREATE TABLE "core_reto" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(200) NOT NULL, "enunciado" text NOT NULL, "respuesta_correcta" varchar(255) NOT NULL, "dificultad" varchar(10) NOT NULL, "puntuacion" integer NOT NULL, "fecha_publicacion" datetime NOT NULL);
--
-- Create model CustomUser
--
CREATE TABLE "core_customuser" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "puntuacion" integer NOT NULL);
CREATE TABLE "core_customuser_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customuser_id" bigint NOT NULL REFERENCES "core_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "core_customuser_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customuser_id" bigint NOT NULL REFERENCES "core_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model RespuestaUsuario
--
CREATE TABLE "core_respuestausuario" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "respuesta_enviada" varchar(255) NOT NULL, "es_correcta" bool NOT NULL, "fecha_intento" datetime NOT NULL, "usuario_id" bigint NOT NULL REFERENCES "core_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "reto_id" bigint NOT NULL REFERENCES "core_reto" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "core_customuser_groups_customuser_id_group_id_7990e9c6_uniq" ON "core_customuser_groups" ("customuser_id", "group_id");
CREATE INDEX "core_customuser_groups_customuser_id_976bc4d7" ON "core_customuser_groups" ("customuser_id");
CREATE INDEX "core_customuser_groups_group_id_301aeff4" ON "core_customuser_groups" ("group_id");
CREATE UNIQUE INDEX "core_customuser_user_permissions_customuser_id_permission_id_49ea742a_uniq" ON "core_customuser_user_permissions" ("customuser_id", "permission_id");
CREATE INDEX "core_customuser_user_permissions_customuser_id_ebd2ce6c" ON "core_customuser_user_permissions" ("customuser_id");
CREATE INDEX "core_customuser_user_permissions_permission_id_80ceaab9" ON "core_customuser_user_permissions" ("permission_id");
CREATE INDEX "core_respuestausuario_usuario_id_8541a498" ON "core_respuestausuario" ("usuario_id");
CREATE INDEX "core_respuestausuario_reto_id_e6ae8a16" ON "core_respuestausuario" ("reto_id");
COMMIT;
