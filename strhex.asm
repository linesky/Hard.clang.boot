
	.text
	.section	.rodata
.LC0:
	.string	"0123456789ABCDEF0123456789ABCDEF"
	.text
	.align	2
	.globl	strshex
	.type	strshex, @function
strshex:
	link.w %fp,#-24
	move.l 12(%fp),-4(%fp)
	moveq #8,%d0
	move.l %d0,-8(%fp)
	clr.l -12(%fp)
	moveq #16,%d0
	move.l %d0,-16(%fp)
	moveq #15,%d0
	move.l %d0,-20(%fp)
	move.l #.LC0,-24(%fp)
	move.l -8(%fp),%d0
	move.l 8(%fp),%a0
	add.l %d0,%a0
	clr.b (%a0)
	moveq #7,%d0
	move.l %d0,-8(%fp)
	jra .L2
.L3:
	move.l -4(%fp),%d0
	and.l -20(%fp),%d0
	move.l %d0,-12(%fp)
	move.l -12(%fp),%d0
	move.l -24(%fp),%a1
	add.l %d0,%a1
	move.l -8(%fp),%d0
	move.l 8(%fp),%a0
	add.l %d0,%a0
	move.b (%a1),%d0
	move.b %d0,(%a0)
	move.l -4(%fp),%d0
	divsl.l -16(%fp),%d1:%d0
	move.l %d0,-4(%fp)
	subq.l #1,-8(%fp)
.L2:
	tst.l -8(%fp)
	jge .L3
	nop
	nop
	unlk %fp
	rts
	.size	strshex, .-strshex
	.section	.rodata
.LC1:
	.string	"%s  \n"
	.text
	.align	2
	.globl	main
	.type	main, @function
main:
	link.w %fp,#-56
	clr.l -4(%fp)
	move.l #305419896,-(%sp)
	lea (-54,%fp),%a0
	move.l %a0,-(%sp)
	jsr strshex
	addq.l #8,%sp
	lea (-54,%fp),%a0
	move.l %a0,-(%sp)
	pea .LC1
	jsr printf
	addq.l #8,%sp
	clr.l %d0
	unlk %fp
	rts

