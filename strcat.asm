#NO_APP
	.file	"strcat.c"
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
	.align	2
	.globl	strcats
	.type	strcats, @function
strcats:
	link.w %fp,#-8
	clr.l -4(%fp)
	move.l 8(%fp),-(%sp)
	jsr strslen
	addq.l #4,%sp
	move.l 8(%fp),%d1
	add.l %d0,%d1
	move.l %d1,-8(%fp)
	jra .L6
.L7:
	move.l -4(%fp),%d0
	move.l 12(%fp),%a1
	add.l %d0,%a1
	move.l -4(%fp),%d0
	move.l -8(%fp),%a0
	add.l %d0,%a0
	move.b (%a1),%d0
	move.b %d0,(%a0)
	addq.l #1,-4(%fp)
.L6:
	move.l -4(%fp),%d0
	move.l 12(%fp),%a0
	add.l %d0,%a0
	move.b (%a0),%d0
	jne .L7
	move.l -4(%fp),%d0
	move.l 12(%fp),%a1
	add.l %d0,%a1
	move.l -4(%fp),%d0
	move.l -8(%fp),%a0
	add.l %d0,%a0
	move.b (%a1),%d0
	move.b %d0,(%a0)
	move.l -4(%fp),%d0
	unlk %fp
	rts
	.size	strcats, .-strcats
	.section	.rodata
.LC0:
	.string	"hello "
.LC1:
	.string	"world \n "
.LC2:
	.string	"%s  \n"
	.text
	.align	2
	.globl	main
	.type	main, @function
main:
	link.w %fp,#-52
	clr.b -50(%fp)
	pea .LC0
	lea (-50,%fp),%a0
	move.l %a0,-(%sp)
	jsr strcats
	addq.l #8,%sp
	pea .LC1
	lea (-50,%fp),%a0
	move.l %a0,-(%sp)
	jsr strcats
	addq.l #8,%sp
	lea (-50,%fp),%a0
	move.l %a0,-(%sp)
	pea .LC2
	jsr printf
	addq.l #8,%sp
	clr.l %d0
	unlk %fp
	rts
	.size	main, .-main
	.ident	"GCC: (Debian 10.2.1-6) 10.2.1 20210110"
	.section	.note.GNU-stack,"",@progbits
