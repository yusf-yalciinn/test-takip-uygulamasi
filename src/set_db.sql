CREATE TABLE "users" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"surname"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	"username"	TEXT NOT NULL UNIQUE,
	"login"     INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "lessons" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"examPartId"  INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
	CONSTRAINT FK_examPartContacts FOREIGN KEY (examPartId)
	REFERENCES parts(id) ON DELETE CASCADE
);
CREATE TABLE "analyses" (
	"id"	INTEGER NOT NULL UNIQUE,
	"correctCount"	INTEGER NOT NULL,
	"wrongCount"	INTEGER NOT NULL,
	"gapCount"	INTEGER NOT NULL,
	"Date"  TEXT NOT NULL,
	"lessonId"  INTEGER NOT NULL,
	"userId"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
	CONSTRAINT FK_analyses_userId FOREIGN KEY (userId)
	REFERENCES users(id) ON DELETE CASCADE
	CONSTRAINT FK_lessonContacts FOREIGN KEY (lessonId)
	REFERENCES lessons(id) ON DELETE CASCADE
);
CREATE TABLE "parts" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO parts(name)
VALUES ("TYT");
INSERT INTO parts(name)
VALUES ("AYT");
INSERT INTO lessons(name, examPartId)
VALUES ("Math", 1);
INSERT INTO lessons(name, examPartId)
VALUES ("Physics", 1);
INSERT INTO lessons(name, examPartId)
VALUES ("Chemistry", 1);
INSERT INTO lessons(name, examPartId)
VALUES ("Biology", 1);
INSERT INTO lessons(name, examPartId)
VALUES ("History", 1);
INSERT INTO lessons(name, examPartId)
VALUES ("Geography", 1);
INSERT INTO lessons(name, examPartId)
VALUES ("Philosophy", 1);
INSERT INTO lessons(name, examPartId)
VALUES ("Religious Culture", 1);
INSERT INTO lessons(name, examPartId)
VALUES ("Turkish Language", 1);

INSERT INTO lessons(name, examPartId)
VALUES ("Math", 2);
INSERT INTO lessons(name, examPartId)
VALUES ("Physics", 2);
INSERT INTO lessons(name, examPartId)
VALUES ("Chemistry", 2);
INSERT INTO lessons(name, examPartId)
VALUES ("Biology", 2);
INSERT INTO lessons(name, examPartId)
VALUES ("History", 2);
INSERT INTO lessons(name, examPartId)
VALUES ("Geography", 2);
INSERT INTO lessons(name, examPartId)
VALUES ("Philosophy", 2);
INSERT INTO lessons(name, examPartId)
VALUES ("Religious Culture", 2);
INSERT INTO lessons(name, examPartId)
VALUES ("Turkish Literature", 2);
INSERT INTO lessons(name, examPartId)
VALUES ("English", NULL);
