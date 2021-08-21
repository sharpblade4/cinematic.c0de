(*  
  Jurassic Park (1993)   -    00:54:32  

  Sources:
  - MPW 3.4 :: Examples :: DerezPict (by Tom Taylor)   [not reconstructed]
  - MPW 3.4 :: Examples :: CheckOutActive              [not reconstructed]
  - MPW 3.4 :: HyperXExamples :: PExamples :: Reduce.p (by Dan Allen)
*)

h := NewHandle(GetHandleSize(params[1]));
 IF h = NIL THEN EXIT(EntryPoint);
p := params[1]^;
q := h^;
WHILE p^ <> 0 DO
	IF (p^ =tab) OR (p^ = space) THEN
		BEGIN
			REPEAT
				p := POINTER(ORD(p)+1);
			UNTIL (p^ <> tab) AND (p^ <> space);
			q^ := space;
			q := POINTER(ORD(q)+1);
		END
	ELSE
		BEGIN
			q^ := p^;
			p := POINTER(ORD(p)+1);
			q := POINTER(ORD(q)+1);
		END;
	q^ := 0;
	returnValue := h;
