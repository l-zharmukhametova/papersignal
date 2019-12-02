# By Kent Quirk, April 2018
# SVG writer; outputs lines and text

# Although SVG is an XML-based language, XML manipulation is annoyingly complicated for what we need
# to do here, so we're just going to treat set things up with a template and embed strings.

# This system exists generate SVG files -- in particular to use with the Glowforge laser cutter. One thing that
# makes using the Glowforge UI work better is for SVGs to use closed paths rather than a semi-random selection of
# lines. Consequently, what this driver does is collect all of the line commands and record them; on the
# save call it concatenates them together into a set of paths.

from string import Template

tmpl_svg = Template("""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="${point_width}pt" height="${point_height}pt" version="1.1"
    viewBox="0 0 ${point_width} ${point_height}"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xml:space="preserve"
    xmlns:serif="http://www.serif.com/"
    style="fill-rule:evenodd;clip-rule:evenodd;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:1.5;">
${contents}
</svg>
""")

tmpl_path = Template("""      
""")
#<path d="${path}" style="fill:#ffcfd9 ;stroke:${stroke_color};stroke-width:${stroke_pixels}px;"/>
#73.637332

tmpl_rect = Template("""    
<path
       style="fill:#ffcfd9 ;stroke:#ff0000;stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       d="M 35.075403,35.500069 
       h 51.419828 
       h ${w}
       v 15.827727 
       l 5.079998,-5.08 
       h 5.667727 
       l 10.160004,10.16 
       V ${y}
       L ${p},${l}
       h -5.667727 
       l -5.079998,-5.079997 
       v 39.080373 v ${f} 
       l -5.079998,5.08 
       h -41.25983 
       h ${ww}
       l -5.08,-5.08 
       V ${vlu} 
       l -5.079999,5.079997 
       h -5.667728 
       l -10.16,-10.159997 
       V 56.407796 
       l 10.16,-10.16 
       h 5.667728 
       l 5.079999,5.08 z"
       id="path3702"
       />
    <path
         id="path126"
         d="M 20.317748,52.384656 h 81.419828 h ${w} V ${y} v 5 h ${wh} h -30 L 20.317748,52.384656"
         style="fill:none;stroke:#000000;stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;stroke-dasharray:2, 1;stroke-opacity:1" />
    <path
         id="path126"
         d="M 35.317748,${yh} h 51.419828 h ${w}"
         style="fill:none;stroke:#000000;stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;stroke-dasharray:2, 1;stroke-opacity:1" />
    <path
         id="path126"
         d="M 35.317748,${yhh} h 51.419828 h ${w}"
         style="fill:none;stroke:#000000;stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;stroke-dasharray:2, 1;stroke-opacity:1" />
       
       


<g transform="translate(0.0,100.0)">
      <path
       style="fill:#ffcfd9;
       stroke:#ff0000;

       stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       d="M 200.50192,72.018055 
       V 190.41647 
       h ${f} 
       h 40.29176 
       l -8.1549,8.1549 
       v 23.84754 
       v ${f} 
       l 8.1549,8.35507 
       h 68.67658 
       h ${w}
       l 8.68944,-8.33998 
       v -5.54011 
       v ${nf}
       h -8.5784 
       v -13.21383 
       h 8.32805 
       v -5.10787 
       v ${nf}
       l -7.92239,-8.15436 
       h 12.90713 
       h ${fdt} 
       v -10.70726 
       h 13.97417 
       v 10.70929 
       h 13.17392 
       h ${fdt} 
       l 8.41951,8.41951 
       v 0 h 51.62438 
       h ${w}
       l 16.9511,-16.9511 
       V 80.609115 
       L ${hhw},63.661556 
       h -51.62168 
       h ${nw}
       l -8.46784,8.324309 -8.24794,-8.324309 
       h -23.85304 
       h ${ndf} 
       l -8.09573,8.102228 
       V ${vll} 
       h -68.84519 
       h ${nw}
       v 40.307751 
       v ${f}
       l -8.09312,-8.214645 
       h -23.83931 
       h ${ndf}
       z"
       id="path470bigpath"
       />

       <path
       style="fill:none;stroke:#000000;
       
       stroke-dasharray:2, 1;
       stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       d="M 200.53679,71.99401 H ${hhhd} V 190.1331 H ${hhd} V 71.985865"
       id="path459"
       /><path
       style="fill:none;stroke:#000000;

       stroke-dasharray:2, 1;
       stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       d="M ${dff},72.018055 V 190.35518 h 68.74827 h ${w} V 71.763784"
       id="path461"
       /><path
       style="fill:none;stroke:#000000;
       
       stroke-dasharray:2, 1;
       stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       d="m ${bbf},190.41647 v 40.35751 v ${f}"
       id="path463"
       /><path
       style="fill:none;stroke:#000000;
       
       stroke-dasharray:2, 1;
       stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       d="m ${bbbf},190.35518 v 13.1028 v ${fdt} "
       id="path465"
       />
       
       <path
       style="fill:none;stroke:#000000;
       stroke-dasharray:2, 1;
       stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       d="m ${bbbf},${stlt} v 13.86288 v ${fdt}"
       id="path467"/>
       </g>
   """)

