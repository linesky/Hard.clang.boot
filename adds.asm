

	.text
	.align	2
	.globl	adds
	.type	adds, @function
adds:
	link.w %fp,#0
	move.l 8(%fp),%d0
	add.l 12(%fp),%d0
	unlk %fp
	rts
	.size	adds, .-adds
	.section	.rodata
.LC0:
	.string	"\033[43;37m%d....\n"
	.text
	.align	2
	.globl	main
	.type	main, @function
main:
	link.w %fp,#-12
	moveq #10,%d0
	move.l %d0,-4(%fp)
	moveq #10,%d0
	move.l %d0,-8(%fp)
	move.l #.LC0,-12(%fp)
	move.l -8(%fp),-(%sp)
	move.l -4(%fp),-(%sp)
	jsr adds
	addq.l #8,%sp
	move.l %d0,-(%sp)
	move.l -12(%fp),-(%sp)
	jsr printf
	addq.l #8,%sp
	clr.l %d0
	unlk %fp
	rts

