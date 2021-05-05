-- The Girl with the Dragon Tattoo  -  1:20:24

SELECT DISTINCT v.fname, v.lname, i.year, i.location, i.report_file FROM Incident AS i LEFT JOIN Victim AS v on v.incident_id = i.id LE
FT JOIN Keyword AS k ON k.incident_id = i.id WHERE i.year BETWEEN 1947 AND 1966 AND i.type = 'HOMICIDE' AND v.sex = 'F' AND i.status = 'UNSOLV
ED' AND (k.keyword IN ('rape', 'decapitation', 'dismemberment', 'fire', 'altar', 'priest', 'prostitute') OR v.fname IN ('Mari', 'Magda') OR SU
BSTR(v.fname, 1, 1) = 'R' AND SUBSTR(v.lname, 1, 1) = 'L');