#ffcfd9 
#v ${y}
#<rect x="${x}" y="${y}" width="${w}" height="${h}"/>
#${x}
PIXEL_TO_POINT = 0.75


class SVGDoc(object):

    def __init__(self, filename):
        self.comments = []
        self.elements = []
        self.paths = []
        self.firsts = set()
        self.filename = filename
        self.stroke_color = "black"
        self.line_width = 0.5  # default is mm so we need to convert
        self.page_size = [0, 0]
        self.author = ''

    def setPageSize(self, page_size):
        self.page_size = page_size

    def setAuthor(self, author):
        self.author = author

    def setStrokeColor(self, col):
        self.stroke_color = col

    def setLineWidth(self, lw):
        self.line_width = lw

    def drawString(self, x, y, st):
        # String must be free of metacharacters
        self.comments.append((x, y, st))

    def rect(self, x, y, w, h):
        a = self._sc(x)
        self.elements.append(tmpl_rect.substitute(dict(
            vll=str(31.567073-float(self._sc(y))),
            stlt=str(217.13317+float(self._sc(y))/2), 
            bbf=str(240.79368+float(self._sc(y))),
            bbbf=str(309.80338+float(self._sc(w))+float(self._sc(y))),
            dff=str(241.05511+float(self._sc(y))),
            hhd=str(350.00009 +2* (float(self._sc(y)))+ float(self._sc(w))),
            hhhd=str(417.95696 + 2*(float(self._sc(y)))+ 2*float(self._sc(w))),
            nw=str(-float(self._sc(w))),
            hhw=str(410.08961+2*float(self._sc(w))+2*float(self._sc(y))),
            nf=str(-float(self._sc(y))/2),
            ndf=str(-float(self._sc(y))),
            fdt=str(float(self._sc(y))/2),
            ww=str(-float(self._sc(w))),
            yh=str(20.827727+69.500437 +float(self._sc(y))),
            yhh=str(113+float(self._sc(y))+float(self._sc(y))),
            wh=str(-51.419828-float(self._sc(w))),
            f= self._sc(y), 
            vlu = str(74.580437+float(self._sc(y))),
            x=a, 
            l= str(79.660434+float(self._sc(y))),
            y=str(69.500437 +float(self._sc(y))), 
            w=self._sc(w), h=self._sc(h)),
            p=str(97.242956+float(self._sc(w)))))

    def drawClosedPath(self, p):
        s = "M{},{}".format(self._sc(p[0][0]), self._sc(p[0][1]))
        s += ''.join(["L{},{}".format(self._sc(pt[0]), self._sc(pt[1])) for pt in p[1:-1]])
        s += 'Z'
        self.elements.append(tmpl_path.substitute(dict(
            path=s,
            stroke_color=self._col(self.stroke_color),
            stroke_pixels=self._sc(self.line_width)
            )))

    def drawOpenPath(self, p):
        s = "M{},{}".format(self._sc(p[0][0]), self._sc(p[0][1]))
        s += ''.join(["L{},{}".format(self._sc(pt[0]), self._sc(pt[1])) for pt in p[1:]])
        self.elements.append(tmpl_path.substitute(dict(
            path=s,
            stroke_color=self._col(self.stroke_color),
            stroke_pixels=self._sc(self.line_width)
            )))

    def save(self):
        s = ''.join([e for e in self.elements])
        pgw, pgh = self._sc(self.page_size[0]), self._sc(self.page_size[1])
        # To support different DPI viewers, we shoudl encode the page size in points, not pixels.  This makes it work
        #  in both InkScape and Illustrator.
        svg = tmpl_svg.substitute(dict(
            point_width=self._pixel_to_point(pgw),
            point_height=self._pixel_to_point(pgh),
            contents=s))
        ofh = open(self.filename, 'w')
        ofh.write(svg)
        ofh.close()

    # end public API

    @staticmethod
    def _sc(v):
        # converts from mm to pixels as a numeric string
        return "{:.2f}".format(v)  # * 96 / 25.4)

    @staticmethod
    def _col(color):
        # generates a CSS color from a reportlab color
        return '#'+color.hexval()[2:]

    @staticmethod
    def _pixel_to_point(pixels):
        return "{:.2f}".format(float(pixels) * PIXEL_TO_POINT)
