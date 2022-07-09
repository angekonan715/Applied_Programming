import sqlite3

db_file = sqlite3.connect("student.db")
cur = db_file.cursor()

#insert data into our 
cur.execute("""
INSERT INTO student_info(fname, lname, email, phone) VALUES
    ('Ange', 'Kouadio', 'angek@gmail.com', '0749715895'),
    ('Eugene', 'Loukou', 'loukoue22@gmail.com', '0545715893'),
    ('Etienne', 'Zoro', 'ettienZoro@gmail.com', '0749715812'),
    ('asko', 'Kouadio', 'askok@gmail.com', '0749435895'),
    ('Jean', 'Ange', 'angoj@gmail.com', '0749711235'),
    ('Stephanie', 'Konan', 'stephk@gmail.com', '0576715895'),
    ('felicite', 'djeha', 'djehaF@gmail.com', '0504715895'),
    ('Diallo', 'Socrate', 'socra34@gmail.com', '0745715895'),
    ('Gervais', 'Kone', 'gkone@gmail.com', '0549715895'),
    ('Angie', 'Kouame', 'angieKouame@gmail.com', '0777715895'),
    ('Ange', 'ahouto', 'ahoutoa@gmail.com', '0709153091'),
    ('ange', 'Kobenan', 'angek66@gmail.com', '0749815895'),
    ('Ange', 'Kouadio', 'angek03@gmail.com', '0749315895'),
    ('sekou', 'Toure', 'sekouT23@gmail.com', '0123715895'),
    ('Amadi', 'kortor', 'amadiKorto@gmail.com', '0749711234')     
""")

cur.execute("""
INSERT INTO emergency_contact(parents_tutor_name, eEmail, ePhone) VALUES
('leanie Akissi', 'leonieA@gmail.com', '0748053677'),
('Osoa Beatrice', 'ousoa@gmail.com',  '0444567898'),
('marlene Kouassi', 'marlenekA@gmail.com', '0464567898'),
('Kouadio Remi', 'remik233@gmail.com', '0444567897'),
('Nadege Akissi', 'nadegeA@gmail.com', '0748153677'),
('Siloue Jonas', 'jojo21@gmail.com', '0748053612'),
('Mariam Coulibali', 'colibaliem12@gmail.com', '0748000677'),
('soubile kouassi', 'sousoub@gmail.com', '0128053677'),
('margerette choupette', 'choup08@gmail.com', '0848053677'),
('angelique Matha', 'mataEng56@gmail.com', '0749053677'),
('Kone siriki', 'siriki@gmail.com', '0444567812'),
('lIsamel Issac', 'ismo@gmail.com', '0444533898'),
('chwukwu rolisse', 'chwukwuR@gmail.com', '0545053677'),
('Sonia Aya', 'yayas@gmail.com', '07071853677'),
('memorig bridge', 'bridememo@gmail.com', '148053677')
""")

cur.execute("""
INSERT INTO student_gpa(id, emergency_id, gpa) VALUES
(1, 1, 3.7),
(2, 2, 3.4),
(3, 3, 4.0),
(4, 4, 3.3),
(5, 5, 3.1),
(6, 6, 2.7),
(7, 7, 3.6),
(8, 8, 1.5),
(9, 9, 2.5),
(10, 10, 2.9),
(11, 11, 4.0),
(12, 12, 3.9),
(13, 13, 2.4),
(14, 14, 3.2),
(15, 15, 1.7)    
""")

db_file.commit()
db_file.close()