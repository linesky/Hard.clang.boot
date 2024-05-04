
	.text
	.align	2
	.globl	strslen
	.type	strslen, @function
strslen:
	link.w %fp,#-4
	clr.l -4(%fp)
	jra .L2
.L3:
	addq.l #1,-4(%fp)
.L2:
	move.l -4(%fp),%d0
	move.l 8(%fp),%a0
	add.l %d0,%a0
	move.b (%a0),%d0
	jne .L3
	move.l -4(%fp),%d0
	unlk %fp
	rts
	.size	strslen, .-strslen
	.section	.rodata
.LC0:
	.string	"hello world\n"
.LC1:
	.string	"%s  %d\n"
	.text
	.align	2
	.globl	main
	.type	main, @function
main:
	link.w %fp,#-4
	move.l #.LC0,-4(%fp)
	move.l -4(%fp),-(%sp)
	jsr strslen
	addq.l #4,%sp
	move.l %d0,-(%sp)
	move.l -4(%fp),-(%sp)
	pea .LC1
	jsr printf
	lea (12,%sp),%sp
	clr.l %d0
	unlk %fp
	rts

