
	.text
	.align	2
	.globl	cfill
	.type	cfill, @function
cfill:
	link.w %fp,#-16
	move.l 12(%fp),%d0
	move.b %d0,%d0
	move.b %d0,-14(%fp)
	clr.l -4(%fp)
	move.l 8(%fp),-(%sp)
	jsr strlen
	addq.l #4,%sp
	lsr.l #1,%d0
	move.l %d0,-8(%fp)
	move.l 16(%fp),%d0
	move.l %d0,%d1
	add.l %d1,%d1
	subx.l %d1,%d1
	neg.l %d1
	add.l %d1,%d0
	asr.l #1,%d0
	move.l %d0,-12(%fp)
	clr.l -4(%fp)
	jra .L2
.L3:
	move.l -8(%fp),%d0
	sub.l -12(%fp),%d0
	add.l -4(%fp),%d0
	move.l 8(%fp),%a0
	add.l %d0,%a0
	move.b -14(%fp),(%a0)
	addq.l #1,-4(%fp)
.L2:
	move.l -4(%fp),%d0
	cmp.l 16(%fp),%d0
	jlt .L3
	nop
	nop
	unlk %fp
	rts
	.size	cfill, .-cfill
	.section	.rodata
.LC0:
	.string	"%s \n"
	.text
	.align	2
	.globl	main
	.type	main, @function
main:
	link.w %fp,#-80
	lea (-80,%fp),%a0
	move.l #1751477356,(%a0)
	addq.l #4,%a0
	move.l #1864398703,(%a0)
	addq.l #4,%a0
	move.l #1919706122,(%a0)
	addq.l #4,%a0
	clr.l (%a0)
	addq.l #4,%a0
	move.l %a0,%d1
	moveq #64,%d0
	move.l %d0,-(%sp)
	clr.l -(%sp)
	move.l %d1,-(%sp)
	jsr memset
	lea (12,%sp),%sp
	pea 3.w
	pea 46.w
	lea (-80,%fp),%a0
	move.l %a0,-(%sp)
	jsr cfill
	lea (12,%sp),%sp
	lea (-80,%fp),%a0
	move.l %a0,-(%sp)
	pea .LC0
	jsr printf
	addq.l #8,%sp
	clr.l %d0
	unlk %fp
	rts

