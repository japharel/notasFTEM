import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

class gravityField:
    def __init__(self, mass):
        self.mass = mass
        self.G = 6.67e-11
        
    def vectorField(self, X, Y, Z = None, eqs = False):
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
    
    def plotVectorField2D(self, lim, samples, lines = True, field = False, cmap='viridis', color='black', aspect='equal'):
        X, Y = np.meshgrid(np.linspace(-lim, lim, samples),
                           np.linspace(-lim, lim, samples))
        G_R, G_X, G_Y = self.vectorField(X, Y)
        
        if lines and not field:
            plt.quiver(X, Y, G_X, G_Y)
            plt.gca().set_aspect(aspect)
        elif lines and field:
            plt.contourf(X, Y, G_R, samples, cmap=cmap)
            plt.quiver(X, Y, G_X, G_Y, color=color)
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
        
    def vectorField(self, x, y, z = None):
        if not z:
            r = np.hypot(x, y)# + x.max() / 3 * np.ones_like(x)
            k = self.mu0 * self.I / (2 * np.pi)
            
            b_x = - k * y / r
            b_y = k * x / r
            
            return (b_x, b_y)
        else:
            pass
                
    # Yet to implement: 3D Vector Field and plot
    
    def plotVectorField2D(self, lim, samples, field = False):
        X, Y = np.meshgrid(np.linspace(-lim, lim, samples),
                           np.linspace(-lim, lim, samples))
        B_X, B_Y = self.vectorField(X, Y)
        
        if field:
            plt.quiver(X, Y, B_X, B_Y)
            plt.imshow(B_X + B_Y, origin = 'lower', 
                       extent = (X.min(), X.max(), Y.min(), Y.max()))
        else:
            plt.quiver(X, Y, B_X, B_Y)
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
    b.plotVectorField2D(lim, samples, field=True)