.PROGRAM main()
  ; *******************************************************************
  ;
  ; Program:      main 4.4
  ; Comment:      
  ; Author:       SIGMA
  ;
  ; Date:         3/25/2022
  ;
  ; *******************************************************************
  ;
  leinght = 45.2
  d_h = 100
  
  SPEED 10 MM/S
  JMOVE #home_point
  
  DRIVE 6, 90
  BREAK
  DRIVE 6, -90
  BREAK
  
  LMOVE ASM_point
  
  DRAW 102,10,-70
  BREAK
  DRAW 0, 0,-40
  BREAK
  DRAW 0, 0,40
  BREAK
  
  DRAW -22, -6, 0
  BREAK
  DRAW 0, 0,-43
  BREAK
  DRAW 0, 0,43
  BREAK
  
  DRAW -13.5, -14, 0
  BREAK
  DRAW 0, 0,-43
  BREAK
  DRAW 0, 0,43
  BREAK
  
  JMOVE ASM_point
  
  DRIVE 5, -90
  BREAK
  
  DRAW -115, 0, -100
  BREAK
  
  DRAW 0, -8, -173
  BREAK
  DRAW 38, 0, 0
  BREAK
  
  
  DRAW -38, 0, 0
  BREAK
  DRAW 0, 15, -21
  BREAK
  DRAW 38, 0, 0
  BREAK
  
  DRAW -38, 0, 0
  BREAK
  DRAW 0, -20, -17
  BREAK
  DRAW 38, 0, 0
  BREAK
  
  DRAW -38, 0, 0
  BREAK
  DRAW 0, 22, -20
  BREAK
  DRAW 38, 0, 0
  BREAK
  
  DRAW -45, 0, 0
  BREAK
  DRAW -45, 0, 200
  BREAK
  
  JMOVE #home_point
.END
.PROGRAM Comment___ () ; Comments for IDE. Do not use.
	; @@@ PROJECT @@@
	; @@@ HISTORY @@@
	; @@@ INSPECTION @@@
	; @@@ CONNECTION @@@
	; KROSET R01
	; 127.0.0.1
	; 9105
	; @@@ PROGRAM @@@
	; MainProg:main
	; 0:main
	; @@@ TRANS @@@
	; ASM_point 
	; STG_point 
	; INS_point 
	; Coord 
	; @@@ JOINTS @@@
	; @@@ REALS @@@
	; @@@ STRINGS @@@
	; @@@ INTEGER @@@
	; @@@ SIGNALS @@@
	; @@@ TOOLS @@@
	; @@@ BASE @@@
	; @@@ FRAME @@@
	; @@@ BOOL @@@
.END
.TRANS
ASM_point 600.000000 0.000000 0.000000 -90.000008 180.000000 0.000000
STG_point 300.000000 500.000000 0.000000 -180.000000 180.000000 0.000000
INS_point 300.000763 -500.000000 0.003110 -180.000000 180.000000 0.000000
Coord 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000
.END
.JOINTS
#service_point 123.676178 -10.981930 -136.281784 -160.887314 -36.845402 -105.499237
#home_point 90.000000 -11.732300 -136.005768 -180.000000 55.726089 -89.999489
.END
