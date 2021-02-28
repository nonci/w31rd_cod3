### Functional one-line implementation of Newton's method; parameters are separated only for convenience.

PARS = lambda _:4+8*_**2-_**4, lambda _:16*_-4*_**3, 3, 100, .1E-8  # F, dF, X0, N_ITER, EPSILON

print((lambda a:a(a,*PARS))(lambda newton,f,fp,x0,iter,eps:x0 if not iter or abs(f(x0))<eps else newton(newton,f,fp,x0-(f(x0)/fp(x0)),iter-1,eps)))
