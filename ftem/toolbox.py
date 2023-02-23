import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

class gravityField:
    def __init__(self, mass):
        self.mass = mass
        self.G = 6.67e-11
        
    def vectorField(self, X, Y, Z=None, eqs=False):
        # SI to cgs system conversion
        mGal = 1e5
        
        if not Z:
            # sympy symbols
            c, R, G, m = sy.symbols('c, R, G, m')
            
            # analytic equations
            # adapted from Blakely's SPHERE subroutine
            a_gr = - G * m / R**3
            a_gxy = - G * m * c / R**3
            
            # analytic to numerical representation
            n_gr = sy.lambdify(R, a_gr.subs({G:self.G, m:self.mass}))
            n_gx = sy.lambdify([c, R], a_gxy.subs({G:self.G, m:self.mass}))
            n_gy = sy.lambdify([c, R], a_gxy.subs({G:self.G, m:self.mass}))
            
            # distance-r vector
            # added noise is experimental after trial and error
            # where the ratio of such noise was calibrated such
            # that the field neither explodes at r = 0 nor
            # is not visible as a whole within the range
            r = np.hypot(X, Y) + X.max()/3 * np.ones_like(X)
            
            # numerical vector components of field
            # mGal and km2m conversions are taken from Blakely's
            # SPHERE subroutine
            gr = n_gr(r) * mGal
            gx = n_gx(X, r) * mGal
            gy = n_gy(Y, r) * mGal
            
            if eqs:
                x, y = sy.symbols('x y')
                display(a_g.subs({c:x}) + a_g.subs({c:y}))
                
            return gr, gx, gy
        else:
            pass
    
    def plotVectorField2D(self, lim, samples, lines=True, field=False, cmap='viridis', color='black', aspect='equal'):
        X, Y = np.meshgrid(np.linspace(-lim, lim, samples),
                           np.linspace(-lim, lim, samples))
        G_R, G_X, G_Y = self.vectorField(X, Y)
        
        if samples >= 80:
            s = np.floor(np.power(samples, 1/3))
        else:
            s = 1
        skip = (slice(None, None, s), slice(None, None, s))
        
        if lines and not field:    
            plt.quiver(X[skip], Y[skip], G_X[skip], G_Y[skip])
            plt.gca().set_aspect(aspect)
        elif lines and field:
            plt.contourf(X, Y, G_R, samples, cmap=cmap)
            plt.quiver(X[skip], Y[skip], G_X[skip], G_Y[skip], color=color)
            plt.gca().set_aspect(aspect)
        elif not lines and field:
            plt.contourf(X, Y, G_R, samples, cmap=cmap)
            plt.gca().set_aspect(aspect)
        plt.title('Campo gravitacional 2D')
        plt.show()
        
class magneticField:
    def __init__(self, I):
        self.I = I
        self.mu0 = 4 * np.pi * 1e-7
        
    def vectorField(self, X, Y, Z=None, eqs=False):
        if not Z:
            # sympy symbols
            I, mu0, s, theta = sy.symbols('I mu_0 s theta')
            
            # analytic equations
            # adapted from Tejero's notes
            a_Bp = mu0 * I / (2 * sy.pi * s)
            a_Bx = - mu0 * I / (2 * sy.pi * s) * sy.sin(theta)
            a_By = mu0 * I / (2 * sy.pi * s) * sy.cos(theta)
            
            # analytic to numerical representation
            n_Bp = sy.lambdify([I, s], a_Bp.subs({mu0:self.mu0}))
            n_Bx = sy.lambdify([s, theta, I], a_Bx.subs({mu0:self.mu0}))
            n_By = sy.lambdify([s, theta, I], a_By.subs({mu0:self.mu0}))
            
            # distance-r vector
            # added noise is experimental after trial and error
            # where the ratio of such noise was calibrated such
            # that the field neither explodes at r = 0 nor
            # is not visible as a whole within the range
            S = np.hypot(X, Y) + X.max()/2 * np.ones_like(X)
            T = np.arctan2(Y, X)
            
            # numerical vector components of field
            Bp = n_Bp(self.I, S)
            Bx = n_Bx(S, T, self.I)
            By = n_By(S, T, self.I)
            
            if eqs:
                display(a_Bx + a_By)
                
            return Bp, Bx, By
        else:
            pass
                
    # Yet to implement: 3D Vector Field and plot
    
    def plotVectorField2D(self, lim, samples, lines = True, field = False, cmap='viridis', color='black', aspect='equal'):
        X, Y = np.meshgrid(np.linspace(-lim, lim, samples),
                           np.linspace(-lim, lim, samples))
        B_P, B_X, B_Y = self.vectorField(X, Y)
        
        if samples >= 80:
            s = np.floor(np.power(samples, 1/3))
        else:
            s = 1
        skip = (slice(None, None, s), slice(None, None, s))
        
        if lines and not field:    
            plt.quiver(X[skip], Y[skip], B_X[skip], B_Y[skip])
            plt.gca().set_aspect(aspect)
        elif lines and field:
            plt.contourf(X, Y, B_P, samples, cmap=cmap)
            plt.quiver(X[skip], Y[skip], B_X[skip], B_Y[skip], color=color)
            plt.gca().set_aspect(aspect)
        elif not lines and field:
            plt.contourf(X, Y, B_P, samples, cmap=cmap)
            plt.gca().set_aspect(aspect)
        plt.title('Campo magnético 2D')
        plt.show()
        
if __name__ == '__main__':
    
    g = gravityField(10)
    print(g.G)
    
    samples = 30
    lim = 10
    g.plotVectorField2D(lim, samples)
    g.plotVectorField2D(lim, samples, lines=False, field=True)
    g.plotVectorField2D(lim, samples, True, True)
    
    b = magneticField(10)
    print(b.mu0)
    
    samples = 30
    lim = 10
    b.plotVectorField2D(lim, samples)
    b.plotVectorField2D(lim, samples, lines=False, field=True)
    b.plotVectorField2D(lim, samples, True, True)