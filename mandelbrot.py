import PIL
import PIL.Image
import time
import os
import math
import colorsys

# Nathan Brei
# Sunday, 16 October 2011

def mandelbrot(xres=600, yres=400, 
          xmin=-2, xmax=1, ymin=-1, ymax=1, 
          threshold=30, escape=10, 
          fractalfcn=lambda z,a: z**2+a, 
          colorfcn=lambda color: colorsys.hls_to_rgb(color*100/360., color, 1),
          innercolor=(0,0,0),
          destination='~/Desktop/mandelbrot.png'
          ):

    'Generates fractal images. Sorry about using PIL.'
   
    def zauberkraft(x,y):
        'Generate the color value for a specified pixel'
        a = complex(xmin+x*dx, ymin+y*dy)
        z = count = 0
        while(abs(z)<escape and count<threshold):
            z = fractalfcn(z,a)
            count += 1
        if count==threshold:
            return innercolor
        else:
            color = (count+0.0)/threshold    # in [0,1]
            return tuple([int(255*i) for i in colorfcn(color)])

    t = time.time()
    dx = (xmax-xmin-0.0)/xres
    dy = (ymax-ymin-0.0)/yres

    im = PIL.Image.new('RGB',(xres,yres))
    im.putdata([zauberkraft(x,y) for y in range(yres) for x in range(xres)])
    im.save(os.path.expanduser(destination))
    os.system('open '+destination)
    print '{0} generated in {1:.3} seconds.'.format(destination,time.time()-t)


mandelbrot()

# Samples

def example_fractalfcns():
    mandelbrot(xres=600,yres=600,xmin=-2,xmax=2,ymin=-2,ymax=2,fractalfcn=lambda z,a: z**6+a, destination='~/Desktop/multibrot-6.png')
    mandelbrot(xres=600,yres=600,xmin=-2,xmax=2,ymin=-2,ymax=2,fractalfcn=lambda z,a: (z.conjugate())**2+a, colorfcn=lambda c: colorsys.hls_to_rgb(c*100/360.,c,1), destination='~/Desktop/tricorn.png')
    mandelbrot(xres=600,yres=600,xmin=-2,xmax=2,ymin=-2,ymax=2,fractalfcn=lambda z,a: (complex(abs(z.real),abs(z.imag))**2+a), destination='~/Desktop/burningship.png')

def example_colorfcns():
    mandelbrot(colorfcn=lambda c: (0,0,c), innercolor=(0,0,0), destination='~/Desktop/a.png')
    mandelbrot(colorfcn=lambda c: colorsys.hls_to_rgb(math.exp(c),.5,1), threshold=100,destination='~/Desktop/b.png')
    mandelbrot(colorfcn=lambda c: colorsys.hls_to_rgb(math.exp(c*100/360.), c, 1),innercolor=(255,255,255), threshold=75,destination='~/Desktop/c.png')
    mandelbrot(colorfcn=lambda c: colorsys.hls_to_rgb(c, c, 1),threshold=75,destination='~/Desktop/d.png')
    mandelbrot(colorfcn=lambda c: colorsys.hls_to_rgb(c, (1+math.sin(50*c))/2, 1),threshold=200,destination='~/Desktop/e.png')

